---
claim_id: 18a336a730f938683110ce68
entity: test_apa
status: inferred
confidence: 0.75
sources:
  - tests\test_apa.py:26
  - tests\test_apa.py:29
  - tests\test_apa.py:32
  - tests\test_apa.py:41
  - tests\test_apa.py:49
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_apa

**LOC:** 310

## Entities
- `class TestCalibratedTokenCount:` (class)
- `def test_empty_content_returns_zero(self)` (function)
- `def test_python_denser_than_default(self)` (function)
- `def test_rust_less_dense_than_python(self)` (function)
- `def test_json_densest(self)` (function)
- `def test_unknown_extension_uses_default(self)` (function)
- `def test_never_returns_zero_for_nonempty(self)` (function)
- `def test_no_source_uses_default(self)` (function)
- `def test_all_languages_return_positive(self, ext, lang)` (function)
- `class TestBuildPreamble:` (class)
- `def test_no_signals_returns_empty(self)` (function)
- `def test_security_issues_trigger_warning(self)` (function)
- `def test_single_security_issue_singular(self)` (function)
- `def test_high_vagueness_triggers_clarification(self)` (function)
- `def test_low_vagueness_no_clarification(self)` (function)
- `def test_bugtracing_hint(self)` (function)
- `def test_refactoring_hint(self)` (function)
- `def test_testing_hint(self)` (function)
- `def test_codereview_hint(self)` (function)
- `def test_codegeneration_no_hint(self)` (function)
- `def test_combined_signals(self)` (function)
- `class TestDeduplicateFragments:` (class)
- `def test_no_duplicates_keeps_all(self)` (function)
- `def test_exact_duplicates_removed(self)` (function)
- `def test_keeps_first_occurrence(self)` (function)
- `def test_near_duplicates_kept(self)` (function)
- `def test_empty_list(self)` (function)
- `def test_uses_preview_field(self)` (function)
- `class TestFormatContextBlockAPA:` (class)
- `def test_preamble_appears_for_bugtracing(self)` (function)
- `def test_no_preamble_for_unknown_low_vagueness(self)` (function)
- `def test_security_preamble_with_issues(self)` (function)
- `def test_dedup_removes_duplicate_fragments(self)` (function)
- `def test_backward_compatible_without_kwargs(self)` (function)
- `def test_vagueness_threshold(self)` (function)
- `def test_empty_fragments_and_memories_returns_empty(self)` (function)
- `def test_preamble_before_fragments(self)` (function)
- `class TestTokenBudgetAccuracy:` (class)
- `def test_reasonable_estimates(self, code, source, expected_range)` (function)
