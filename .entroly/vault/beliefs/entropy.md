---
claim_id: e0cfe129-a899-4f70-abf7-cdd27926aae5
entity: entropy
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/entropy.rs:39
  - entroly-core/src/entropy.rs:65
  - entroly-core/src/entropy.rs:93
  - entroly-core/src/entropy.rs:119
  - entroly-core/src/entropy.rs:161
  - entroly-core/src/entropy.rs:210
  - entroly-core/src/entropy.rs:226
  - entroly-core/src/entropy.rs:293
  - entroly-core/src/entropy.rs:317
  - entroly-core/src/entropy.rs:389
last_checked: 2026-04-14T04:12:29.594970+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: entropy

**Language:** rust
**Lines of code:** 650


## Functions
- `fn kolmogorov_entropy(text: &str) -> f64` — This replaces TWO separate O(N) scans (normalized_entropy + boilerplate_ratio) with ONE faster pass that is more theoretically grounded.  Calibration for code files (empirical): - Boilerplate (imports
- `fn shannon_entropy(text: &str) -> f64` — Character-level Shannon entropy in bits per character.  Uses a 256-element byte histogram for O(n) computation with virtually zero allocation overhead.
- `fn normalized_entropy(text: &str) -> f64` — Normalize Shannon entropy to [0, 1]. Max entropy for source code is empirically ~6.0 bits/char.
- `fn renyi_entropy_2(text: &str) -> f64` — Computational advantage: requires only Σ p² (no per-symbol log), making it ~30% faster than Shannon on large fragments.  Used as a secondary signal in the IOS knapsack: fragments with high Shannon but
- `fn renyi_entropy_alpha(scores: &[f64], alpha: f64) -> f64` — normalizes them to a probability distribution internally.  Used by EGSC's admission gate: given per-fragment entropy scores s₁, ..., sₖ, we form pᵢ = sᵢ/Σsⱼ and compute H₂(p) to measure the *diversity
- `fn renyi_max(n: usize) -> f64` — Maximum possible Rényi entropy for n elements: H₂_max = log₂(n).  When all pᵢ = 1/n (uniform distribution), H₂ = log₂(n). Used to normalize EGSC admission threshold to [0, 1] scale.
- `fn entropy_divergence(text: &str) -> f64` — but collision entropy is low, the fragment has many unique-but-rare symbols (e.g., binary-encoded data, UUID strings, minified code).  High divergence → likely noise or encoded data, not useful contex
- `fn boilerplate_ratio(text: &str) -> f64` — Boilerplate pattern matcher. Returns the fraction of non-empty lines matching common boilerplate.  Hardcoded patterns for speed (no regex dependency): - import/from imports - pass/... - dunder methods
- `fn is_boilerplate(trimmed: &str) -> bool` — Fast boilerplate check without regex.
- `fn simhash_uniqueness(fp: u64, sample_fps: &[u64]) -> f64` — For k=50 sample fragments, ~900x faster on 5KB files.  Mathematical basis (Charikar 2002 LSH): Pr[simhash(A)[i] == simhash(B)[i]] ≈ 1 - θ/π where θ = arccos(cosine_similarity(A, B)). Hamming distance 
- `fn cross_fragment_redundancy(
    fragment: &str,
    others: &[&str],
) -> f64`
- `fn ngram_redundancy(
    words: &[&str],
    others: &[&str],
    ngram_size: usize,
) -> f64` — Compute single-scale n-gram overlap ratio against a set of other fragments. Parallelises over others when len > 10 (Rayon).
- `fn information_score(
    text: &str,
    other_fragments: &[&str],
) -> f64` — Compute the final information density score.  Combines: 40% Shannon entropy (normalized) 30% Boilerplate penalty (1 - ratio) 30% Uniqueness (1 - adaptive multi-scale redundancy)

## Dependencies
- `rayon::prelude::`
- `std::collections::HashSet`
- `std::io::Write`
