---
claim_id: 18a336a70c2bc2a80c4358a8
entity: value_tracker
status: stale
confidence: 0.75
sources:
  - entroly\value_tracker.py:64
  - entroly\value_tracker.py:98
  - entroly\value_tracker.py:110
  - entroly\value_tracker.py:255
  - entroly\value_tracker.py:260
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: value_tracker

**LOC:** 344

## Entities
- `def estimate_cost(tokens_saved: int, model: str = "") -> float` (function)
- `class ValueTracker:` (class)
- `def __init__(self, data_dir: Optional[Path] = None)` (function)
- `def get_lifetime(self) -> Dict[str, Any]` (function)
- `def get_daily(self, last_n: int = 30) -> List[Dict[str, Any]]` (function)
- `def get_weekly(self, last_n: int = 12) -> List[Dict[str, Any]]` (function)
- `def get_monthly(self, last_n: int = 12) -> List[Dict[str, Any]]` (function)
- `def get_session(self) -> Dict[str, Any]` (function)
- `def get_confidence(self) -> Dict[str, Any]` (function)
- `def get_trends(self) -> Dict[str, Any]` (function)
- `def get_tracker() -> ValueTracker` (function)
