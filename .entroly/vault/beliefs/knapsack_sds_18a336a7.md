---
claim_id: 18a336a72b5d62f82b74f8f8
entity: knapsack_sds
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\knapsack_sds.rs:38
  - entroly-wasm\src\knapsack_sds.rs:50
  - entroly-wasm\src\knapsack_sds.rs:56
  - entroly-wasm\src\knapsack_sds.rs:63
  - entroly-wasm\src\knapsack_sds.rs:71
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: knapsack_sds

**LOC:** 636

## Entities
- `pub enum Resolution` (enum)
- `pub struct InfoFactors` (struct)
- `fn default() -> Self` (function)
- `fn info_factor(&self, factors: &InfoFactors) -> f64` (function)
- `pub fn as_str(&self) -> &'static str` (function)
- `pub struct Candidate` (struct)
- `pub struct SdsResult` (struct)
- `fn diversity_factor(candidate_hash: u64, selected_hashes: &[u64]) -> f64` (function)
- `fn compute_pairwise_diversity(hashes: &[u64]) -> f64` (function)
- `pub fn ios_select(` (function)
- `fn empty_feedback() -> HashMap<String, f64>` (function)
- `fn default_factors() -> InfoFactors` (function)
- `fn make_frag(id: &str, content: &str, tokens: u32, source: &str) -> ContextFragment` (function)
- `fn test_empty_fragments()` (function)
- `fn test_single_fragment_selected()` (function)
- `fn test_pinned_always_included()` (function)
- `fn test_diversity_penalizes_duplicates()` (function)
- `fn test_multi_resolution_fits_more()` (function)
- `fn test_budget_respected()` (function)
- `fn test_feedback_multiplier_affects_selection()` (function)
- `fn test_reference_resolution_very_cheap()` (function)
- `fn test_diversity_score_range()` (function)
- `fn test_resolution_preference_by_budget()` (function)
- `fn test_fast_path_selects_all_when_budget_generous()` (function)
