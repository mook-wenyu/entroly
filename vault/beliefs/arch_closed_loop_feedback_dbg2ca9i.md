---
claim_id: dbg2ca9i_closed_loop
entity: closed_loop_feedback
status: inferred
confidence: 0.87
sources:
  - entroly-core/src/utilization.rs:1
  - entroly-core/src/guardrails.rs:19
  - entroly-core/src/resonance.rs:19
  - entroly-core/src/causal.rs:16
  - entroly-core/src/cache.rs:66
  - bench/autotune.py:1
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - utilization_18a33f4c
  - autotune_18a33f4c
  - resonance_18a33f4c
  - causal_18a33f4c
epistemic_layer: evolution
boundary_note: "Outcome recording = Truth. Feedback loops = Evolution."
---

# Closed-Loop Feedback: Three Feedback Timescales

Most RAG systems are open-loop: stuff context in, hope it helps. Entroly has three closed-loop feedback mechanisms operating at different timescales.

## Per-Turn Feedback (Milliseconds to Seconds)

**Utilization scoring** (utilization.rs): After the LLM responds, measures how much of each injected fragment the LLM actually used:
- 40% trigram Jaccard overlap (fragment content vs. LLM response)
- 60% identifier overlap (function/variable names referenced)
- Fragment is "used" if combined > 0.1

This feeds back into:
- `record_success(fragment_ids)` / `record_failure(fragment_ids)` on EntrolyEngine
- FeedbackTracker updates per-fragment value multipliers
- ResonanceMatrix updates pairwise co-selection strengths
- CausalContextGraph records interventional traces
- EGSC cache quality scores (Wilson scoring: successes/failures)
- PRISM weight gradient computation

## Per-Session Feedback (Minutes)

**Query Persona Manifold** adapts across a session:
- Pitman-Yor process discovers query archetypes dynamically
- Per-archetype weights diverge from global weights
- Lifecycle: birth (new archetype) -> growth (weight learning) -> death (Ebbinghaus decay) -> fusion (merge similar archetypes)

**EGSC cache** learns per-session:
- Thompson Sampling admission (Beta posterior on hit probability)
- Linear bandit hit predictor (4-feature model, online SGD)
- Quality scores drive eviction (Wilson lower bound < 0.15 -> GC)

## Cross-Session Feedback (Hours to Days)

**Autotune** (bench/autotune.py): Overnight hyperparameter optimization:
1. Mutate one parameter in tuning_config.json
2. Run benchmark suite (evaluate.py)
3. Keep if composite_score improves, discard if regresses
4. Optional PRISM spectral directions for principled mutation

This tunes: scoring weights, decay half-life, exploration rate, sliding window fraction, PRISM learning rate, IOS info factors, diversity floor.

## The Feedback Hierarchy

```
Turn-level:    FeedbackTracker -> fragment multipliers (immediate)
               ResonanceMatrix -> pairwise synergies (10-turn convergence)
               CausalGraph -> interventional estimates (3+ exploration trials)

Session-level: QueryPersonaManifold -> per-archetype weights (~20 turns)
               EGSC cache -> admission/eviction (~50 queries)
               PRISM -> global weight learning (~100 turns)

Cross-session: Autotune -> hyperparameters (50-200 iterations overnight)
```

Each level learns on top of the one below it. Turn-level feedback provides the signal; session-level aggregates the pattern; cross-session locks in the meta-parameters.

## Related Modules

- **Modules:** [[autotune_18a33f4c]], [[cache_18a33f4c]], [[causal_18a33f4c]], [[cogops_18a33f4c]], [[resonance_18a33f4c]], [[utilization_18a33f4c]], [[value_tracker_18a33f4c]]
- **Related architectures:** [[arch_optimize_pipeline_a7c2e1f0]], [[arch_rl_learning_loop_b3d4f2a1]]
