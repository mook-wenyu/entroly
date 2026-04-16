---
claim_id: f7a430f5-e275-41db-bc4c-9ce8cb3be0d5
entity: cache
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/cache.rs:47
  - entroly-core/src/cache.rs:136
  - entroly-core/src/cache.rs:221
  - entroly-core/src/cache.rs:286
  - entroly-core/src/cache.rs:409
  - entroly-core/src/cache.rs:495
  - entroly-core/src/cache.rs:529
  - entroly-core/src/cache.rs:598
  - entroly-core/src/cache.rs:753
  - entroly-core/src/cache.rs:874
last_checked: 2026-04-14T04:12:29.546360+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: cache

**Language:** rust
**Lines of code:** 2968

## Types
- `pub struct CacheEntry` — A single cache entry storing an LLM response and its metadata.
- `pub struct CostModel` — Hybrid cost model for cache utility estimation.  U(entry) = P(hit) × (recompute_tokens × cost_per_token + latency_ms) − size_penalty  This optimizes *real-world cost savings*, not abstract hit rate. D
- `pub struct EntropySketch` — Streaming entropy sketch — O(1) moment-based Rényi H₂ approximation.  Maintains running Σpᵢ² without storing the full distribution. When a new score arrives, updates incrementally: Σp² = Σ((old_sᵢ/new
- `pub struct FrequencySketch` —  4-row × 256-column sketch with 4 independent hash functions. Supports periodic halving for non-stationarity (aging).  Used for TinyLFU-style admission gating: admit(new) iff freq(new) > freq(victim) 
- `pub struct ShiftDetector` —  Monitors the running hit-rate EMA and detects sudden drops (negative shift) that indicate a distribution change. When triggered: 1. Halves the frequency sketch (forget old frequencies) 2. Softens the
- `pub struct TailStats` — Tracks per-query cost savings for tail-latency analysis.
- `pub struct AdaptiveAlpha` — Adaptive Rényi order selector.  Learns optimal α via gradient descent on hit-rate: α ← α - η · ∂(miss_rate)/∂α  Heavy-skew workloads → α increases (focus on dominant fragments). Flat workloads → α dec
- `pub struct ThompsonGate` — Thompson Sampling Admission Gate.  Instead of hard-thresholding H_α > τ, we sample from a Beta posterior: p_admit ~ Beta(α_succ + prior, β_fail + prior) ADMIT if H_α(context) · p_admit > 0.5  This nat
- `pub struct SubmodularEvictor` — Submodular diversity-based cache eviction with lazy greedy evaluation.  f(S) = Σ_{i∈S} utility(eᵢ) · diversity(eᵢ, S\{i}) where utility incorporates cost model and time decay.  Lazy evaluation (Minoux
- `pub struct CausalInvalidator` — Causal invalidation with depth-weighted exponential decay.  w(e) ← w(e) · exp(-λ · overlap_ratio · (1/depth_factor))  Direct dependents (depth 1) decay hardest. Transitive dependents (depth 2+) decay 
- `pub struct HitPredictor` — Lightweight linear model predicting P(hit | features).  Features: [context_entropy, fragment_count, query_length_norm, recompute_cost_norm] Updated via online SGD with learning rate decay.  This bridg
- `pub struct EgscConfig`
- `pub struct CacheSnapshot` — Serializable snapshot of the full EGSC cache state.  Captures all entries (sorted by value for predictive warming), all learned parameters, and all stats. Indices are rebuilt on import.  Reference: Pr
- `pub struct EgscCache` — EGSC — Entropy-Gated Submodular Cache (benchmark-grade).
- `pub struct CacheStats` — Diagnostic statistics.
- `pub enum CacheLookup` — Cache lookup result with provenance.

## Dependencies
- `crate::dedup::`
- `crate::lsh::LshIndex`
- `serde::`
- `std::cmp::Ordering`
- `std::collections::`
