---
claim_id: 18a336a72af1502c2b08e62c
entity: entropy
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\entropy.rs:26
  - entroly-wasm\src\entropy.rs:54
  - entroly-wasm\src\entropy.rs:80
  - entroly-wasm\src\entropy.rs:122
  - entroly-wasm\src\entropy.rs:171
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: entropy

**LOC:** 580

## Entities
- `pub fn shannon_entropy(text: &str) -> f64` (function)
- `pub fn normalized_entropy(text: &str) -> f64` (function)
- `pub fn renyi_entropy_2(text: &str) -> f64` (function)
- `pub fn renyi_entropy_alpha(scores: &[f64], alpha: f64) -> f64` (function)
- `pub fn renyi_max(n: usize) -> f64` (function)
- `pub fn entropy_divergence(text: &str) -> f64` (function)
- `pub(crate) fn bits_per_byte(text: &str) -> f64` (function)
- `pub(crate) fn bpb_quality(text: &str, redundancy: f64) -> f64` (function)
- `pub fn boilerplate_ratio(text: &str) -> f64` (function)
- `fn is_boilerplate(trimmed: &str) -> bool` (function)
- `pub fn cross_fragment_redundancy(` (function)
- `fn ngram_redundancy(` (function)
- `pub fn information_score(` (function)
- `fn test_entropy_identical_chars()` (function)
- `fn test_entropy_increases_with_diversity()` (function)
- `fn test_boilerplate_detection()` (function)
- `fn test_redundancy_identical()` (function)
- `fn test_multiscale_short_fragment_uses_bigrams()` (function)
- `fn test_multiscale_long_fragment_discriminates()` (function)
- `fn test_bpb_empty()` (function)
- `fn test_bpb_uniform_char()` (function)
- `fn test_bpb_range()` (function)
- `fn test_bpb_boilerplate_lower()` (function)
- `fn test_bpb_quality_combines_density_and_uniqueness()` (function)
- `fn test_renyi_entropy_empty()` (function)
- `fn test_renyi_entropy_uniform()` (function)
- `fn test_renyi_leq_shannon()` (function)
- `fn test_entropy_divergence_nonnegative()` (function)
- `fn test_entropy_divergence_low_for_code()` (function)
- `fn test_noise_penalty_in_information_score()` (function)
