---
claim_id: 18a336a7318db1c831a547c8
entity: test_intensive_functional
status: inferred
confidence: 0.75
sources:
  - tests\test_intensive_functional.py:52
  - tests\test_intensive_functional.py:64
  - tests\test_intensive_functional.py:70
  - tests\test_intensive_functional.py:78
  - tests\test_intensive_functional.py:87
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_intensive_functional

**LOC:** 825

## Entities
- `def check(label: str, condition: bool, detail: str = "") -> bool` (function)
- `def skip(label: str, reason: str = "")` (function)
- `def section(code: str, title: str)` (function)
- `def real_sources() -> list[tuple[str, Path]]` (function)
- `def fresh_engine(tmp=None, **cfg_overrides)` (function)
- `def load_all(engine, sources, pinned=())` (function)
- `def test_token_count_accuracy()` (function)
- `def test_feedback_idempotency()` (function)
- `def test_relevance_ordering()` (function)
- `def test_checkpoint_file_format()` (function)
- `def test_resume_full_state()` (function)
- `def test_multi_checkpoint_cycle()` (function)
- `def test_budget_utilization_math()` (function)
- `def test_sufficiency_contract()` (function)
- `def test_provenance_chain()` (function)
- `def test_entropy_signal()` (function)
- `def test_advance_turn_decay()` (function)
- `def recency_score()` (function)
- `def test_stats_after_eviction()` (function)
- `def frag_count()` (function)
- `def test_record_success_monotone()` (function)
- `def test_dedup_tokens_saved()` (function)
- `def test_optimize_fields_contract()` (function)
- `def test_recall_top_k_exact()` (function)
- `def test_recall_scores_ordered()` (function)
- `def test_stats_after_feedback()` (function)
- `def test_config_propagates()` (function)
- `def test_empty_record_success()` (function)
- `def test_unknown_fragment_id()` (function)
- `def test_large_corpus_performance()` (function)
- `def run()` (function)
