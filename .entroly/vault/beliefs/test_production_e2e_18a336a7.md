---
claim_id: 18a336a731d6dab031ee70b0
entity: test_production_e2e
status: inferred
confidence: 0.75
sources:
  - tests\test_production_e2e.py:57
  - tests\test_production_e2e.py:69
  - tests\test_production_e2e.py:73
  - tests\test_production_e2e.py:390
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_production_e2e

**LOC:** 552

## Entities
- `def ok(label: str, cond: bool, detail: str = "") -> bool` (function)
- `def section(name: str)` (function)
- `def fresh(max_frags: int = 10_000) -> EntrolyEngine` (function)
- `def worker(thread_id: int)` (function)
