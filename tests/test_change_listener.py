from entroly.belief_compiler import BeliefCompiler
from entroly.change_listener import WorkspaceChangeListener
from entroly.change_pipeline import ChangePipeline
from entroly.verification_engine import VerificationEngine
from entroly.vault import VaultConfig, VaultManager


def test_workspace_change_listener_syncs_changed_file(tmp_path):
    project = tmp_path / "project"
    project.mkdir()
    src = project / "auth.py"
    src.write_text(
        """class AuthService:
    def verify_token(self, token: str) -> bool:
        return bool(token)
""",
        encoding="utf-8",
    )

    vault = VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))
    compiler = BeliefCompiler(vault)
    verifier = VerificationEngine(vault)
    change_pipe = ChangePipeline(vault, verifier)
    listener = WorkspaceChangeListener(vault, compiler, verifier, change_pipe, str(project))

    first = listener.scan_once(force=True)
    assert first.status == "synced"
    assert first.beliefs_written >= 1
    assert first.action_path
    assert vault.read_belief("auth") is not None

    src.write_text(
        """class AuthService:
    def verify_token(self, token: str) -> bool:
        return bool(token)

    def rotate_keys(self) -> None:
        return None
""",
        encoding="utf-8",
    )

    second = listener.scan_once()
    assert second.status == "synced"
    assert "auth.py" in second.changed_files
    assert second.beliefs_written >= 1
    assert second.verification_summary["total_beliefs_checked"] >= 1


def test_workspace_change_listener_syncs_csharp_with_project_context(tmp_path):
    project = tmp_path / "project"
    runtime = project / "Assets" / "Runtime"
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
    src = runtime / "MapDocument.cs"
    src.write_text(
        """
namespace ProjectStrategy.Runtime;

public sealed class MapDocument
{
    public string Id { get; }
}
""".strip(),
        encoding="utf-8",
    )

    vault = VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))
    compiler = BeliefCompiler(vault)
    verifier = VerificationEngine(vault)
    change_pipe = ChangePipeline(vault, verifier)
    listener = WorkspaceChangeListener(vault, compiler, verifier, change_pipe, str(project))

    result = listener.scan_once(force=True)

    assert result.status == "synced"
    assert "Assets/Runtime/MapDocument.cs" in result.changed_files
    assert result.beliefs_written >= 1
    belief = vault.read_belief("mapdocument")
    assert belief is not None
    assert "**Assembly:** ProjectStrategy.Runtime" in belief["body"]


def test_workspace_change_listener_skips_unity_generated_directories(tmp_path):
    project = tmp_path / "project"
    library = project / "Library"
    library.mkdir(parents=True)
    (library / "Generated.cs").write_text("public sealed class Generated {}", encoding="utf-8")

    vault = VaultManager(VaultConfig(base_path=str(tmp_path / "vault")))
    compiler = BeliefCompiler(vault)
    verifier = VerificationEngine(vault)
    change_pipe = ChangePipeline(vault, verifier)
    listener = WorkspaceChangeListener(vault, compiler, verifier, change_pipe, str(project))

    result = listener.scan_once(force=True)

    assert result.status == "synced"
    assert result.scanned_files == 0
    assert result.changed_files == []
    assert result.beliefs_written == 0
