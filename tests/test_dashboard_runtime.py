from __future__ import annotations

import sys
import threading
import builtins
from pathlib import Path
from types import SimpleNamespace

import pytest

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

import entroly.dashboard as dashboard  # noqa: E402
from entroly.server import EntrolyEngine  # noqa: E402


@pytest.fixture(autouse=True)
def reset_dashboard_state():
    dashboard._engine = None
    dashboard._proxy = None
    dashboard._seed_optimization = None
    dashboard.clear_request_log()
    yield
    dashboard._engine = None
    dashboard._proxy = None
    dashboard._seed_optimization = None
    dashboard.clear_request_log()


def _write_belief(path: Path, entity: str, status: str = "inferred", confidence: float = 0.8) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\nentity: {entity}\nstatus: {status}\nconfidence: {confidence}\n---\n\n# {entity}\n",
        encoding="utf-8",
    )


def test_dashboard_snapshot_reads_project_vault_without_engine(monkeypatch, tmp_path):
    monkeypatch.delenv("ENTROLY_VAULT", raising=False)
    monkeypatch.delenv("ENTROLY_DIR", raising=False)
    monkeypatch.delenv("ENTROLY_SOURCE", raising=False)
    monkeypatch.chdir(tmp_path)
    _write_belief(tmp_path / ".entroly" / "vault" / "beliefs" / "runtime.md", "runtime", "verified", 0.9)

    snapshot = dashboard._get_full_snapshot()

    assert snapshot["engine_available"] is False
    assert snapshot["cogops"]["total_beliefs"] == 1
    assert snapshot["cogops"]["verified"] == 1
    assert snapshot["capabilities"]["cogops"]["status"] == "available"


def test_dashboard_snapshot_marks_empty_cogops_as_degraded(monkeypatch, tmp_path):
    monkeypatch.delenv("ENTROLY_VAULT", raising=False)
    monkeypatch.delenv("ENTROLY_DIR", raising=False)
    monkeypatch.setenv("ENTROLY_SOURCE", str(tmp_path))
    (tmp_path / ".entroly" / "vault" / "beliefs").mkdir(parents=True)

    snapshot = dashboard._get_full_snapshot()

    assert snapshot["cogops"]["status"] == "unseeded"
    assert snapshot["cogops"]["total_beliefs"] == 0
    assert snapshot["capabilities"]["cogops"]["status"] == "degraded"
    assert str(tmp_path) in snapshot["capabilities"]["cogops"]["reason"]


def test_dashboard_snapshot_marks_missing_native_cogops_as_degraded(monkeypatch, tmp_path):
    monkeypatch.delenv("ENTROLY_VAULT", raising=False)
    monkeypatch.delenv("ENTROLY_DIR", raising=False)
    monkeypatch.setenv("ENTROLY_SOURCE", str(tmp_path))
    _write_belief(tmp_path / ".entroly" / "vault" / "beliefs" / "runtime.md", "runtime", "verified", 0.9)

    real_import = builtins.__import__

    def import_without_native(name, *args, **kwargs):
        if name == "entroly_core":
            raise ImportError("missing native extension")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", import_without_native)

    snapshot = dashboard._get_full_snapshot()

    assert snapshot["cogops"]["engine"] == "unavailable"
    assert "missing native extension" in snapshot["cogops"]["engine_error"]
    assert snapshot["capabilities"]["cogops"]["status"] == "degraded"


def test_dashboard_snapshot_uses_proxy_last_optimization():
    dashboard._proxy = SimpleNamespace(
        _stats_lock=threading.Lock(),
        _has_successful_optimization=True,
        _last_original_prompt_tokens=1200,
        _last_optimized_prompt_tokens=320,
        _last_tokens_saved_pct=73.33,
        _last_fragment_count=14,
        _last_coverage_pct=68.2,
        _last_confidence=0.81,
        _last_pipeline_ms=5.7,
        _last_query="fix failing auth test",
        _last_optimization_at=123.0,
    )

    snapshot = dashboard._get_full_snapshot()
    last = snapshot["last_optimization"]
    assert last["available"] is True
    assert last["source"] == "proxy"
    assert last["original_tokens"] == 1200
    assert last["optimized_tokens"] == 320
    assert last["fragment_count"] == 14
    assert last["coverage_pct"] == 68.2
    assert last["query"] == "fix failing auth test"


def test_dashboard_snapshot_falls_back_to_seed_optimization():
    dashboard._seed_optimization = {
        "available": True,
        "source": "engine",
        "original_tokens": 5000,
        "optimized_tokens": 800,
        "fragment_count": 32,
        "coverage_pct": 44.4,
        "query": "project overview",
    }

    snapshot = dashboard._get_full_snapshot()
    last = snapshot["last_optimization"]
    assert last["available"] is True
    assert last["source"] == "engine"
    assert last["optimized_tokens"] == 800
    assert last["fragment_count"] == 32


def test_explain_selection_includes_token_count_with_rust_engine():
    engine = EntrolyEngine()
    if not getattr(engine, "_use_rust", False):
        pytest.skip("requires Rust engine")

    engine.ingest_fragment("def calculate_tax(amount):\n    return amount * 0.2\n", source="file:tax.py", token_count=20)
    engine.ingest_fragment("total = calculate_tax(100)\n", source="file:main.py", token_count=8)

    engine.optimize_context(token_budget=128, query="calculate_tax")
    explain = engine.explain_selection()

    assert "included" in explain
    assert len(explain["included"]) > 0
    assert "token_count" in explain["included"][0]
    assert explain["included"][0]["token_count"] > 0
