import sys
from pathlib import Path
from types import SimpleNamespace


REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))


from entroly.proxy import PromptCompilerProxy  # noqa: E402
from entroly.proxy_config import ProxyConfig  # noqa: E402
from entroly.server import EntrolyEngine  # noqa: E402


def test_proxy_can_read_ltm_state():
    engine = EntrolyEngine()
    proxy = PromptCompilerProxy(engine, ProxyConfig())
    assert hasattr(proxy.engine, "_ltm")
    assert hasattr(proxy.engine._ltm, "active")


def test_proxy_initializes_tokens_saved_header_state():
    engine = EntrolyEngine()
    proxy = PromptCompilerProxy(engine, ProxyConfig())
    assert proxy._last_tokens_saved_pct == 0.0


def test_proxy_allows_disabled_ltm_attribute():
    engine = EntrolyEngine()
    engine._ltm = None
    proxy = PromptCompilerProxy(engine, ProxyConfig(enable_ltm=True, enable_hierarchical_compression=False))

    proxy._run_pipeline("hello", {"model": "gpt-4o"})


def test_proxy_uses_adaptive_budget_when_confident():
    class EngineStub:
        def __init__(self):
            self._turn_counter = 0
            self._ltm = SimpleNamespace(active=False)
            self.seen_budget = None

        def set_model(self, model):
            self.model = model

        def advance_turn(self):
            pass

        def optimize_context(self, token_budget, query):
            self.seen_budget = token_budget
            return {
                "selected_fragments": [],
                "query_analysis": {},
            }

    engine = EngineStub()
    config = ProxyConfig(enable_dynamic_budget=False, enable_hierarchical_compression=False)
    proxy = PromptCompilerProxy(engine, config)
    proxy._acb = SimpleNamespace(
        predict=lambda features: {
            "fallback": None,
            "budget_used": 0.25,
            "budget_se": 0.01,
            "n_training": 25,
        }
    )

    proxy._run_pipeline("fix login bug", {"model": "gpt-4o"})

    assert engine.seen_budget == 32_000
