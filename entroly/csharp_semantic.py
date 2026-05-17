"""Roslyn-backed C# semantic analysis adapter."""

from __future__ import annotations

import json
import os
import subprocess
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class CSharpSemanticError(RuntimeError):
    """Raised when Roslyn semantic analysis cannot produce a valid contract."""


@dataclass(frozen=True)
class CSharpEntity:
    name: str
    kind: str
    file_path: str
    line: int
    docstring: str
    signature: str
    symbol: str
    return_type: str
    dependencies: list[str]


@dataclass(frozen=True)
class CSharpVersionDefine:
    name: str
    expression: str
    define: str


@dataclass(frozen=True)
class CSharpAsmdefMetadata:
    include_platforms: list[str]
    exclude_platforms: list[str]
    define_constraints: list[str]
    version_defines: list[CSharpVersionDefine]
    precompiled_references: list[str]
    override_references: bool
    no_engine_references: bool
    auto_referenced: bool
    allow_unsafe_code: bool


@dataclass(frozen=True)
class CSharpDiagnostic:
    code: str
    severity: str
    assembly: str
    message: str


@dataclass(frozen=True)
class CSharpModule:
    path: str
    name: str
    language: str
    assembly: str
    root_namespace: str
    assembly_references: list[str]
    include_platforms: list[str]
    asmdef: CSharpAsmdefMetadata
    diagnostics: list[CSharpDiagnostic]
    imports: list[str]
    entities: list[CSharpEntity]
    analysis_completeness: str
    loc: int


@dataclass(frozen=True)
class CSharpAnalysisResult:
    project_dir: str
    analysis_completeness: str
    modules: list[CSharpModule]


class RoslynProcessRunner:
    """Owns subprocess execution and error translation for the Roslyn analyzer."""

    def __init__(self, dotnet_command: str | None = None, analyzer_project: str | None = None) -> None:
        self._dotnet_command = dotnet_command or os.environ.get("ENTROLY_DOTNET", "dotnet")
        self._analyzer_project = Path(analyzer_project) if analyzer_project else _default_analyzer_project()

    @property
    def analyzer_project(self) -> Path:
        return self._analyzer_project

    def run_directory(self, directory: Path, *, strict: bool = False) -> dict[str, Any]:
        if not directory.is_dir():
            raise CSharpSemanticError(f"C# semantic analysis target is not a directory: {directory}")
        analyzer_artifact = self._ensure_analyzer_artifact()

        command = [
            self._dotnet_command,
            "exec",
            str(analyzer_artifact),
        ]
        if strict:
            command.append("--strict")
        command.append(str(directory))
        try:
            completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", check=False)
        except OSError as exc:
            raise CSharpSemanticError(f"Roslyn analyzer failed to start: {exc}") from exc

        stdout = completed.stdout.strip()
        if completed.returncode != 0:
            message = _extract_error(stdout) or completed.stderr.strip() or f"exit code {completed.returncode}"
            raise CSharpSemanticError(f"Roslyn analyzer failed: {message}")
        if not stdout:
            raise CSharpSemanticError("Roslyn analyzer returned empty output")

        try:
            payload = json.loads(stdout)
        except json.JSONDecodeError as exc:
            raise CSharpSemanticError(f"Roslyn analyzer returned invalid JSON: {exc}") from exc
        if payload.get("status") != "ok":
            raise CSharpSemanticError(_extract_error(stdout) or "Roslyn analyzer returned non-ok status")
        return payload

    def _ensure_analyzer_artifact(self) -> Path:
        if not self._analyzer_project.is_file():
            raise CSharpSemanticError(f"Roslyn analyzer project not found: {self._analyzer_project}")
        if self._analyzer_project.suffix.lower() == ".dll":
            return self._analyzer_project

        artifact = self._artifact_path_for_project()
        if self._artifact_is_current(artifact):
            return artifact

        build_command = [self._dotnet_command, "build", str(self._analyzer_project), "-nologo"]
        try:
            completed = subprocess.run(build_command, capture_output=True, text=True, encoding="utf-8", check=False)
        except OSError as exc:
            raise CSharpSemanticError(f"Roslyn analyzer build failed to start: {exc}") from exc
        if completed.returncode != 0:
            message = completed.stderr.strip() or completed.stdout.strip() or f"exit code {completed.returncode}"
            raise CSharpSemanticError(f"Roslyn analyzer build failed: {message}")
        if not artifact.is_file():
            raise CSharpSemanticError(f"Roslyn analyzer artifact not found after build: {artifact}")
        return artifact

    def _artifact_path_for_project(self) -> Path:
        assembly_name, target_framework = _read_project_output_metadata(self._analyzer_project)
        configuration = os.environ.get("ENTROLY_ROSLYN_BUILD_CONFIGURATION", "Debug")
        return self._analyzer_project.parent / "bin" / configuration / target_framework / f"{assembly_name}.dll"

    def _artifact_is_current(self, artifact: Path) -> bool:
        if not artifact.is_file():
            return False
        artifact_mtime = artifact.stat().st_mtime
        for source_file in self._source_files_for_project():
            try:
                if source_file.stat().st_mtime > artifact_mtime:
                    return False
            except OSError:
                return False
        return True

    def _source_files_for_project(self) -> list[Path]:
        if self._analyzer_project.suffix.lower() == ".dll":
            return [self._analyzer_project]
        project_dir = self._analyzer_project.parent
        source_files = [self._analyzer_project]
        for pattern in ("*.cs", "*.props", "*.targets"):
            source_files.extend(
                path
                for path in project_dir.rglob(pattern)
                if "bin" not in path.parts and "obj" not in path.parts
            )
        return source_files


