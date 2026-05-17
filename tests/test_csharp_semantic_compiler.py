import os
import subprocess
from pathlib import Path

import pytest

from entroly.belief_compiler import BeliefCompiler, extract_entities
from entroly.csharp_semantic import CSharpSemanticAnalyzer, CSharpSemanticError
from entroly.vault import VaultConfig, VaultManager


DOTNET = os.environ.get("ENTROLY_DOTNET", "dotnet")


def write_unity_project(root: Path) -> Path:
    runtime = root / "Assets" / "Runtime"
    editor = root / "Assets" / "Editor"
    runtime.mkdir(parents=True)
    editor.mkdir(parents=True)

    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": []
}
""".strip(),
        encoding="utf-8",
    )
    (runtime / "MapDocument.cs").write_text(
        """
namespace ProjectStrategy.Runtime;

public sealed class MapDocument
{
    public string Id { get; }

    public MapDocument(string id)
    {
        Id = id;
    }
}
""".strip(),
        encoding="utf-8",
    )

    (editor / "ProjectStrategy.Editor.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Editor",
  "rootNamespace": "ProjectStrategy.Editor",
  "references": ["ProjectStrategy.Runtime"],
  "includePlatforms": ["Editor"]
}
""".strip(),
        encoding="utf-8",
    )
    controller = editor / "MapEditorController.cs"
    controller.write_text(
        """
using ProjectStrategy.Runtime;

namespace ProjectStrategy.Editor;

public sealed class MapEditorController
{
    private readonly MapDocument _document;

    public MapEditorController(MapDocument document)
    {
        _document = document;
    }

    public string DisplayName => _document.Id;
}
""".strip(),
        encoding="utf-8",
    )
    return controller


def write_unity_project_with_guid_reference(root: Path) -> Path:
    runtime = root / "Assets" / "Runtime"
    editor = root / "Assets" / "Editor"
    runtime.mkdir(parents=True)
    editor.mkdir(parents=True)
    runtime_guid = "11111111111111111111111111111111"

    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": []
}
""".strip(),
        encoding="utf-8",
    )
    (runtime / "ProjectStrategy.Runtime.asmdef.meta").write_text(
        f"fileFormatVersion: 2\nguid: {runtime_guid}\n",
        encoding="utf-8",
    )
    (runtime / "MapDocument.cs").write_text(
        """
namespace ProjectStrategy.Runtime;

public sealed class MapDocument
{
}
""".strip(),
        encoding="utf-8",
    )

    (editor / "ProjectStrategy.Editor.asmdef").write_text(
        f"""
{{
  "name": "ProjectStrategy.Editor",
  "rootNamespace": "ProjectStrategy.Editor",
  "references": ["GUID:{runtime_guid}"],
  "includePlatforms": ["Editor"]
}}
""".strip(),
        encoding="utf-8",
    )
    controller = editor / "MapEditorController.cs"
    controller.write_text(
        """
using ProjectStrategy.Runtime;

namespace ProjectStrategy.Editor;

public sealed class MapEditorController
{
    public MapEditorController(MapDocument document)
    {
    }
}
""".strip(),
        encoding="utf-8",
    )
    return controller


def write_unity_project_with_extended_asmdef(root: Path) -> Path:
    editor = root / "Assets" / "Editor"
    editor.mkdir(parents=True)

    (editor / "ProjectStrategy.Editor.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Editor",
  "rootNamespace": "ProjectStrategy.Editor",
  "references": ["GUID:22222222222222222222222222222222"],
  "includePlatforms": ["Editor"],
  "excludePlatforms": ["Android"],
  "defineConstraints": ["UNITY_2022_3_OR_NEWER", "!DISABLE_EDITOR"],
  "versionDefines": [
    {
      "name": "com.unity.inputsystem",
      "expression": "1.7.0",
      "define": "HAS_INPUT_SYSTEM"
    }
  ],
  "precompiledReferences": ["ProjectStrategy.Native.dll"],
  "overrideReferences": true,
  "noEngineReferences": true,
  "autoReferenced": false,
  "allowUnsafeCode": true
}
""".strip(),
        encoding="utf-8",
    )
    marker = editor / "UnsafeEditorMarker.cs"
    marker.write_text(
        """
namespace ProjectStrategy.Editor;

public unsafe sealed class UnsafeEditorMarker
{
    public int Value { get; }
}
""".strip(),
        encoding="utf-8",
    )
    return marker


