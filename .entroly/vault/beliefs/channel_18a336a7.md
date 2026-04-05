---
claim_id: 18a336a72a8622ac2a9db8ac
entity: channel
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\channel.rs:41
  - entroly-wasm\src\channel.rs:59
  - entroly-wasm\src\channel.rs:76
  - entroly-wasm\src\channel.rs:100
  - entroly-wasm\src\channel.rs:183
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: channel

**LOC:** 1330

## Entities
- `fn trigram_hashes(text: &str) -> Vec<u64>` (function)
- `fn build_trigram_set(frags: &[ContextFragment], indices: &[usize]) -> HashSet<u64>` (function)
- `fn marginal_gain(` (function)
- `pub fn channel_trailing_pass(` (function)
- `pub fn attention_weight(position: usize, total: usize) -> f64` (function)
- `pub fn semantic_interleave(` (function)
- `pub fn information_reward(` (function)
- `pub fn modulated_reward(success: bool, sufficiency: f64) -> f64` (function)
- `pub struct ContradictionReport` (struct)
- `pub fn contradiction_guard(` (function)
- `pub fn bookend_calibrate(` (function)
- `fn frag(id: &str, content: &str, tokens: u32, source: &str) -> ContextFragment` (function)
- `fn test_trailing_pass_fills_gap()` (function)
- `fn test_trailing_pass_zero_gap_returns_empty()` (function)
- `fn test_trailing_pass_respects_budget()` (function)
- `fn test_marginal_gain_is_submodular()` (function)
- `fn test_attention_u_shaped()` (function)
- `fn test_attention_single_fragment()` (function)
- `fn test_interleave_preserves_all_indices()` (function)
- `fn test_interleave_respects_causal_order()` (function)
- `fn test_interleave_two_fragments()` (function)
- `fn test_information_reward_high_util()` (function)
- `fn test_information_reward_zero_util()` (function)
- `fn test_modulated_reward_bounds()` (function)
- `fn test_modulated_reward_credit_assignment()` (function)
- `fn test_trailing_pass_performance_1000_frags()` (function)
- `fn test_trailing_pass_empty_fragment_list()` (function)
- `fn test_trailing_pass_all_already_selected()` (function)
- `fn test_trailing_pass_all_candidates_oversized()` (function)
- `fn test_trailing_pass_single_token_gap()` (function)
- `fn test_trailing_pass_zero_entropy_fragments()` (function)
- `fn test_trailing_pass_no_duplicate_indices()` (function)
- `fn test_trailing_pass_incremental_submodularity()` (function)
- `fn test_trailing_pass_with_very_short_content()` (function)
- `fn test_interleave_empty()` (function)
- `fn test_interleave_single()` (function)
- `fn test_interleave_cyclic_dependencies()` (function)
- `fn test_interleave_deep_dependency_chain()` (function)
- `fn test_interleave_star_dependency()` (function)
- `fn test_interleave_mismatched_relevances()` (function)
- `fn test_attention_large_context_no_nan_inf()` (function)
- `fn test_attention_zero_total()` (function)
- `fn test_attention_symmetry()` (function)
- `fn test_information_reward_empty_inputs()` (function)
- `fn test_information_reward_single_fragment()` (function)
- `fn test_information_reward_no_nan_with_zero_entropy()` (function)
- `fn test_modulated_reward_extreme_sufficiency()` (function)
- `fn test_modulated_reward_is_always_finite()` (function)
- `fn test_full_pipeline_trailing_then_interleave()` (function)
- `fn test_contradiction_guard_no_contradictions()` (function)
- `fn test_contradiction_guard_same_source_different_content()` (function)
- `fn test_contradiction_guard_single_fragment()` (function)
- `fn test_contradiction_guard_empty()` (function)
- `fn test_contradiction_guard_different_sources_no_eviction()` (function)
- `fn test_bookend_preserves_all_indices()` (function)
- `fn test_bookend_small_input()` (function)
- `fn test_bookend_empty()` (function)
