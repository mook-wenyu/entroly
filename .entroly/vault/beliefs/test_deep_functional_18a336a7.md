---
claim_id: 18a336a731233dd4313ad3d4
entity: test_deep_functional
status: inferred
confidence: 0.75
sources:
  - tests\test_deep_functional.py:64
  - tests\test_deep_functional.py:77
  - tests\test_deep_functional.py:83
  - tests\test_deep_functional.py:91
  - tests\test_deep_functional.py:96
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_deep_functional

**LOC:** 850

## Entities
- `def check(label: str, condition: bool, detail: str = "") -> bool` (function)
- `def skip_check(label: str, reason: str = "")` (function)
- `def section(name: str)` (function)
- `def get_selected(opt: dict) -> list[dict]` (function)
- `def get_total_tokens(opt: dict) -> int` (function)
- `def get_effective_budget(opt: dict, fallback: int = 0) -> int` (function)
- `def get_total_fragments(stats: dict) -> int` (function)
- `def get_current_turn(stats: dict) -> int` (function)
- `def real_sources() -> list[tuple[str, Path]]` (function)
- `def fresh_engine(tmp_dir: str | None = None, **cfg_kwargs)` (function)
- `def ingest_corpus(engine, sources=None, pinned_names=()) -> dict[str, str]` (function)
- `def test_unicode_binary()` (function)
- `def test_massive_fragment()` (function)
- `def test_rapid_fire_ingest()` (function)
- `def test_dedup_near_miss()` (function)
- `def test_dedup_reorder()` (function)
- `def test_feedback_saturation()` (function)
- `def test_feedback_nonexistent()` (function)
- `def test_optimize_after_eviction()` (function)
- `def test_interleaved()` (function)
- `def test_special_char_queries()` (function)
- `def test_pin_everything()` (function)
- `def test_concurrent_like()` (function)
- `def test_checkpoint_fidelity()` (function)
- `def test_checkpoint_then_ingest()` (function)
- `def test_corrupted_checkpoint()` (function)
- `def test_zero_token_fragments()` (function)
- `def test_same_source_diff_content()` (function)
- `def test_recall_topk_boundary()` (function)
- `def test_budget_equals_corpus()` (function)
- `def test_extreme_aging()` (function)
- `def test_multi_engine_isolation()` (function)
- `def test_empty_whitespace()` (function)
- `def test_self_similar_corpus()` (function)
- `def test_query_refinement()` (function)
- `def test_prefetch_coacccess()` (function)
- `def test_prefetch_imports()` (function)
- `def process(data)` (function)
- `def test_stats_consistency()` (function)
- `def test_wilson_score_math()` (function)
- `def test_ebbinghaus_decay_math()` (function)
- `def test_knapsack_dp()` (function)
- `def test_entropy_scoring()` (function)
- `def compute_gradient_descent(weights, learning_rate, loss_fn)` (function)
- `def test_full_lifecycle_stress()` (function)
- `def run()` (function)