def write_unity_project_with_resolved_context(root: Path) -> Path:
    runtime = root / "Assets" / "Runtime"
    editor = root / "Assets" / "Editor"
    plugins = root / "Assets" / "Plugins"
    runtime.mkdir(parents=True)
    editor.mkdir(parents=True)
    plugins.mkdir(parents=True)
    runtime_guid = "33333333333333333333333333333333"
    plugin_dll = build_csharp_library(
        root / "build",
        "ProjectStrategy.Native",
        """
namespace ProjectStrategy.Native;

public sealed class NativeService
{
    public string Name => "native";
}
""",
    )
    (plugins / plugin_dll.name).write_bytes(plugin_dll.read_bytes())

    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": []
}
""".strip(),
        encoding="utf-8",
    )
    (runtime / "ProjectStrategy.Runtime.asmdef.meta").write_text(
        f"fileFormatVersion: 2\nguid: {runtime_guid}\n",
        encoding="utf-8",
    )
    (runtime / "MapDocument.cs").write_text(
        """
namespace ProjectStrategy.Runtime;

public sealed class MapDocument
{
}
""".strip(),
        encoding="utf-8",
    )
    (editor / "ProjectStrategy.Editor.asmdef").write_text(
        f"""
{{
  "name": "ProjectStrategy.Editor",
  "rootNamespace": "ProjectStrategy.Editor",
  "references": ["GUID:{runtime_guid}"],
  "includePlatforms": ["Editor"],
  "defineConstraints": ["UNITY_2022_3_OR_NEWER", "!DISABLE_EDITOR"],
  "versionDefines": [
    {{
      "name": "com.unity.inputsystem",
      "expression": "1.7.0",
      "define": "HAS_INPUT_SYSTEM"
    }}
  ],
  "precompiledReferences": ["ProjectStrategy.Native.dll"],
  "overrideReferences": true,
  "noEngineReferences": true,
  "autoReferenced": false,
  "allowUnsafeCode": true
}}
""".strip(),
        encoding="utf-8",
    )
    marker = editor / "UnsafeEditorMarker.cs"
    marker.write_text(
        """
using ProjectStrategy.Native;

namespace ProjectStrategy.Editor;

public unsafe sealed class UnsafeEditorMarker
{
    public NativeService Service { get; }

    public UnsafeEditorMarker(NativeService service)
    {
        Service = service;
    }
}
""".strip(),
        encoding="utf-8",
    )
    return marker


def write_unity_project_with_asmref(root: Path) -> Path:
    runtime = root / "Assets" / "Runtime"
    features = root / "Assets" / "Features"
    runtime.mkdir(parents=True)
    features.mkdir(parents=True)

    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": []
}
""".strip(),
        encoding="utf-8",
    )
    runtime_guid = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    (runtime / "ProjectStrategy.Runtime.asmdef.meta").write_text(
        f"fileFormatVersion: 2\nguid: {runtime_guid}\n",
        encoding="utf-8",
    )
    (runtime / "MapDocument.cs").write_text(
        """
namespace ProjectStrategy.Runtime;

public sealed class MapDocument
{
}
""".strip(),
        encoding="utf-8",
    )
    (features / "Gameplay.asmref").write_text(
        f"""
{{
  "reference": "GUID:{runtime_guid}"
}}
""".strip(),
        encoding="utf-8",
    )
    feature_file = features / "GameplayFeature.cs"
    feature_file.write_text(
        """
using ProjectStrategy.Runtime;

namespace ProjectStrategy.Runtime;

public sealed class GameplayFeature
{
    public MapDocument Create() => new();
}
""".strip(),
        encoding="utf-8",
    )
    return feature_file


