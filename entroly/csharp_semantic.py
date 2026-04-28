"""Roslyn-backed C# semantic analysis adapter."""

from __future__ import annotations

import json
import os
import subprocess
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
    loc: int


@dataclass(frozen=True)
class CSharpAnalysisResult:
    project_dir: str
    modules: list[CSharpModule]


class CSharpSemanticAnalyzer:
    def __init__(self, dotnet_command: str | None = None, analyzer_project: str | None = None) -> None:
        self._dotnet_command = dotnet_command or os.environ.get("ENTROLY_DOTNET", "dotnet")
        self._analyzer_project = Path(analyzer_project) if analyzer_project else _default_analyzer_project()

    def analyze_directory(self, directory: str) -> CSharpAnalysisResult:
        project_dir = Path(directory).resolve()
        if not project_dir.is_dir():
            raise CSharpSemanticError(f"C# semantic analysis target is not a directory: {project_dir}")
        if not self._analyzer_project.is_file():
            raise CSharpSemanticError(f"Roslyn analyzer project not found: {self._analyzer_project}")

        command = [
            self._dotnet_command,
            "run",
            "--project",
            str(self._analyzer_project),
            "--",
            str(project_dir),
        ]
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
        return _parse_result(payload)


def _default_analyzer_project() -> Path:
    return Path(__file__).resolve().parent / "roslyn" / "Entroly.CSharpAnalyzer" / "Entroly.CSharpAnalyzer.csproj"


def _extract_error(stdout: str) -> str:
    if not stdout:
        return ""
    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError:
        return stdout
    error = payload.get("error")
    return str(error) if error else ""


def _parse_result(payload: dict[str, Any]) -> CSharpAnalysisResult:
    modules = [_parse_module(module) for module in payload.get("modules", [])]
    return CSharpAnalysisResult(project_dir=str(payload.get("projectDir", "")), modules=modules)


def _parse_module(payload: dict[str, Any]) -> CSharpModule:
    asmdef = _parse_asmdef(payload.get("asmdef", {}))
    return CSharpModule(
        path=str(payload.get("path", "")),
        name=str(payload.get("name", "")),
        language=str(payload.get("language", "csharp")),
        assembly=str(payload.get("assembly", "")),
        root_namespace=str(payload.get("rootNamespace", "")),
        assembly_references=[str(item) for item in payload.get("assemblyReferences", [])],
        include_platforms=asmdef.include_platforms,
        asmdef=asmdef,
        diagnostics=[_parse_diagnostic(item) for item in payload.get("diagnostics", [])],
        imports=[str(item) for item in payload.get("imports", [])],
        entities=[_parse_entity(entity) for entity in payload.get("entities", [])],
        loc=int(payload.get("loc", 0)),
    )


def _parse_asmdef(payload: Any) -> CSharpAsmdefMetadata:
    data = payload if isinstance(payload, dict) else {}
    return CSharpAsmdefMetadata(
        include_platforms=[str(item) for item in data.get("includePlatforms", [])],
        exclude_platforms=[str(item) for item in data.get("excludePlatforms", [])],
        define_constraints=[str(item) for item in data.get("defineConstraints", [])],
        version_defines=[_parse_version_define(item) for item in data.get("versionDefines", [])],
        precompiled_references=[str(item) for item in data.get("precompiledReferences", [])],
        override_references=bool(data.get("overrideReferences", False)),
        no_engine_references=bool(data.get("noEngineReferences", False)),
        auto_referenced=bool(data.get("autoReferenced", True)),
        allow_unsafe_code=bool(data.get("allowUnsafeCode", False)),
    )


def _parse_version_define(payload: Any) -> CSharpVersionDefine:
    data = payload if isinstance(payload, dict) else {}
    return CSharpVersionDefine(
        name=str(data.get("name", "")),
        expression=str(data.get("expression", "")),
        define=str(data.get("define", "")),
    )


def _parse_diagnostic(payload: Any) -> CSharpDiagnostic:
    data = payload if isinstance(payload, dict) else {}
    return CSharpDiagnostic(
        code=str(data.get("code", "")),
        severity=str(data.get("severity", "")),
        assembly=str(data.get("assembly", "")),
        message=str(data.get("message", "")),
    )


def _parse_entity(payload: dict[str, Any]) -> CSharpEntity:
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
