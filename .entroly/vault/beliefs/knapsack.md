---
claim_id: e83996fb-45df-4b51-94f6-778dc87f5bbd
entity: knapsack
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/knapsack.rs:44
  - entroly-core/src/knapsack.rs:64
  - entroly-core/src/knapsack.rs:91
  - entroly-core/src/knapsack.rs:107
  - entroly-core/src/knapsack.rs:123
  - entroly-core/src/knapsack.rs:242
  - entroly-core/src/knapsack.rs:311
  - entroly-core/src/knapsack.rs:412
  - entroly-core/src/knapsack.rs:474
  - entroly-core/src/knapsack.rs:498
last_checked: 2026-04-14T04:12:29.611695+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: knapsack

**Language:** rust
**Lines of code:** 628

## Types
- `pub struct ScoringWeights` — Weights for the four-dimensional relevance scoring.
- `pub struct KnapsackResult` — Result of a knapsack optimization run.

## Functions
- `fn sigmoid(x: f64) -> f64` — Numerically stable sigmoid σ(x). Clamped to [-500, 500] — no NaN, no Inf, no overflow.
- `fn linear_score(frag: &ContextFragment, w: &ScoringWeights, fm: f64) -> f64` — Raw linear score for a fragment, scaled by the per-fragment RL feedback multiplier.  This is the **pre-softcap** score — the same landscape used in the REINFORCE backward pass. Feedback multipliers sh
- `fn knapsack_optimize(
    fragments: &[ContextFragment],
    token_budget: u32,
    weights: &ScoringWeights,
    feedback_mults: &HashMap<String, f64>,
    temperature: f64,
) -> KnapsackResult` — Select the most valuable subset of fragments within the token budget.  `temperature` controls the forward-pass mode: - `temperature < 0.05` → exact 0/1 DP (optimal, used at weight convergence) - `temp
- `fn compute_lambda_star(
    scored: &[(usize, f64)` — "expected" to be included given the actual budget consumed by IOS.  # Arguments - `scored`: (fragment_idx, linear_score) pairs for all candidates - `fragments`: fragment slice (for token counts) - `bu
- `fn soft_bisection_select(
    scored: &[(usize, f64)` — exact when all tokens_i are equal — a bias-inducing simplification.  Dual feasibility: find λ* ≥ 0 such that Σ p*ᵢ·tokensᵢ = B. g(λ) = Σ σ((sᵢ − λ·tokensᵢ)/τ)·tokensᵢ − B dg/dλ = −1/τ · Σ p_i(1−p_i)·t
- `fn knapsack_dp(
    scored: &[(usize, f64)` — Exact 0/1 knapsack via DP with budget quantization.  Quantize budget into Q=1000 bins to bound the DP table at N×1000. Precision loss: < 0.1% of optimal value.  Small fragments (token_count < granular
- `fn knapsack_greedy(
    scored: &[(usize, f64)` — Greedy approximation for very large sets (N > 2000) under hard τ. Sort by relevance/token density. Provable 0.5 optimality (Dantzig, 1957).
- `fn pinned_relevance(
    pinned: &[usize],
    fragments: &[ContextFragment],
    weights: &ScoringWeights,
    feedback_mults: &HashMap<String, f64>,
) -> f64` — Compute total relevance for pinned fragments only.

## Dependencies
- `crate::fragment::`
- `std::collections::HashMap`