def write_project_version(root: Path, version: str) -> None:
    settings = root / "ProjectSettings"
    settings.mkdir(parents=True, exist_ok=True)
    (settings / "ProjectVersion.txt").write_text(
        f"m_EditorVersion: {version}\n",
        encoding="utf-8",
    )


def write_packages_lock(root: Path, versions: dict[str, str]) -> None:
    packages = root / "Packages"
    packages.mkdir(parents=True, exist_ok=True)
    deps = ",\n".join(
        f'    "{name}": {{"version": "{version}"}}'
        for name, version in versions.items()
    )
    (packages / "packages-lock.json").write_text(
        "{\n  \"dependencies\": {\n" + deps + "\n  }\n}\n",
        encoding="utf-8",
    )


def build_csharp_library(
    root: Path,
    assembly_name: str,
    source_code: str,
    *,
    target_framework: str = "net8.0",
) -> Path:
    project_dir = root / assembly_name
    project_dir.mkdir(parents=True, exist_ok=True)
    csproj = project_dir / f"{assembly_name}.csproj"
    csproj.write_text(
        f"""
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>{target_framework}</TargetFramework>
    <AssemblyName>{assembly_name}</AssemblyName>
    <Nullable>enable</Nullable>
  </PropertyGroup>
</Project>
""".strip(),
        encoding="utf-8",
    )
    (project_dir / "Library.cs").write_text(source_code.strip(), encoding="utf-8")
    subprocess.run(
        [DOTNET, "build", str(csproj), "-c", "Release", "-nologo"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    built = project_dir / "bin" / "Release" / target_framework / f"{assembly_name}.dll"
    assert built.is_file(), f"expected built DLL at {built}"
    return built


def test_roslyn_analyzer_reports_unity_asmdef_and_semantic_symbols(tmp_path):
    source_file = write_unity_project(tmp_path)

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    editor_module = next(module for module in result.modules if module.path == expected_path)
    assert editor_module.language == "csharp"
    assert editor_module.assembly == "ProjectStrategy.Editor"
    assert editor_module.root_namespace == "ProjectStrategy.Editor"
    assert editor_module.assembly_references == ["ProjectStrategy.Runtime"]

    controller = next(entity for entity in editor_module.entities if entity.name == "MapEditorController")
    assert controller.symbol == "ProjectStrategy.Editor.MapEditorController"
    assert controller.kind == "class"

    display_name = next(entity for entity in editor_module.entities if entity.name == "DisplayName")
    assert display_name.kind == "property"
    assert display_name.return_type == "string"


def test_roslyn_analyzer_resolves_unity_asmdef_guid_references(tmp_path):
    source_file = write_unity_project_with_guid_reference(tmp_path)

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    editor_module = next(module for module in result.modules if module.path == expected_path)
    assert editor_module.assembly_references == ["ProjectStrategy.Runtime"]
    assert editor_module.include_platforms == ["Editor"]
    constructor = next(
        entity for entity in editor_module.entities if entity.name == "MapEditorController" and entity.kind == "function"
    )
    assert "ProjectStrategy.Runtime.MapDocument document" in constructor.signature


def test_belief_compiler_uses_roslyn_for_csharp_and_writes_asmdef_metadata(tmp_path):
    source_file = write_unity_project(tmp_path / "project")
    vault = VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))
    vault.ensure_structure()

    result = BeliefCompiler(vault).compile_directory(str(tmp_path / "project"))

    assert result.files_processed == 2
    assert result.beliefs_written >= 2
    belief = vault.read_belief("mapeditorcontroller")
    assert belief is not None
    body = belief["body"]
    assert "**Language:** csharp" in body
    assert "**Assembly:** ProjectStrategy.Editor" in body
    assert "**Root namespace:** ProjectStrategy.Editor" in body
    assert "ProjectStrategy.Runtime" in body
    assert "MapEditorController(ProjectStrategy.Runtime.MapDocument document)" in body
    assert str(source_file.relative_to(tmp_path / "project")).replace(os.sep, "/") in belief["frontmatter"]["sources"][0]


