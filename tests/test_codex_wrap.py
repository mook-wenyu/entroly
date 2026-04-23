from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

from entroly.cli import _ensure_loopback_no_proxy, cmd_wrap  # noqa: E402
from entroly.codex_integration import (  # noqa: E402
    build_codex_override_args,
    parse_codex_cli_selection,
    prepare_codex_wrap,
    resolve_openai_proxy_route,
)
from entroly.launching import resolve_launch_cmd, resolve_python_cmd  # noqa: E402


def test_parse_codex_cli_selection_profile_and_provider_override():
    selection = parse_codex_cli_selection(
        ["--profile", "proxy", "--config", 'model_provider="sub2api"']
    )
    assert selection.profile == "proxy"
    assert selection.provider_override == "sub2api"


def test_parse_codex_cli_selection_rejects_manual_base_url_override():
    with pytest.raises(ValueError, match="base_url"):
        parse_codex_cli_selection(
            ["--config", 'model_providers.sub2api.base_url="http://127.0.0.1:9377"']
        )


def test_build_codex_override_args_for_openai():
    args = build_codex_override_args(
        provider=type(
            "Provider",
            (),
            {"provider_id": "openai"},
        )(),
        proxy_base_url="http://127.0.0.1:9377/v1",
    )
    assert args == [
        "--config",
        'openai_base_url="http://127.0.0.1:9377/v1"',
        "--config",
        "features.responses_websockets_v2=false",
    ]


def test_prepare_codex_wrap_reads_custom_provider_from_config(tmp_path: Path):
    codex_home = tmp_path / ".codex"
    codex_home.mkdir()
    (codex_home / "config.toml").write_text(
        """
model_provider = "sub2api"

[model_providers.sub2api]
name = "sub2api"
base_url = "https://api.mookbot.com"
wire_api = "responses"
""".strip(),
        encoding="utf-8",
    )

    plan = prepare_codex_wrap(
        [],
        port=9377,
        env={"CODEX_HOME": str(codex_home)},
    )

    assert plan.provider.provider_id == "sub2api"
    assert plan.provider.base_url == "https://api.mookbot.com"
    assert plan.proxy_base_url == "http://127.0.0.1:9377"
    assert plan.env_updates["ENTROLY_OPENAI_BASE"] == "https://api.mookbot.com"
    assert plan.override_args == [
        "--config",
        'model_providers.sub2api.base_url="http://127.0.0.1:9377"',
        "--config",
        "model_providers.sub2api.responses_websockets_v2=false",
        "--config",
        "model_providers.sub2api.supports_websockets=false",
        "--config",
        "features.responses_websockets_v2=false",
    ]


def test_prepare_codex_wrap_uses_profile_provider(tmp_path: Path):
    codex_home = tmp_path / ".codex"
    codex_home.mkdir()
    (codex_home / "config.toml").write_text(
        """
model_provider = "openai"

[profiles.proxy]
model_provider = "azure"

[model_providers.azure]
name = "Azure"
base_url = "https://example.openai.azure.com/openai"
wire_api = "responses"
""".strip(),
        encoding="utf-8",
    )

    plan = prepare_codex_wrap(
        ["--profile", "proxy"],
        port=9377,
        env={"CODEX_HOME": str(codex_home)},
    )

    assert plan.provider.provider_id == "azure"
    assert plan.proxy_base_url == "http://127.0.0.1:9377/openai"
    assert plan.env_updates["ENTROLY_OPENAI_BASE"] == "https://example.openai.azure.com/openai"
    assert plan.override_args == [
        "--config",
        'model_providers.azure.base_url="http://127.0.0.1:9377/openai"',
        "--config",
        "model_providers.azure.responses_websockets_v2=false",
        "--config",
        "model_providers.azure.supports_websockets=false",
        "--config",
        "features.responses_websockets_v2=false",
    ]


def test_prepare_codex_wrap_supports_explicit_provider_without_config():
    plan = prepare_codex_wrap(
        [],
        port=9377,
        provider_id="sub2api",
        base_url="https://api.mookbot.com/v1",
    )

    assert plan.proxy_base_url == "http://127.0.0.1:9377/v1"
    assert plan.env_updates["ENTROLY_OPENAI_BASE"] == "https://api.mookbot.com/v1"


