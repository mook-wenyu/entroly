---
claim_id: 18a336a70f76813c0f8e173c
entity: test_integration
status: stale
confidence: 0.75
sources:
  - entroly-core\tests\test_integration.py:15
  - entroly-core\tests\test_integration.py:34
  - entroly-core\tests\test_integration.py:40
  - entroly-core\tests\test_integration.py:49
  - entroly-core\tests\test_integration.py:59
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_integration

**LOC:** 814

## Entities
- `def test(name, fn)` (function)
- `def test_default_constructor()` (function)
- `def test_custom_params()` (function)
- `def test_exploration_rate_clamp()` (function)
- `def test_basic_ingest()` (function)
- `def test_ingest_with_explicit_tokens()` (function)
- `def test_token_estimation_code_vs_prose()` (function)
- `def test_pinned_ingest()` (function)
- `def test_empty_content()` (function)
- `def test_large_content()` (function)
- `def test_multiple_ingests()` (function)
- `def test_criticality(path, expected_crit)` (function)
- `def test_license_safety()` (function)
- `def test_security_warning_safety()` (function)
- `def test_normal_code_not_pinned()` (function)
- `def test_entropy_honest_for_critical()` (function)
- `def test_entropy_varies_with_content()` (function)
- `def test_exact_duplicate()` (function)
- `def test_different_content_not_duplicate()` (function)
- `def test_near_duplicate()` (function)
- `def test_dep_graph_auto_link()` (function)
- `def test_dep_graph_import_detection()` (function)
- `def test_dep_graph_order_matters()` (function)
- `def test_dep_graph_empty()` (function)
- `def test_bug_tracing()` (function)
- `def test_refactoring()` (function)
- `def test_code_generation()` (function)
- `def test_testing()` (function)
- `def test_unknown_task()` (function)
- `def test_optimize_empty()` (function)
- `def test_optimize_selects_within_budget()` (function)
- `def test_optimize_adaptive_budget()` (function)
- `def test_optimize_pinned_always_included()` (function)
- `def test_optimize_sufficiency()` (function)
- `def test_optimize_returns_ordered()` (function)
- `def test_feedback_success()` (function)
- `def test_feedback_failure()` (function)
- `def test_feedback_affects_ranking()` (function)
- `def test_feedback_empty_ids()` (function)
- `def test_feedback_nonexistent_id()` (function)
- `def test_explain_before_optimize()` (function)
- `def test_explain_after_optimize()` (function)
- `def test_recall_empty()` (function)
- `def test_recall_returns_ranked()` (function)
- `def test_advance_turn()` (function)
- `def test_decay_evicts_stale()` (function)
- `def test_pinned_survives_decay()` (function)
- `def test_critical_file_survives_decay()` (function)
- `def test_export_import_roundtrip()` (function)
- `def test_import_invalid_json()` (function)
- `def test_stats_structure()` (function)
- `def test_shannon_entropy()` (function)
- `def test_simhash()` (function)
- `def test_hamming_distance()` (function)
- `def test_normalized_entropy()` (function)
- `def test_boilerplate_ratio()` (function)
- `def test_unicode_content()` (function)
- `def test_binary_like_content()` (function)
- `def test_very_long_source_path()` (function)
- `def test_optimize_zero_budget()` (function)
- `def test_recall_zero_k()` (function)
- `class DataPipeline:` (class)
- `def __init__(self, config: dict)` (function)
- `def ingest_event(self, event: dict) -> bool` (function)
- `def flush(self) -> int` (function)
- `def test_skeleton_populated_on_ingest_python()` (function)
- `def test_skeleton_token_count_less_than_full()` (function)
- `def test_no_skeleton_for_non_code()` (function)
- `def test_skeleton_present_for_js()` (function)
- `def test_optimize_uses_skeleton_when_budget_tight()` (function)
- `def test_optimize_prefers_full_when_budget_allows()` (function)
- `def test_optimize_variant_field_always_present()` (function)