def test_csharp_compile_fails_when_roslyn_analyzer_is_unavailable(tmp_path, monkeypatch):
    write_unity_project(tmp_path)
    monkeypatch.setenv("ENTROLY_DOTNET", str(tmp_path / "missing-dotnet.exe"))

    with pytest.raises(CSharpSemanticError):
        BeliefCompiler(VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))).compile_directory(str(tmp_path))


def test_csharp_regex_path_is_removed():
    assert extract_entities("public sealed class ShouldNotParse {}", "ShouldNotParse.cs") == []


def test_single_file_csharp_compile_requires_project_context(tmp_path):
    compiler = BeliefCompiler(VaultManager(VaultConfig(base_path=str(tmp_path / "vault"))))

    with pytest.raises(ValueError, match="Roslyn"):
        compiler.compile_file("Assets/Runtime/MapDocument.cs", "public sealed class MapDocument {}")


def test_roslyn_analyzer_reports_default_assembly_csharp_without_asmdef(tmp_path):
    source_dir = tmp_path / "Assets" / "Scripts"
    source_dir.mkdir(parents=True)
    source_file = source_dir / "DefaultAssemblyType.cs"
    source_file.write_text(
        """
namespace ProjectStrategy;

public sealed class DefaultAssemblyType
{
}
""".strip(),
        encoding="utf-8",
    )

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    assert module.assembly == "Assembly-CSharp"
    assert module.analysis_completeness == "partial"


def test_compile_directory_skips_csharp_build_artifact_directories(tmp_path):
    source_dir = tmp_path / "project" / "Assets" / "Scripts"
    obj_dir = tmp_path / "project" / "obj" / "Debug" / "net8.0"
    bin_dir = tmp_path / "project" / "bin" / "Debug" / "net8.0"
    source_dir.mkdir(parents=True)
    obj_dir.mkdir(parents=True)
    bin_dir.mkdir(parents=True)
    (source_dir / "GameplayType.cs").write_text("public sealed class GameplayType {}", encoding="utf-8")
    (obj_dir / "GeneratedAssemblyInfo.cs").write_text("public sealed class GeneratedAssemblyInfo {}", encoding="utf-8")
    (bin_dir / "GeneratedGlobalUsings.g.cs").write_text("public sealed class GeneratedGlobalUsings {}", encoding="utf-8")
    compiler = BeliefCompiler(VaultManager(VaultConfig(base_path=str(tmp_path / "vault"))))

    files = compiler._walk_source_files(tmp_path / "project", max_files=0)

    relative = {str(path.relative_to(tmp_path / "project")).replace(os.sep, "/") for path in files}
    assert "Assets/Scripts/GameplayType.cs" in relative
    assert "obj/Debug/net8.0/GeneratedAssemblyInfo.cs" not in relative
    assert "bin/Debug/net8.0/GeneratedGlobalUsings.g.cs" not in relative


def test_csharp_compile_fails_when_selected_file_is_not_returned(tmp_path):
    project = tmp_path / "project"
    skipped = project / "Library"
    skipped.mkdir(parents=True)
    (skipped / "Generated.cs").write_text("public sealed class Generated {}", encoding="utf-8")

    compiler = BeliefCompiler(VaultManager(VaultConfig(base_path=str(tmp_path / "vault"))))

    with pytest.raises(CSharpSemanticError, match="Generated.cs"):
        compiler.compile_paths(str(project), ["Library/Generated.cs"])