def test_resolve_openai_proxy_route_uses_active_codex_provider(tmp_path: Path, monkeypatch):
    codex_home = tmp_path / ".codex"
    codex_home.mkdir()
    (codex_home / "config.toml").write_text(
        """
model_provider = "sub2api"

[model_providers.sub2api]
name = "sub2api"
base_url = "https://api.mookbot.com"
wire_api = "responses"
""".strip(),
        encoding="utf-8",
    )

    monkeypatch.delenv("ENTROLY_OPENAI_BASE", raising=False)
    monkeypatch.setenv("CODEX_HOME", str(codex_home))

    route = resolve_openai_proxy_route(port=9377, env={"CODEX_HOME": str(codex_home)})

    assert route.upstream_base_url == "https://api.mookbot.com"
    assert route.upstream_origin == "https://api.mookbot.com"
    assert route.proxy_base_url == "http://127.0.0.1:9377"
    assert route.provider_id == "sub2api"
    assert route.source == "codex-provider"


def test_resolve_openai_proxy_route_prefers_explicit_env(monkeypatch):
    route = resolve_openai_proxy_route(
        port=9377,
        env={"ENTROLY_OPENAI_BASE": "https://example.openai.azure.com/openai"},
    )

    assert route.upstream_base_url == "https://example.openai.azure.com/openai"
    assert route.upstream_origin == "https://example.openai.azure.com"
    assert route.proxy_base_url == "http://127.0.0.1:9377/openai"
    assert route.provider_id is None
    assert route.source == "env"


def test_resolve_openai_proxy_route_accepts_non_responses_provider_for_generic_proxy(tmp_path: Path):
    codex_home = tmp_path / ".codex"
    codex_home.mkdir()
    (codex_home / "config.toml").write_text(
        """
model_provider = "sub2api"

[model_providers.sub2api]
name = "sub2api"
base_url = "https://api.mookbot.com/openai"
wire_api = "chat_completions"
""".strip(),
        encoding="utf-8",
    )

    route = resolve_openai_proxy_route(port=9377, env={"CODEX_HOME": str(codex_home)})

    assert route.upstream_base_url == "https://api.mookbot.com/openai"
    assert route.proxy_base_url == "http://127.0.0.1:9377/openai"
    assert route.provider_id == "sub2api"
    assert route.wire_api == "chat_completions"


def test_resolve_openai_proxy_route_defaults_to_openai_when_config_missing(tmp_path: Path):
    route = resolve_openai_proxy_route(
        port=9377,
        env={"CODEX_HOME": str(tmp_path / ".missing-codex")},
    )

    assert route.upstream_base_url == "https://api.openai.com/v1"
    assert route.upstream_origin == "https://api.openai.com"
    assert route.proxy_base_url == "http://127.0.0.1:9377/v1"
    assert route.provider_id == "openai"
    assert route.source == "default-openai"


def test_resolve_openai_proxy_route_rejects_invalid_env_base_url():
    with pytest.raises(ValueError, match="provider base_url"):
        resolve_openai_proxy_route(
            port=9377,
            env={"ENTROLY_OPENAI_BASE": "not-a-url"},
        )


def test_resolve_launch_cmd_resolves_bare_executable(monkeypatch):
    monkeypatch.setattr("entroly.launching.shutil.which", lambda name: r"C:\tools\codex.cmd")
    resolved = resolve_launch_cmd(["codex", "--version"])
    assert resolved == [r"C:\tools\codex.cmd", "--version"]


def test_resolve_python_cmd_prefers_real_python_sibling(tmp_path: Path):
    scripts_dir = tmp_path / "Scripts"
    scripts_dir.mkdir()
    launcher = scripts_dir / "entroly.exe"
    launcher.write_text("", encoding="utf-8")
    python = scripts_dir / "python.exe"
    python.write_text("", encoding="utf-8")

    resolved = resolve_python_cmd(str(launcher))

    assert resolved == str(python)


def test_ensure_loopback_no_proxy_merges_existing_entries():
    env = {"NO_PROXY": "example.com,internal.local"}

    _ensure_loopback_no_proxy(env)

    assert env["NO_PROXY"] == "example.com,internal.local,127.0.0.1,localhost,::1"
    assert env["no_proxy"] == env["NO_PROXY"]


