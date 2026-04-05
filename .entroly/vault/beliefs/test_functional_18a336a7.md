---
claim_id: 18a336a73179f82c31918e2c
entity: test_functional
status: inferred
confidence: 0.75
sources:
  - tests\test_functional.py:50
  - tests\test_functional.py:63
  - tests\test_functional.py:69
  - tests\test_functional.py:81
  - tests\test_functional.py:86
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_functional

**LOC:** 823

## Entities
- `def check(label: str, condition: bool, detail: str = "") -> bool` (function)
- `def skip(label: str, reason: str = "")` (function)
- `def section(name: str)` (function)
- `def opt_selected(opt: dict) -> list[dict]` (function)
- `def opt_total_tokens(opt: dict) -> int` (function)
- `def opt_effective_budget(opt: dict, fallback: int) -> int` (function)
- `def real_sources() -> list[tuple[str, Path]]` (function)
- `def fresh_engine(tmp_dir: str | None = None, **cfg_kwargs)` (function)
- `def ingest_corpus(engine, sources, pinned_names=()) -> dict[str, str]` (function)
- `def test_cold_start()` (function)
- `def test_single_file()` (function)
- `def test_ingest_contract()` (function)
- `def test_dedup_boundary()` (function)
- `def test_feedback_loop()` (function)
- `def score_of(fid: str) -> float | None` (function)
- `def test_multi_turn_lifecycle()` (function)
- `def test_query_sensitivity()` (function)
- `def test_score_stability()` (function)
- `def test_advance_turn()` (function)
- `def get_turn()` (function)
- `def test_stats_contract()` (function)
- `def test_explain_selection()` (function)
- `def test_checkpoint_crash_sim()` (function)
- `def test_large_budget()` (function)
- `def test_tiny_budget()` (function)
- `def test_recall_vs_optimize_universe()` (function)
- `def test_mixed_feedback()` (function)
- `def test_prefetch_prediction()` (function)
- `def test_zero_query()` (function)
- `def run()` (function)
