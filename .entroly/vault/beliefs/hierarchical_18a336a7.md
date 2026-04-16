---
claim_id: 18a336a72b35cc342b4d6234
entity: hierarchical
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\hierarchical.rs:29
  - entroly-wasm\src\hierarchical.rs:54
  - entroly-wasm\src\hierarchical.rs:82
  - entroly-wasm\src\hierarchical.rs:175
  - entroly-wasm\src\hierarchical.rs:224
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: hierarchical

**LOC:** 749

## Entities
- `pub struct HccResult` (struct)
- `pub fn compress_level1(fragments: &[ContextFragment]) -> (String, u32)` (function)
- `fn extract_oneliner_from_skeleton(skeleton: &str) -> String` (function)
- `pub fn identify_cluster(` (function)
- `pub fn compress_level2(` (function)
- `pub(crate) fn compute_pagerank(` (function)
- `pub fn allocate_budget(` (function)
- `pub fn submodular_marginal_gain(` (function)
- `fn extract_module(source: &str) -> String` (function)
- `pub fn hierarchical_compress(` (function)
- `fn make_frag(id: &str, source: &str, tokens: u32, skeleton: Option<&str>) -> ContextFragment` (function)
- `fn test_level1_generates_oneliners()` (function)
- `fn test_extract_oneliner_caps_at_6()` (function)
- `fn test_identify_cluster_follows_deps()` (function)
- `fn test_budget_allocation()` (function)
- `fn test_submodular_diversity()` (function)
- `fn test_pagerank_hub_gets_highest()` (function)
- `fn test_hierarchical_compress_end_to_end()` (function)
- `fn test_empty_fragments()` (function)
