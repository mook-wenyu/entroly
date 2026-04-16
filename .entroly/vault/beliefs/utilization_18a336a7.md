---
claim_id: 18a336a72c5cd5e42c746be4
entity: utilization
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\utilization.rs:28
  - entroly-wasm\src\utilization.rs:43
  - entroly-wasm\src\utilization.rs:55
  - entroly-wasm\src\utilization.rs:73
  - entroly-wasm\src\utilization.rs:82
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: utilization

**LOC:** 236

## Entities
- `pub struct FragmentUtilization` (struct)
- `pub struct UtilizationReport` (struct)
- `fn trigrams(text: &str) -> HashSet<Vec<String>>` (function)
- `fn identifier_set(text: &str) -> HashSet<String>` (function)
- `pub fn score_utilization(` (function)
- `fn make_frag(id: &str, content: &str) -> ContextFragment` (function)
- `fn test_full_utilization()` (function)
- `fn test_zero_utilization()` (function)
- `fn test_partial_utilization()` (function)
- `fn test_empty_fragments()` (function)
- `fn test_identifier_overlap_weighted_higher()` (function)