def test_cmd_wrap_codex_passes_upstream_env_to_proxy(monkeypatch):
    popen_calls: list[dict] = []
    run_calls: list[dict] = []
    state = {"proxy_started": False}

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def settimeout(self, timeout):
            return None

        def connect_ex(self, address):
            return 0 if state["proxy_started"] else 1

    def fake_popen(cmd, **kwargs):
        popen_calls.append({"cmd": cmd, "kwargs": kwargs})
        state["proxy_started"] = True
        return SimpleNamespace()

    def fake_run(cmd, **kwargs):
        run_calls.append({"cmd": cmd, "kwargs": kwargs})
        return SimpleNamespace(returncode=0)

    plan = SimpleNamespace(
        env_updates={"ENTROLY_OPENAI_BASE": "https://api.mookbot.com"},
        override_args=[
            "--config",
            'model_providers.sub2api.base_url="http://127.0.0.1:9377"',
            "--config",
            "model_providers.sub2api.responses_websockets_v2=false",
            "--config",
            "model_providers.sub2api.supports_websockets=false",
            "--config",
            "features.responses_websockets_v2=false",
        ],
        provider=SimpleNamespace(
            provider_id="sub2api",
            config_path=Path(r"C:\Users\WenYu\.codex\config.toml"),
            base_url="https://api.mookbot.com/v1",
        ),
        proxy_base_url="http://127.0.0.1:9377",
    )

    monkeypatch.setattr("entroly.cli.prepare_codex_wrap", lambda *args, **kwargs: plan)
    monkeypatch.setattr("entroly.cli.resolve_python_cmd", lambda: r"D:\venv\Scripts\python.exe")
    monkeypatch.setattr("entroly.cli.resolve_launch_cmd", lambda cmd: cmd)
    monkeypatch.setattr("entroly.cli.subprocess.Popen", fake_popen)
    monkeypatch.setattr("entroly.cli.subprocess.run", fake_run)
    monkeypatch.setattr("socket.socket", lambda *args, **kwargs: FakeSocket())
    monkeypatch.setattr("entroly.cli.os.environ", {"PATH": r"C:\tools"})

    args = SimpleNamespace(
        agent="codex",
        port=9377,
        codex_provider_id=None,
        codex_base_url=None,
        agent_args=[],
    )

    cmd_wrap(args)

    assert popen_calls
    proxy_env = popen_calls[0]["kwargs"]["env"]
    assert proxy_env["ENTROLY_OPENAI_BASE"] == "https://api.mookbot.com"
    assert proxy_env["NO_PROXY"].endswith("127.0.0.1,localhost,::1")
    assert popen_calls[0]["cmd"][:4] == [r"D:\venv\Scripts\python.exe", "-m", "entroly.cli", "proxy"]
    assert popen_calls[0]["cmd"][-2:] == ["--port", "9377"]

    assert run_calls
    assert run_calls[0]["kwargs"]["env"]["NO_PROXY"].endswith("127.0.0.1,localhost,::1")
    assert run_calls[0]["cmd"] == [
        "codex",
        "--config",
        'model_providers.sub2api.base_url="http://127.0.0.1:9377"',
        "--config",
        "model_providers.sub2api.responses_websockets_v2=false",
        "--config",
        "model_providers.sub2api.supports_websockets=false",
        "--config",
        "features.responses_websockets_v2=false",
    ]


def test_cmd_wrap_aider_uses_dynamic_openai_proxy_base(monkeypatch):
    popen_calls: list[dict] = []
    run_calls: list[dict] = []
    state = {"proxy_started": False}

    class FakeSocket:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc, tb):
            return False

        def settimeout(self, timeout):
            return None

        def connect_ex(self, address):
            return 0 if state["proxy_started"] else 1

    def fake_popen(cmd, **kwargs):
        popen_calls.append({"cmd": cmd, "kwargs": kwargs})
        state["proxy_started"] = True
        return SimpleNamespace()

    def fake_run(cmd, **kwargs):
        run_calls.append({"cmd": cmd, "kwargs": kwargs})
        return SimpleNamespace(returncode=0)

    monkeypatch.setattr(
        "entroly.cli.resolve_openai_proxy_route",
        lambda **kwargs: SimpleNamespace(
            proxy_base_url="http://127.0.0.1:9377/openai/v1",
            upstream_base_url="https://example.openai.azure.com/openai/v1",
            source="env",
            provider_id=None,
        ),
    )
    monkeypatch.setattr("entroly.cli.resolve_python_cmd", lambda: r"D:\venv\Scripts\python.exe")
    monkeypatch.setattr("entroly.cli.resolve_launch_cmd", lambda cmd: cmd)
    monkeypatch.setattr("entroly.cli.subprocess.Popen", fake_popen)
    monkeypatch.setattr("entroly.cli.subprocess.run", fake_run)
    monkeypatch.setattr("socket.socket", lambda *args, **kwargs: FakeSocket())
    monkeypatch.setattr("entroly.cli.os.environ", {"PATH": r"C:\tools"})

    args = SimpleNamespace(
        agent="aider",
        port=9377,
        codex_provider_id=None,
        codex_base_url=None,
        agent_args=["--model", "gpt-5.4"],
    )

    cmd_wrap(args)

    assert popen_calls
    assert run_calls
    assert run_calls[0]["kwargs"]["env"]["OPENAI_API_BASE"] == "http://127.0.0.1:9377/openai/v1"
