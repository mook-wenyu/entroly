---
claim_id: b88ff12d-3c06-4231-be97-eb897acb6e80
entity: semantic_dedup
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/semantic_dedup.rs:133
  - entroly-core/src/semantic_dedup.rs:43
  - entroly-core/src/semantic_dedup.rs:50
  - entroly-core/src/semantic_dedup.rs:72
  - entroly-core/src/semantic_dedup.rs:99
  - entroly-core/src/semantic_dedup.rs:142
last_checked: 2026-04-14T04:12:29.677606+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: semantic_dedup

**Language:** rust
**Lines of code:** 264

## Types
- `pub struct DeduplicationResult` — Convenience: deduplicate and return count stats.

## Functions
- `fn content_overlap(a: &str, b: &str) -> f64` — Compute content overlap between two fragments using: 50% n-gram overlap (word trigrams) 50% identifier overlap  Returns [0, 1] where 1.0 = identical information.
- `fn trigram_jaccard(a: &str, b: &str) -> f64` — Symmetric trigram Jaccard similarity.
- `fn identifier_jaccard(a: &str, b: &str) -> f64` — Symmetric identifier Jaccard similarity.
- `fn semantic_deduplicate(
    fragments: &[ContextFragment],
    sorted_indices: &[usize],
    threshold: Option<f64>,
) -> Vec<usize>` — contribute at least `threshold` marginal information.  # Arguments * `fragments` - all fragments in the engine * `sorted_indices` - indices into `fragments`, sorted by relevance descending * `threshol
- `fn semantic_deduplicate_with_stats(
    fragments: &[ContextFragment],
    sorted_indices: &[usize],
    threshold: Option<f64>,
) -> DeduplicationResult`

## Dependencies
- `crate::depgraph::extract_identifiers`
- `crate::fragment::ContextFragment`
- `std::collections::HashSet`
