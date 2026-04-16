---
claim_id: 0307acb0-b6ab-49ca-9188-bc6f41f95c03
entity: accuracy
status: inferred
confidence: 0.75
sources:
  - bench/accuracy.py:51
  - bench/accuracy.py:66
  - bench/accuracy.py:243
  - bench/accuracy.py:445
  - bench/accuracy.py:560
last_checked: 2026-04-14T04:12:29.381677+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: accuracy

**Language:** python
**Lines of code:** 655

## Types
- `class BenchmarkResult()` — Result of a single benchmark run.
- `class RetentionReport()` — Accuracy retention: Entroly vs baseline.

## Functions
- `def bench_needle(model: str, samples: int = 20) -> list[dict]` — NeedleInAHaystack: can the LLM find a fact in compressed context?
- `def run_benchmark(
    benchmark: str,
    model: str = "gpt-4o-mini",
    samples: int = 50,
    budget: int = 50_000,
) -> RetentionReport`
- `def main()`

## Dependencies
- `__future__`
- `dataclasses`
- `json`
- `os`
- `pathlib`
- `random`
- `re`
- `sys`
- `time`
- `typing`
