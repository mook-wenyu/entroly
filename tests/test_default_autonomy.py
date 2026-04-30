from __future__ import annotations

from types import SimpleNamespace

from entroly.cli import _select_runtime_quality
from entroly.federation import FederationClient
from entroly.proxy import PromptCompilerProxy
from entroly.proxy_config import ProxyConfig, QUALITY_PRESETS


def test_proxy_config_from_env_defaults_to_max_quality(monkeypatch):
    monkeypatch.delenv("ENTROLY_QUALITY", raising=False)
    monkeypatch.delenv("ENTROLY_CONTEXT_FRACTION", raising=False)

    config = ProxyConfig.from_env()

    assert config.quality == QUALITY_PRESETS["max"]
    assert config.context_fraction == 0.25
    assert config.enable_ltm is True
    assert config.enable_hierarchical_compression is True
    assert config.enable_trajectory_convergence is True


def test_proxy_config_from_env_respects_named_quality_override(monkeypatch):
    monkeypatch.setenv("ENTROLY_QUALITY", "balanced")

    config = ProxyConfig.from_env()

    assert config.quality == QUALITY_PRESETS["balanced"]
    assert config.context_fraction == 0.165


def test_cli_runtime_quality_defaults_to_max_and_preserves_explicit_overrides():
    label, value, source = _select_runtime_quality(None, env={})
    assert (label, value, source) == ("max", QUALITY_PRESETS["max"], "default")

    label, value, source = _select_runtime_quality(None, env={"ENTROLY_QUALITY": "quality"})
    assert (label, value, source) == ("quality", QUALITY_PRESETS["quality"], "env")

    label, value, source = _select_runtime_quality("fast", env={"ENTROLY_QUALITY": "quality"})
    assert (label, value, source) == ("fast", QUALITY_PRESETS["fast"], "cli")


def test_response_distillation_defaults_to_ultra(monkeypatch):
    monkeypatch.delenv("ENTROLY_DISTILL", raising=False)
    monkeypatch.delenv("ENTROLY_DISTILL_MODE", raising=False)

    proxy = PromptCompilerProxy(engine=SimpleNamespace(), config=ProxyConfig())

    assert proxy._enable_distill is True
    assert proxy._distill_mode == "ultra"


def test_federation_client_defaults_enabled_and_can_be_disabled(monkeypatch, tmp_path):
    monkeypatch.delenv("ENTROLY_FEDERATION", raising=False)
    default_client = FederationClient(data_dir=tmp_path / "default")
    assert default_client.enabled is True

    monkeypatch.setenv("ENTROLY_FEDERATION", "0")
    disabled_client = FederationClient(data_dir=tmp_path / "disabled")
    assert disabled_client.enabled is False


def test_runtime_learning_services_start_evolution_daemon_with_feedback_journal(monkeypatch, tmp_path):
    import entroly.server as server

    events: dict[str, object] = {}

    class FakeFeedbackJournal:
        def __init__(self, checkpoint_dir):
            self.checkpoint_dir = checkpoint_dir

        def log(self, **kwargs):
            events["journal_log"] = kwargs

    class FakeEvolutionLogger:
        def __init__(self, vault_path, gap_threshold):
            events["evolution_logger"] = (vault_path, gap_threshold)

    class FakeEvolutionDaemon:
        def __init__(self, **kwargs):
            events["daemon_kwargs"] = kwargs
            self.started = False

        def start(self):
            self.started = True
            events["daemon_started"] = True

    class FakeEngine:
        _use_rust = False
        _rust = None

        def set_journal_callback(self, callback):
            events["journal_callback"] = callback

    monkeypatch.setattr(server, "FeedbackJournal", FakeFeedbackJournal)
    monkeypatch.setattr(server, "EvolutionLogger", FakeEvolutionLogger)
    monkeypatch.setattr(server, "EvolutionDaemon", FakeEvolutionDaemon)
    monkeypatch.setattr(server, "get_tracker", lambda: "tracker")

    engine = FakeEngine()
    services = server.start_runtime_learning_services(
        engine,
        project_root=tmp_path,
        checkpoint_dir=tmp_path / ".entroly",
        vault_path=tmp_path / ".entroly" / "vault",
    )

    assert events["daemon_started"] is True
    assert events["daemon_kwargs"]["feedback_journal"] is services.feedback_journal
    assert events["daemon_kwargs"]["value_tracker"] == "tracker"
    assert events["journal_callback"] == services.feedback_journal.log
    assert getattr(engine, "_runtime_learning_services") is services
