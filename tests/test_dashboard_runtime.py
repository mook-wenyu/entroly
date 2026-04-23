from __future__ import annotations

import sys
import threading
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
