---
claim_id: 8cfa0583-1387-465d-ae6d-34f6408c88f1
entity: benchmark_harness
status: inferred
confidence: 0.75
sources:
  - entroly/benchmark_harness.py:43
  - entroly/benchmark_harness.py:26
  - entroly/benchmark_harness.py:39
  - entroly/benchmark_harness.py:40
last_checked: 2026-04-14T04:12:29.407585+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: benchmark_harness

**Language:** python
**Lines of code:** 120


## Functions
- `def run_benchmark(engine: Any, budget_seconds: float = 10.0) -> dict[str, Any]` — Run the fixed evaluation payload and return the context_efficiency score. READ ONLY — this function is the ground truth metric. autotune.py calls this but never modifies it. The engine and benchmark c

## Dependencies
- `__future__`
- `gc`
- `time`
- `typing`
