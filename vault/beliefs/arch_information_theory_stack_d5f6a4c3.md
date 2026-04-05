---
claim_id: d5f6a4c3_information_theory_stack
entity: information_theory_stack
status: inferred
confidence: 0.90
sources:
  - entroly-core/src/entropy.rs:1
  - entroly-core/src/entropy.rs:69
  - entroly-core/src/entropy.rs:187
  - entroly-core/src/entropy.rs:419
  - entroly-core/src/cache.rs:1
  - entroly-core/src/channel.rs:1
  - entroly-core/src/anomaly.rs:1
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - entropy_18a33f4c
  - cache_18a33f4c
  - channel_18a33f4c
  - anomaly_18a33f4c
epistemic_layer: truth
boundary_note: "Raw entropy = Truth. Information-theoretic scoring = Belief."
---

# Information Theory Stack: Shannon to Channel Coding

Entroly is built on a layered information-theoretic foundation. Each layer uses a different aspect of information theory for a different purpose. This is not a monolithic "entropy score" — it is five distinct applications of information theory composed into a coherent system.

## Layer 1: Fragment-Level Information Density (Shannon + Renyi)

**Shannon entropy** H1 (entropy.rs:26): Measures character-level information density. Stack-allocated 256-element histogram, O(n). Used as the primary entropy_score dimension in the 4D scoring model.

**Renyi entropy** H2 (entropy.rs:80): Collision entropy, always <= H1. More sensitive to concentrated probability mass (boilerplate). Used as a secondary signal: high H1 but low H2 = "entropy inflation" (noise, not information).

**Shannon-Renyi divergence** (entropy.rs:187): H1 - H2. Novel metric: penalizes fragments where divergence > 1.5 bits. Catches base64 blobs, UUID strings, minified code — things that look high-entropy but carry no useful information for LLM reasoning.

## Layer 2: Cross-Fragment Redundancy (Adaptive N-gram)

Multi-scale n-gram overlap (entropy.rs:338): Adaptive weights by fragment length — short fragments use bigram-heavy weights, long fragments use 4-gram-heavy weights. Parallelized via Rayon when > 10 other fragments. This is the uniqueness dimension of the information_score.

## Layer 3: Cache Admission (Renyi Alpha + Thompson Sampling)

EGSC cache (cache.rs:1) uses **generalized Renyi entropy** H_alpha over per-fragment entropy scores to measure context diversity. High H2 of the score distribution means information is spread across many fragments (complex query); low H2 means one fragment dominates (trivial query). The alpha parameter itself is learned online via gradient descent on hit-rate.

## Layer 4: Channel Coding (Shannon Channel Model)

channel.rs models the LLM context window as a noisy communication channel: Encoder (Entroly) -> Channel (LLM attention) -> Decoder (LLM response). Three components:
- Marginal information gain trailing pass: submodular fill of remaining budget gap
- Attention-aware interleaving: U-shaped placement based on "Lost in the Middle" (Liu et al. 2023)
- Information-theoretic reward: continuous RL reward = attention-weighted utilization * sufficiency

## Layer 5: Anomaly Detection (MAD Z-score)

anomaly.rs inverts the entropy lens: instead of "high entropy = good context", it asks "statistically unusual entropy = potential bug". Robust Z-score using Median Absolute Deviation on per-directory entropy groups. Catches copy-paste errors, security anti-patterns, dead logic.

## Composite: The information_score Formula

```
score = 0.40 * normalized_entropy
      + 0.30 * (1 - boilerplate_ratio)
      + 0.30 * (1 - cross_fragment_redundancy)
      - noise_penalty(divergence)
```

The weights (0.40/0.30/0.30) were empirically calibrated. The noise_penalty only kicks in when Shannon-Renyi divergence exceeds 1.5 bits (entropy.rs:442), penalizing by up to 15% of the score.

## Related Modules

- **Modules:** [[anomaly_18a33f4c]], [[cache_18a33f4c]], [[channel_18a33f4c]], [[cognitive_bus_18a33f4c]], [[conversation_pruner_18a33f4c]], [[entropy_18a33f4c]], [[nkbe_18a33f4c]]
- **Related architectures:** [[arch_concurrency_model_ecf3db0j]], [[arch_dedup_hierarchy_e6a7b5d4]], [[arch_optimize_pipeline_a7c2e1f0]]
