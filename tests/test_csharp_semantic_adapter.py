from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from entroly.csharp_semantic import (
    CSharpAnalysisResult,
    CSharpSemanticAnalyzer,
    CSharpSemanticError,
    RoslynPayloadParser,
    RoslynProcessRunner,
)


class StubRunner:
    def __init__(self, payload: dict[str, object]) -> None:
        self.payload = payload
        self.calls: list[tuple[Path, bool]] = []

    def run_directory(self, directory: Path, *, strict: bool = False) -> dict[str, object]:
        self.calls.append((directory, strict))
        return self.payload


def test_payload_parser_maps_analysis_completeness_and_nested_contracts() -> None:
    parser = RoslynPayloadParser()

    result = parser.parse_result(
        {
            "status": "ok",
            "projectDir": "/tmp/project",
            "analysisCompleteness": "complete",
            "modules": [
                {
                    "path": "Assets/Runtime/Foo.cs",
                    "name": "Foo",
                    "language": "csharp",
                    "assembly": "Project.Runtime",
                    "rootNamespace": "Project.Runtime",
                    "assemblyReferences": ["Project.Core"],
                    "asmdef": {
                        "includePlatforms": ["Editor"],
                        "excludePlatforms": [],
                        "defineConstraints": ["UNITY_2022_3_OR_NEWER"],
                        "versionDefines": [{"name": "pkg", "expression": "1.0.0", "define": "HAS_PKG"}],
                        "precompiledReferences": ["Plugin.dll"],
                        "overrideReferences": True,
                        "noEngineReferences": False,
                        "autoReferenced": True,
                        "allowUnsafeCode": False,
                    },
                    "diagnostics": [{"code": "info-code", "severity": "info", "assembly": "Project.Runtime", "message": "ok"}],
                    "imports": ["Project.Core"],
                    "entities": [
                        {
                            "name": "Foo",
                            "kind": "class",
                            "filePath": "Assets/Runtime/Foo.cs",
                            "line": 3,
                            "docstring": "",
                            "signature": "class Project.Runtime.Foo",
                            "symbol": "Project.Runtime.Foo",
                            "returnType": "",
                            "dependencies": ["Project.Core.Bar"],
                        }
                    ],
                    "analysisCompleteness": "complete",
                    "loc": 10,
                }
            ],
        }
    )

    assert isinstance(result, CSharpAnalysisResult)
    assert result.analysis_completeness == "complete"
    assert result.modules[0].analysis_completeness == "complete"
    assert result.modules[0].asmdef.version_defines[0].define == "HAS_PKG"
    assert result.modules[0].diagnostics[0].code == "info-code"


def test_facade_passes_strict_to_runner_and_returns_parsed_result(tmp_path: Path) -> None:
    project_dir = tmp_path / "project"
    project_dir.mkdir()
    runner = StubRunner({"status": "ok", "projectDir": str(project_dir), "analysisCompleteness": "partial", "modules": []})
    analyzer = CSharpSemanticAnalyzer(strict=True, process_runner=runner, payload_parser=RoslynPayloadParser())

    result = analyzer.analyze_directory(str(project_dir))

    assert result.analysis_completeness == "partial"
    assert runner.calls == [(project_dir.resolve(), True)]


def test_process_runner_rejects_missing_directory(tmp_path: Path) -> None:
    runner = RoslynProcessRunner(dotnet_command="dotnet", analyzer_project=str(tmp_path / "missing.csproj"))

    with pytest.raises(CSharpSemanticError, match="not a directory"):
        runner.run_directory(tmp_path / "does-not-exist")


def test_process_runner_prefers_prebuilt_dll_and_uses_dotnet_exec(tmp_path: Path) -> None:
    project_dir = tmp_path / "project"
    project_dir.mkdir()
    analyzer_dll = tmp_path / "Entroly.CSharpAnalyzer.dll"
    analyzer_dll.write_text("placeholder", encoding="utf-8")
    runner = RoslynProcessRunner(dotnet_command="dotnet", analyzer_project=str(analyzer_dll))

    commands: list[list[str]] = []

    def fake_run(command: list[str], **_: object) -> subprocess.CompletedProcess[str]:
        commands.append(command)
        return subprocess.CompletedProcess(
            command,
            0,
            stdout=json.dumps({"status": "ok", "projectDir": str(project_dir), "analysisCompleteness": "complete", "modules": []}),
            stderr="",
        )

    with patch("entroly.csharp_semantic.subprocess.run", side_effect=fake_run):
        result = runner.run_directory(project_dir, strict=True)

    assert result["analysisCompleteness"] == "complete"
    assert commands == [["dotnet", "exec", str(analyzer_dll), "--strict", str(project_dir)]]