def test_roslyn_analyzer_records_extended_unity_asmdef_metadata_and_diagnostics(tmp_path):
    source_file = write_unity_project_with_extended_asmdef(tmp_path)

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    assert module.include_platforms == ["Editor"]
    assert module.asmdef.exclude_platforms == ["Android"]
    assert module.asmdef.define_constraints == ["!DISABLE_EDITOR", "UNITY_2022_3_OR_NEWER"]
    assert [(item.name, item.expression, item.define) for item in module.asmdef.version_defines] == [
        ("com.unity.inputsystem", "1.7.0", "HAS_INPUT_SYSTEM")
    ]
    assert module.asmdef.precompiled_references == ["ProjectStrategy.Native.dll"]
    assert module.asmdef.override_references is True
    assert module.asmdef.no_engine_references is True
    assert module.asmdef.auto_referenced is False
    assert module.asmdef.allow_unsafe_code is True

    diagnostics = {item.code: item for item in module.diagnostics}
    assert diagnostics["asmdef-platform-conflict"].severity == "error"
    assert diagnostics["asmdef-unresolved-guid-reference"].severity == "warning"
    assert diagnostics["asmdef-define-constraints-not-evaluated"].severity == "warning"
    assert diagnostics["asmdef-version-defines-not-evaluated"].severity == "warning"
    assert diagnostics["asmdef-precompiled-reference-missing"].severity == "warning"
    assert diagnostics["asmdef-no-engine-references-recorded"].severity == "info"
    assert diagnostics["asmdef-auto-referenced-recorded"].severity == "info"
    assert diagnostics["asmdef-allow-unsafe-code-applied"].severity == "info"


def test_roslyn_analyzer_resolves_asmref_directory_to_target_assembly(tmp_path):
    source_file = write_unity_project_with_asmref(tmp_path)

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    assert module.assembly == "ProjectStrategy.Runtime"
    assert module.root_namespace == "ProjectStrategy.Runtime"
    factory = next(entity for entity in module.entities if entity.name == "Create")
    assert factory.return_type == "MapDocument"


def test_roslyn_analyzer_reports_complete_analysis_when_context_is_explicit(tmp_path, monkeypatch):
    source_file = write_unity_project_with_resolved_context(tmp_path)
    write_project_version(tmp_path, "2022.3.20f1")
    write_packages_lock(tmp_path, {"com.unity.inputsystem": "1.7.0"})
    monkeypatch.setenv("ENTROLY_UNITY_DEFINE_SYMBOLS", "")

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    assert result.analysis_completeness == "complete"
    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    assert module.analysis_completeness == "complete"
    diagnostics = {item.code: item for item in module.diagnostics}
    assert "asmdef-define-constraints-not-evaluated" not in diagnostics
    assert "asmdef-version-defines-not-evaluated" not in diagnostics
    assert "asmdef-unresolved-guid-reference" not in diagnostics
    assert "asmdef-precompiled-reference-missing" not in diagnostics


def test_roslyn_analyzer_strict_mode_rejects_partial_analysis(tmp_path):
    write_unity_project_with_extended_asmdef(tmp_path)

    with pytest.raises(CSharpSemanticError, match="strict"):
        CSharpSemanticAnalyzer(strict=True).analyze_directory(str(tmp_path))


def test_roslyn_analyzer_loads_precompiled_reference_metadata(tmp_path):
    plugin_dll = build_csharp_library(
        tmp_path / "build",
        "ProjectStrategy.Native",
        """
namespace ProjectStrategy.Native;

public sealed class NativeService
{
    public string Name => "native";
}
""",
    )
    plugins = tmp_path / "Assets" / "Plugins"
    runtime = tmp_path / "Assets" / "Runtime"
    plugins.mkdir(parents=True)
    runtime.mkdir(parents=True)
    (plugins / plugin_dll.name).write_bytes(plugin_dll.read_bytes())
    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": [],
  "overrideReferences": true,
  "precompiledReferences": ["ProjectStrategy.Native.dll"]
}
""".strip(),
        encoding="utf-8",
    )
    source_file = runtime / "NativeConsumer.cs"
    source_file.write_text(
        """
using ProjectStrategy.Native;

namespace ProjectStrategy.Runtime;

public sealed class NativeConsumer
{
    public NativeService Service { get; }

    public NativeConsumer(NativeService service)
    {
        Service = service;
    }
}
""".strip(),
        encoding="utf-8",
    )

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    constructor = next(
        entity for entity in module.entities if entity.name == "NativeConsumer" and entity.kind == "function"
    )
    assert "ProjectStrategy.Native.NativeService service" in constructor.signature
    assert "ProjectStrategy.Native.NativeService" in constructor.dependencies


def test_roslyn_analyzer_loads_unity_managed_metadata_from_explicit_dir(tmp_path, monkeypatch):
    managed_dir = tmp_path / "UnityManaged"
    unity_engine_dll = build_csharp_library(
        managed_dir,
        "UnityEngine",
        """
