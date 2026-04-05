---
claim_id: 18a336a7080df79008258d90
entity: evaluate
status: inferred
confidence: 0.75
sources:
  - bench\evaluate.py:35
  - bench\evaluate.py:42
  - bench\evaluate.py:101
  - bench\evaluate.py:117
  - bench\evaluate.py:148
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: evaluate

**LOC:** 305

## Entities
- `def load_cases(path: Path | None = None) -> list[dict]` (function)
- `def validate_tuning_config(config: dict) -> list[str]` (function)
- `def load_tuning_config(path: Path | None = None) -> dict` (function)
- `def create_engine_from_config(config: dict)` (function)
- `def run_case(engine_factory, case: dict) -> dict[str, Any]` (function)
- `def evaluate(config: dict | None = None, cases_path: Path | None = None) -> dict` (function)
- `def main()` (function)
