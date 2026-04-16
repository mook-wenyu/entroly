---
claim_id: 18a336a72b46976c2b5e2d6c
entity: knapsack
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\knapsack.rs:44
  - entroly-wasm\src\knapsack.rs:52
  - entroly-wasm\src\knapsack.rs:64
  - entroly-wasm\src\knapsack.rs:91
  - entroly-wasm\src\knapsack.rs:107
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: knapsack

**LOC:** 627

## Entities
- `pub struct ScoringWeights` (struct)
- `fn default() -> Self` (function)
- `pub struct KnapsackResult` (struct)
- `fn sigmoid(x: f64) -> f64` (function)
- `fn linear_score(frag: &ContextFragment, w: &ScoringWeights, fm: f64) -> f64` (function)
- `pub fn knapsack_optimize(` (function)
- `pub fn compute_lambda_star(` (function)
- `fn soft_bisection_select(` (function)
- `fn knapsack_dp(` (function)
- `fn knapsack_greedy(` (function)
- `fn pinned_relevance(` (function)
- `fn no_feedback() -> HashMap<String, f64>` (function)
- `fn test_knapsack_selects_optimal()` (function)
- `fn test_soft_bisection_selects_optimal()` (function)
- `fn test_small_fragments_not_penalized()` (function)
- `fn test_feedback_affects_selection()` (function)
- `fn test_soft_bisection_respects_budget()` (function)
- `fn test_temperature_transition()` (function)
