---
claim_id: b3d4f2a1_rl_learning_loop
entity: rl_learning_loop
status: inferred
confidence: 0.88
sources:
  - entroly-core/src/prism.rs:1
  - entroly-core/src/knapsack.rs:7
  - entroly-core/src/fragment.rs:57
  - entroly-core/src/lib.rs:134
  - entroly-core/src/lib.rs:795
  - entroly-core/src/resonance.rs:19
  - entroly-core/src/causal.rs:16
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - prism_18a33f4c
  - knapsack_18a33f4c
  - fragment_18a33f4c
epistemic_layer: evolution
boundary_note: "Reward signals = Verification. Policy updates = Evolution."
---

# The Reinforcement Learning Loop: PRISM + REINFORCE + ADGT

Entroly treats context selection as a reinforcement learning problem. The system learns which scoring weights produce the best LLM outputs over time. This belief documents the full learning cycle.

## Forward Pass (Selection)

1. **Linear scoring**: s_i = w^T * [recency, frequency, semantic, entropy] * feedback_multiplier (knapsack.rs:107)
2. **Soft bisection**: Find lambda* such that sum(sigmoid((s_i - lambda* * tokens_i) / tau) * tokens_i) = Budget (knapsack.rs:7)
3. **Selection probabilities**: p_i = sigmoid((s_i - lambda* * tokens_i) / tau) — these are the policy's inclusion probabilities

## Reward Signal

- `record_success(fragment_ids)` / `record_failure(fragment_ids)` — binary signal from user or utilization scoring
- Channel coding provides continuous reward: attention-weighted utilization * sufficiency (channel.rs:17)
- Reward baseline EMA (lib.rs:159): advantage A = R - mu_baseline (variance reduction for REINFORCE)

## Backward Pass (Weight Update via PRISM)

PRISM (Anisotropic Spectral Optimizer) replaces isotropic SGD:

1. **Gradient computation**: REINFORCE policy gradient g_j = sum_i((selected_i - p_i) * feature_ij * advantage)
2. **Covariance tracking**: C = beta * C + (1-beta) * g * g^T (running EMA of gradient outer product)
3. **Eigendecomposition**: C = Q * Lambda * Q^T via Jacobi method (exact for 4-5 dimensions)
4. **Anisotropic update**: w += alpha * Q * Lambda^(-1/2) * Q^T * g

The key insight: if one weight dimension (e.g., resonance) has high gradient variance, Lambda^(-1/2) automatically shrinks its learning rate. This is why resonance can be a 5th PRISM dimension despite being inherently noisier than individual fragment scores.

## Temperature Annealing (ADGT)

The gradient temperature tau controls explore/exploit:
- High tau (~2.0): soft selection, smooth gradients, exploration
- Low tau (<0.05): hard selection (DP fallback), pure exploitation

ADGT (Adaptive Dual Gap Temperature) replaces ad-hoc 0.995 annealing:
- dual_gap = D(lambda*) - primal_value (knapsack.rs:76)
- Large gap: weights not converged, keep tau high
- Small gap: weights converged, lower tau

## Multi-Level Learning

The system learns at four levels simultaneously:
1. **Global weights** (w_recency, w_frequency, w_semantic, w_entropy) via 4D PRISM
2. **Per-archetype weights** via QueryPersonaManifold (Pitman-Yor process discovers archetypes)
3. **Per-fragment value** via FeedbackTracker (TD(lambda) eligibility traces on ContextFragment)
4. **Pairwise interactions** via ResonanceMatrix (fragment pair synergies)

## Causal Deconfounding

The exploration mechanism (RAVEN-UCB) creates natural experiments that enable the CausalContextGraph to distinguish correlation from causation. Fragments randomly included via exploration get interventional success rate estimates P(success | do(include f)), while naturally selected fragments only get observational estimates. The gap reveals confounding bias.

## Related Modules

- **Modules:** [[autotune_18a33f4c]], [[fragment_18a33f4c]], [[knapsack_18a33f4c]], [[prism_18a33f4c]], [[resonance_18a33f4c]], [[utilization_18a33f4c]]
- **Related architectures:** [[arch_closed_loop_feedback_dbg2ca9i]], [[arch_optimize_pipeline_a7c2e1f0]], [[arch_scoring_dimensions_caf1b9h8]]
