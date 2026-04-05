---
claim_id: 18a336a732031df0321ab3f0
entity: test_real_user
status: inferred
confidence: 0.75
sources:
  - tests\test_real_user.py:44
  - tests\test_real_user.py:54
  - tests\test_real_user.py:60
  - tests\test_real_user.py:72
  - tests\test_real_user.py:88
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_real_user

**LOC:** 417

## Entities
- `def check(label: str, condition: bool, detail: str = "")` (function)
- `def invariant(name: str)` (function)
- `def collect_sources() -> list[tuple[str, Path]]` (function)
- `def ingest_all(engine, sources) -> dict[str, str]` (function)
- `def scores_from_explain(engine) -> dict[str, float]` (function)
- `def run()` (function)
- `def top_scores(opt_result: dict) -> dict` (function)
