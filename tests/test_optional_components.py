from __future__ import annotations

import logging
from types import SimpleNamespace

from entroly import adaptive_pruner
from entroly.cli import cmd_doctor


def test_optional_component_loader_falls_back_to_ebbiforge_core(monkeypatch):
    class FakePruner:
        pass

    modules = {
        "entroly_core": SimpleNamespace(),
        "ebbiforge_core": SimpleNamespace(AdaptivePruner=FakePruner),
    }

    monkeypatch.setattr(adaptive_pruner.importlib, "import_module", lambda name: modules[name])

    cls, error = adaptive_pruner._load_optional_class("AdaptivePruner")

    assert cls is FakePruner
    assert error is None


def test_adaptive_pruner_missing_ebbiforge_core_is_not_info_noise(monkeypatch, caplog):
    monkeypatch.setattr(adaptive_pruner, "_PRUNER_AVAILABLE", False)
    monkeypatch.setattr(adaptive_pruner, "_RUST_PRUNER_AVAILABLE", False)
    monkeypatch.setattr(adaptive_pruner, "_PRUNER_IMPORT_ERROR", "No module named 'ebbiforge_core'")
    monkeypatch.setattr(adaptive_pruner, "_RustPruner", None)

    with caplog.at_level(logging.INFO):
        pruner = adaptive_pruner.EntrolyPruner()

    assert pruner.available is True
    assert pruner.backend == "python"
    assert "AdaptivePruner: ebbiforge_core not available" not in caplog.text
    assert "Python fallback active" in caplog.text


def test_doctor_reports_optional_learning_component_status(monkeypatch, capsys):
    monkeypatch.setattr(
        adaptive_pruner,
        "get_optional_component_status",
        lambda: {
            "adaptive_pruner": SimpleNamespace(
                name="AdaptivePruner",
                available=False,
                detail="No module named 'ebbiforge_core'",
            ),
            "fragment_guard": SimpleNamespace(
                name="FragmentGuard",
                available=False,
                detail="No module named 'ebbiforge_core'",
            ),
        },
    )
    monkeypatch.setattr("urllib.request.urlopen", lambda *args, **kwargs: (_ for _ in ()).throw(OSError()))
    monkeypatch.setattr("subprocess.run", lambda *args, **kwargs: SimpleNamespace(returncode=1))

    cmd_doctor(SimpleNamespace(port=65535))

    output = capsys.readouterr().out
    assert "Optional learning components unavailable" in output
    assert "AdaptivePruner" in output
    assert "FragmentGuard" in output
    assert "RL 权重学习与片段质量扫描已停用" in output
