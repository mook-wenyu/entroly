import sys
from pathlib import Path


REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))


from entroly.server import EntrolyEngine  # noqa: E402


def test_engine_always_exposes_ltm_attribute():
    engine = EntrolyEngine()
    assert hasattr(engine, "_ltm")
    assert hasattr(engine._ltm, "active")


def test_engine_ltm_active_is_bool():
    engine = EntrolyEngine()
    assert isinstance(engine._ltm.active, bool)
