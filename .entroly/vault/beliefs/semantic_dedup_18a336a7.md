---
claim_id: 18a336a72c2957142c40ed14
entity: semantic_dedup
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\semantic_dedup.rs:43
  - entroly-wasm\src\semantic_dedup.rs:50
  - entroly-wasm\src\semantic_dedup.rs:72
  - entroly-wasm\src\semantic_dedup.rs:99
  - entroly-wasm\src\semantic_dedup.rs:133
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: semantic_dedup

**LOC:** 263

## Entities
- `fn content_overlap(a: &str, b: &str) -> f64` (function)
- `fn trigram_jaccard(a: &str, b: &str) -> f64` (function)
- `fn identifier_jaccard(a: &str, b: &str) -> f64` (function)
- `pub fn semantic_deduplicate(` (function)
- `pub struct DeduplicationResult` (struct)
- `pub fn semantic_deduplicate_with_stats(` (function)
- `fn make_frag(id: &str, content: &str, tokens: u32) -> ContextFragment` (function)
- `fn test_redundant_fragments_deduplicated()` (function)
- `fn test_unique_fragments_kept()` (function)
- `fn test_three_way_dedup()` (function)
- `fn test_dedup_stats()` (function)
- `fn test_empty_input()` (function)
- `fn test_threshold_sensitivity()` (function)