namespace UnityEngine;

public class MonoBehaviour
{
}
""",
    )
    managed_output = managed_dir / "managed"
    managed_output.mkdir(parents=True, exist_ok=True)
    target_dll = managed_output / unity_engine_dll.name
    target_dll.write_bytes(unity_engine_dll.read_bytes())
    monkeypatch.setenv("ENTROLY_UNITY_MANAGED_DIR", str(managed_output))

    runtime = tmp_path / "Assets" / "Runtime"
    runtime.mkdir(parents=True)
    (runtime / "ProjectStrategy.Runtime.asmdef").write_text(
        """
{
  "name": "ProjectStrategy.Runtime",
  "rootNamespace": "ProjectStrategy.Runtime",
  "references": []
}
""".strip(),
        encoding="utf-8",
    )
    source_file = runtime / "GameplayComponent.cs"
    source_file.write_text(
        """
using UnityEngine;

namespace ProjectStrategy.Runtime;

public sealed class GameplayComponent : MonoBehaviour
{
}
""".strip(),
        encoding="utf-8",
    )

    result = CSharpSemanticAnalyzer().analyze_directory(str(tmp_path))

    expected_path = str(source_file.relative_to(tmp_path)).replace(os.sep, "/")
    module = next(item for item in result.modules if item.path == expected_path)
    component = next(entity for entity in module.entities if entity.name == "GameplayComponent")
    assert "UnityEngine.MonoBehaviour" in component.dependencies


def test_belief_compiler_writes_extended_asmdef_metadata_and_diagnostics(tmp_path):
    write_unity_project_with_extended_asmdef(tmp_path / "project")
    vault = VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))
    vault.ensure_structure()

    result = BeliefCompiler(vault).compile_directory(str(tmp_path / "project"))

    assert result.errors == []
    belief = vault.read_belief("unsafeeditormarker")
    assert belief is not None
    body = belief["body"]
    assert "**Unity include platforms:** Editor" in body
    assert "**Unity exclude platforms:** Android" in body
    assert "**Unity define constraints:** !DISABLE_EDITOR, UNITY_2022_3_OR_NEWER" in body
    assert "**Unity version defines:** com.unity.inputsystem:1.7.0:HAS_INPUT_SYSTEM" in body
    assert "**Unity precompiled references:** ProjectStrategy.Native.dll" in body
    assert "**Unity override references:** true" in body
    assert "**Unity no engine references:** true" in body
    assert "**Unity auto referenced:** false" in body
    assert "**Unity allow unsafe code:** true" in body
    assert "**Analysis completeness:** partial" in body
    assert "## Diagnostics" in body
    assert "error:asmdef-platform-conflict" in body
    assert "warning:asmdef-define-constraints-not-evaluated" in body
    assert "warning:asmdef-version-defines-not-evaluated" in body
    assert "warning:asmdef-precompiled-reference-missing" in body
    assert "info:asmdef-allow-unsafe-code-applied" in body


def test_roslyn_package_config_includes_analyzer_sources_and_excludes_build_outputs():
    if not hasattr(__import__("sys"), "stdlib_module_names"):
        pytest.skip("pyproject structural check requires Python 3.10+ runtime details")

    import sys

    if sys.version_info < (3, 11):
        pytest.skip("tomllib is available in Python 3.11+")
    import tomllib

    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    build_config = pyproject["tool"]["hatch"]["build"]
    wheel_config = build_config["targets"]["wheel"]

    assert "entroly/roslyn/Entroly.CSharpAnalyzer/*.csproj" in wheel_config["artifacts"]
    assert "entroly/roslyn/Entroly.CSharpAnalyzer/*.cs" in wheel_config["artifacts"]
    assert "entroly/roslyn/Entroly.CSharpAnalyzer/bin" in build_config["exclude"]
    assert "entroly/roslyn/Entroly.CSharpAnalyzer/obj" in build_config["exclude"]
