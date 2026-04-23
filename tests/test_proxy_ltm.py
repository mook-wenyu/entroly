import sys
from pathlib import Path


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
