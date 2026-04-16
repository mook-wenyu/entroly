---
claim_id: cda3558e-08aa-4d97-8ab6-6b11b59ccd2d
entity: knapsack_sds
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/knapsack_sds.rs:64
  - entroly-core/src/knapsack_sds.rs:109
  - entroly-core/src/knapsack_sds.rs:45
  - entroly-core/src/knapsack_sds.rs:130
  - entroly-core/src/knapsack_sds.rs:152
  - entroly-core/src/knapsack_sds.rs:190
last_checked: 2026-04-14T04:12:29.614945+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: knapsack_sds

**Language:** rust
**Lines of code:** 733

## Types
- `pub struct InfoFactors` — Configurable information retention factors for each resolution level. These control the value/cost trade-off in multi-resolution knapsack. Tunable via tuning_config.json → autotune daemon.  Belief fac
- `pub struct SdsResult` — Result of the IOS selection.
- `pub enum Resolution` — Resolution level for a selected fragment.  Hierarchical Context Synthesis: four abstraction levels that mirror how engineers actually hold code in working memory. Full      → raw code (100% info, 100%

## Functions
- `fn diversity_factor(candidate_hash: u64, selected_hashes: &[u64]) -> f64` — Similarity is estimated from SimHash Hamming distance: sim(a, b) = 1 - hamming(a, b) / 64  When the selected set is empty, diversity = 1.0 (no penalty).  Returns a value in [0, 1] where: 1.0 = complet
- `fn compute_pairwise_diversity(hashes: &[u64]) -> f64` — Compute average pairwise diversity from SimHash fingerprints.  diversity = mean over all pairs of (hamming_distance / 64). Returns 1.0 when ≤ 1 hash (trivially diverse).
- `fn ios_select(
    fragments: &[ContextFragment],
    token_budget: u32,
    w_recency: f64,
    w_frequency: f64,
    w_semantic: f64,
    w_entropy: f64,
    feedback_mults: &HashMap<String, f64>,
    enable_diversity: bool,
    enable_multi_resolution: bool,
    info_factors: &InfoFactors,
    diversity_floor: f64,
    min_candidate_value: f64,
) -> SdsResult` — 3. Greedy loop (greedy-by-density with diversity penalty): - compute marginal_value = base_value × diversity_factor(hash) - select candidate with highest marginal_value / token_cost - remove all other

## Dependencies
- `crate::dedup::hamming_distance`
- `crate::fragment::`
- `std::collections::HashMap`
