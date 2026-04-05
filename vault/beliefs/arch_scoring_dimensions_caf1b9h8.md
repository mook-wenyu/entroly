---
claim_id: caf1b9h8_scoring_dimensions
entity: scoring_dimensions
status: inferred
confidence: 0.90
sources:
  - entroly-core/src/fragment.rs:104
  - entroly-core/src/fragment.rs:126
  - entroly-core/src/prism.rs:183
  - entroly-core/src/lib.rs:858
  - entroly-core/src/guardrails.rs:1
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - fragment_18a33f4c
  - prism_18a33f4c
  - guardrails_18a33f4c
epistemic_layer: belief
boundary_note: "Raw signals = Truth. Composite scoring = Belief."
---

# The 5+3 Scoring Dimensions: How Fragments Compete

Fragment selection is driven by a composite score with 5 learned dimensions and 3 injected bonuses. Understanding their interactions explains why specific fragments win or lose.

## The 5 Learned Dimensions (PRISM-Optimized)

| Dim | Name | Source | Default Weight | Update Mechanism |
|-----|------|--------|---------------|-----------------|
| 0 | Recency | Ebbinghaus decay exp(-lambda*dt) | 0.30 | Automatic (turn-based) |
| 1 | Frequency | access_count / max_access_count | 0.25 | Automatic (on access) |
| 2 | Semantic | 1 - hamming(query_hash, frag_hash)/64 | 0.25 | Per-query SimHash distance |
| 3 | Entropy | information_score() | 0.20 | At ingestion (static) |
| 4 | Resonance | mean pairwise interaction with selection | 0.00 (cold start) | Per-feedback update |

PRISM learns these weights online. The 5D PrismOptimizer (prism.rs:183) tracks gradient covariance and applies anisotropic damping — high-variance dimensions get lower learning rates automatically.

## The 3 Injected Bonuses (Not PRISM-Learned)

These modify semantic_score additively during optimize(), outside PRISM's control:

1. **Dependency boost** (lib.rs:862): +0.5 * dep_strength when a selected fragment depends on this one. Ensures function definitions accompany their call sites.

2. **Resonance bonus** (lib.rs:870): w_resonance * mean(R[c][s] for s in selected). Pairwise synergy learned from co-selection success/failure history.

3. **Causal gravity + temporal** (lib.rs:881-888): +0.15 * gravity_bonus + 0.10 * temporal_bonus. Gravity from interventional causal estimates; temporal from transfer entropy across turns.

## The Softcap Compression (fragment.rs:126)

After computing the weighted sum, the composite score is compressed via `c * tanh(x/c)` with cap=0.85. This prevents a single high-feedback fragment from monopolizing the budget. Properties:
- Linear near zero (no distortion for typical scores 0.3-0.7)
- Saturates near cap (score=2.0 compresses to 0.84)
- Monotone and smooth (preserves rank ordering)

## Criticality: The Override Dimension

Guardrails (guardrails.rs) provide a non-negotiable override that bypasses scoring entirely:
- **Safety** files: NEVER dropped (license, security)
- **Critical** files: Always included (package.json, Dockerfile, .env)
- **Important** files: Entropy floor of 0.5 (won't rank last)

These are enforced via is_pinned at ingestion, not via score manipulation. This separation is deliberate: entropy scores stay honest (information density is not inflated for critical files), but selection priority is guaranteed through the pinning mechanism.

## Related Modules

- **Modules:** [[fragment_18a33f4c]], [[guardrails_18a33f4c]], [[health_18a33f4c]], [[knapsack_18a33f4c]], [[prism_18a33f4c]], [[utilization_18a33f4c]]
- **Related architectures:** [[arch_optimize_pipeline_a7c2e1f0]], [[arch_rl_learning_loop_b3d4f2a1]]