class RoslynPayloadParser:
    """Owns JSON contract parsing for Roslyn analyzer payloads."""

    def parse_result(self, payload: dict[str, Any]) -> CSharpAnalysisResult:
        modules = [self._parse_module(module) for module in payload.get("modules", [])]
        return CSharpAnalysisResult(
            project_dir=str(payload.get("projectDir", "")),
            analysis_completeness=str(payload.get("analysisCompleteness", "partial")),
            modules=modules,
        )

    def _parse_module(self, payload: dict[str, Any]) -> CSharpModule:
        asmdef = self._parse_asmdef(payload.get("asmdef", {}))
        return CSharpModule(
            path=str(payload.get("path", "")),
            name=str(payload.get("name", "")),
            language=str(payload.get("language", "csharp")),
            assembly=str(payload.get("assembly", "")),
            root_namespace=str(payload.get("rootNamespace", "")),
            assembly_references=[str(item) for item in payload.get("assemblyReferences", [])],
            include_platforms=asmdef.include_platforms,
            asmdef=asmdef,
            diagnostics=[self._parse_diagnostic(item) for item in payload.get("diagnostics", [])],
            imports=[str(item) for item in payload.get("imports", [])],
            entities=[self._parse_entity(entity) for entity in payload.get("entities", [])],
            analysis_completeness=str(payload.get("analysisCompleteness", "partial")),
            loc=int(payload.get("loc", 0)),
        )

    def _parse_asmdef(self, payload: Any) -> CSharpAsmdefMetadata:
        data = payload if isinstance(payload, dict) else {}
        return CSharpAsmdefMetadata(
            include_platforms=[str(item) for item in data.get("includePlatforms", [])],
            exclude_platforms=[str(item) for item in data.get("excludePlatforms", [])],
            define_constraints=[str(item) for item in data.get("defineConstraints", [])],
            version_defines=[self._parse_version_define(item) for item in data.get("versionDefines", [])],
            precompiled_references=[str(item) for item in data.get("precompiledReferences", [])],
            override_references=bool(data.get("overrideReferences", False)),
            no_engine_references=bool(data.get("noEngineReferences", False)),
            auto_referenced=bool(data.get("autoReferenced", True)),
            allow_unsafe_code=bool(data.get("allowUnsafeCode", False)),
        )

    def _parse_version_define(self, payload: Any) -> CSharpVersionDefine:
        data = payload if isinstance(payload, dict) else {}
        return CSharpVersionDefine(
            name=str(data.get("name", "")),
            expression=str(data.get("expression", "")),
            define=str(data.get("define", "")),
        )

    def _parse_diagnostic(self, payload: Any) -> CSharpDiagnostic:
        data = payload if isinstance(payload, dict) else {}
        return CSharpDiagnostic(
            code=str(data.get("code", "")),
            severity=str(data.get("severity", "")),
            assembly=str(data.get("assembly", "")),
            message=str(data.get("message", "")),
        )

    def _parse_entity(self, payload: dict[str, Any]) -> CSharpEntity:
        return CSharpEntity(
            name=str(payload.get("name", "")),
            kind=str(payload.get("kind", "")),
            file_path=str(payload.get("filePath", "")),
            line=int(payload.get("line", 0)),
            docstring=str(payload.get("docstring", "")),
            signature=str(payload.get("signature", "")),
            symbol=str(payload.get("symbol", "")),
            return_type=str(payload.get("returnType", "")),
            dependencies=[str(item) for item in payload.get("dependencies", [])],
        )


class CSharpSemanticAnalyzer:
    """Facade that validates input and coordinates Roslyn execution + payload parsing."""

    def __init__(
        self,
        dotnet_command: str | None = None,
        analyzer_project: str | None = None,
        *,
        strict: bool = False,
        process_runner: RoslynProcessRunner | None = None,
        payload_parser: RoslynPayloadParser | None = None,
    ) -> None:
        self._strict = strict
        self._process_runner = process_runner or RoslynProcessRunner(
            dotnet_command=dotnet_command,
            analyzer_project=analyzer_project,
        )
        self._payload_parser = payload_parser or RoslynPayloadParser()

    def analyze_directory(self, directory: str) -> CSharpAnalysisResult:
        project_dir = Path(directory).resolve()
        payload = self._process_runner.run_directory(project_dir, strict=self._strict)
        return self._payload_parser.parse_result(payload)


def _default_analyzer_project() -> Path:
    return Path(__file__).resolve().parent / "roslyn" / "Entroly.CSharpAnalyzer" / "Entroly.CSharpAnalyzer.csproj"


def _read_project_output_metadata(project_file: Path) -> tuple[str, str]:
    tree = ET.parse(project_file)
    root = tree.getroot()
    assembly_name = None
    target_framework = None
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        text = (element.text or "").strip()
        if not text:
            continue
        if tag == "AssemblyName" and assembly_name is None:
            assembly_name = text
        elif tag == "TargetFramework" and target_framework is None:
            target_framework = text
        elif tag == "TargetFrameworks" and target_framework is None:
            target_framework = text.split(";", 1)[0].strip()

    if not target_framework:
        raise CSharpSemanticError(f"Roslyn analyzer project does not declare TargetFramework: {project_file}")
    return assembly_name or project_file.stem, target_framework


def _extract_error(stdout: str) -> str:
    if not stdout:
        return ""
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout
    error = payload.get("error")
    return str(error) if error else ""
