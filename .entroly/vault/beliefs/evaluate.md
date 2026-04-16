---
claim_id: def2879a-cfc9-4ade-85f2-353dd2f2ea56
entity: evaluate
status: inferred
confidence: 0.75
sources:
  - bench/evaluate.py:35
  - bench/evaluate.py:42
  - bench/evaluate.py:101
  - bench/evaluate.py:117
  - bench/evaluate.py:148
  - bench/evaluate.py:223
  - bench/evaluate.py:264
  - bench/evaluate.py:32
last_checked: 2026-04-14T04:12:29.387907+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: evaluate

**Language:** python
**Lines of code:** 306


## Functions
- `def load_cases(path: Path | None = None) -> list[dict]`
- `def validate_tuning_config(config: dict) -> list[str]` — Validate tuning_config.json schema and value ranges. Returns a list of error strings. Empty list means valid.
- `def load_tuning_config(path: Path | None = None) -> dict`
- `def create_engine_from_config(config: dict)` — Create an EntrolyEngine using the tuning config weights.
- `def run_case(engine_factory, case: dict) -> dict[str, Any]` — Run a single benchmark case. Returns metrics dict.
- `def evaluate(config: dict | None = None, cases_path: Path | None = None) -> dict` — Run the full benchmark suite. Returns aggregate metrics.
- `def main()`

## Dependencies
- `__future__`
- `json`
- `pathlib`
- `sys`
- `time`
- `typing`
