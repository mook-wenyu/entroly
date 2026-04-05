---
claim_id: a7c2e1f0_optimize_pipeline
entity: optimize_pipeline
status: inferred
confidence: 0.92
sources:
  - entroly-core/src/lib.rs:619
  - entroly-core/src/lib.rs:793
  - entroly-core/src/lib.rs:900
  - entroly-core/src/knapsack.rs:123
  - entroly-core/src/knapsack_sds.rs:173
  - entroly-core/src/channel.rs:1
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - knapsack_18a33f4c
  - fragment_18a33f4c
  - knapsack_sds_18a33f4c
  - channel_18a33f4c
  - resonance_18a33f4c
  - causal_18a33f4c
epistemic_layer: action
boundary_note: "Knapsack solving = Action. Cost modeling = Belief."
---

# The Optimize Pipeline: 12-Stage Context Selection

The `EntrolyEngine::optimize()` method (lib.rs:619) is the central orchestration point. It chains 12 distinct stages into a single deterministic pipeline. Understanding this flow is essential because every other module feeds into or derives from it.

## Stage Sequence

1. **EGSC Cache Check** (lib.rs:656) — O(1) exact hash, then O(L*k) SimHash LSH lookup. On hit, skip stages 2-11 entirely. Cache key = (query, fragment_id_set, effective_budget).

2. **Semantic Score Update** (lib.rs:728) — SimHash Hamming distance between query fingerprint and each fragment fingerprint. Coarse semantic similarity without embeddings.

3. **Feedback Multiplier Build** (lib.rs:737) — Per-fragment RL-learned value multiplier from `FeedbackTracker`. Range: [0.01, unbounded), softcapped later.

4. **Query Persona Routing** (lib.rs:744) — Pitman-Yor process assigns query to an archetype via `QueryPersonaManifold`. Per-archetype learned weights override global weights.

5. **Initial Knapsack** (lib.rs:793) — Soft bisection (temperature >= 0.05) or exact DP (temperature < 0.05). Produces initial selection + lambda_star for REINFORCE.

6. **Dependency Boost** (lib.rs:801) — `DepGraph::compute_dep_boosts()` finds unselected fragments depended upon by selected ones. Score boost = 0.5 * dependency strength.

7. **Context Resonance** (lib.rs:807) — Pairwise interaction bonuses from `ResonanceMatrix`. Supermodular: fragments that historically co-occur in successful outputs get boosted.

8. **Causal Gravity + Temporal Chains** (lib.rs:821) — `CausalContextGraph` provides information gravity (do-calculus) and temporal transfer entropy bonuses from previous turn's selection.

9. **Coverage Estimation** (lib.rs:842) — Chapman mark-recapture estimator: N_hat = (N1 * N2) / m. Estimates unseen relevant fragments (unknown unknowns).

10. **IOS Selection** (lib.rs:900) — Submodular Diversity Selection + Multi-Resolution Knapsack. Each fragment can be included at Full/Skeleton/Reference resolution. Greedy-by-density with diversity penalty.

11. **RAVEN-UCB Exploration** (lib.rs:960) — With probability `exploration_rate`, swap out the lowest-scoring selected fragment for an unselected one (random or UCB-max). Creates natural experiments for causal estimation.

12. **Channel Coding Trailing Pass** (channel.rs) — Fill remaining budget gap with marginal information gain (submodular). Then attention-aware semantic interleaving for U-shaped placement.

## Key Architectural Decision: Score Boosting vs. Separate Dimensions

Dependency, resonance, and causal bonuses are applied as **additive boosts to `semantic_score`** rather than as separate scoring dimensions. This is a deliberate simplification: PRISM already learns 4-5 weight dimensions, and adding 3 more would make the optimization surface too noisy for the ~100-turn learning horizons typical in practice. The trade-off is that these signals cannot be independently weighted by PRISM.

Exception: resonance IS a 5th PRISM dimension (w_resonance), but it modulates the resonance bonus magnitude rather than replacing the semantic_score injection.

## Performance Characteristics

- Cache hit path: O(1) to O(L*k) where L=12 tables, k=10 bits
- Full pipeline: O(N log N) dominated by IOS greedy sort and soft bisection (30 iterations * N)
- Typical latency: <1ms for N=500 fragments on commodity hardware

## Related Modules

- **Modules:** [[cache_18a33f4c]], [[causal_18a33f4c]], [[channel_18a33f4c]], [[dedup_18a33f4c]], [[fragment_18a33f4c]], [[knapsack_18a33f4c]], [[knapsack_sds_18a33f4c]], [[lib_18a33f4c]], [[lsh_18a33f4c]], [[resonance_18a33f4c]]
- **Related architectures:** [[arch_closed_loop_feedback_dbg2ca9i]], [[arch_concurrency_model_ecf3db0j]], [[arch_dedup_hierarchy_e6a7b5d4]], [[arch_information_theory_stack_d5f6a4c3]], [[arch_memory_lifecycle_b9dae8g7]], [[arch_multi_resolution_f7b8c6e5]], [[arch_rl_learning_loop_b3d4f2a1]], [[arch_scoring_dimensions_caf1b9h8]]
