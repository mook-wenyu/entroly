---
claim_id: 18a336a731a1345031b8ca50
entity: test_ios
status: inferred
confidence: 0.75
sources:
  - tests\test_ios.py:42
  - tests\test_ios.py:55
  - tests\test_ios.py:65
  - tests\test_ios.py:68
  - tests\test_ios.py:86
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_ios

**LOC:** 804

## Entities
- `def make_engine(**kwargs)` (function)
- `def ingest_fragment(engine, content, source="test.py", token_count=0, is_pinned=False)` (function)
- `class TestSDSDiversityPenalty:` (class)
- `def test_diverse_selection_over_redundant(self)` (function)
- `def test_diversity_score_reported(self)` (function)
- `def test_similar_fragments_low_diversity(self)` (function)
- `def test_all_unique_content_high_diversity(self)` (function)
- `class TestSDSBudgetRespect:` (class)
- `def test_budget_never_exceeded(self, budget)` (function)
- `def test_zero_budget(self)` (function)
- `class TestSDSFeedbackIntegration:` (class)
- `def test_boosted_fragment_preferred(self)` (function)
- `class TestMRKResolutionSelection:` (class)
- `def test_full_resolution_with_generous_budget(self)` (function)
- `def test_skeleton_resolution_with_tight_budget(self)` (function)
- `def test_reference_resolution_exists(self)` (function)
- `def test_mrk_disabled_uses_full_only(self)` (function)
- `class TestMRKCoverageImprovement:` (class)
- `def test_more_files_covered_with_mrk(self)` (function)
- `class TestECDBQueryFactor:` (class)
- `def test_specific_query_small_budget(self)` (function)
- `def test_vague_query_large_budget(self)` (function)
- `def test_medium_vagueness_near_static(self)` (function)
- `def test_budget_monotonic_in_vagueness(self, vagueness)` (function)
- `class TestECDBCodebaseFactor:` (class)
- `def test_larger_codebase_larger_budget(self)` (function)
- `def test_codebase_factor_caps_at_2x(self)` (function)
- `class TestECDBBounds:` (class)
- `def test_minimum_budget(self)` (function)
- `def test_maximum_budget(self)` (function)
- `def test_model_aware_budget(self, model, window)` (function)
- `class TestContextBlockFormatting:` (class)
- `def test_full_fragments_in_code_fences(self)` (function)
- `def test_skeleton_fragments_grouped(self)` (function)
- `def test_reference_fragments_listed(self)` (function)
- `def test_empty_fragments_returns_empty(self)` (function)
- `def test_resolution_ordering(self)` (function)
- `class TestIOSEndToEnd:` (class)
- `def test_pipeline_produces_valid_output(self)` (function)
- `def test_ios_vs_legacy_both_valid(self)` (function)
- `def test_ios_enabled_flag_in_result(self)` (function)
- `def test_ios_disabled_no_flag(self)` (function)
- `class TestIOSPerformance:` (class)
- `def test_1000_fragments_under_100ms(self)` (function)
- `class TestMathProperties:` (class)
- `def test_diversity_factor_bounds(self)` (function)
- `def test_ecdb_sigmoid_shape(self)` (function)
- `def test_ecdb_query_factor_formula(self)` (function)
- `class TestEdgeCases:` (class)
- `def test_single_fragment(self)` (function)
- `def test_all_pinned(self)` (function)
- `def test_budget_smaller_than_smallest(self)` (function)
- `def test_empty_query(self)` (function)
- `def test_unicode_content(self)` (function)
- `class TestIOSRegressionFixes:` (class)
- `def test_negative_feedback_does_not_backfill_bad_reference(self)` (function)
- `def test_ios_exploration_can_vary_selected_set(self)` (function)
- `def test_exploration_does_not_seed_exploit_cache(self)` (function)
- `def test_explain_selection_includes_compressed_variants(self)` (function)
