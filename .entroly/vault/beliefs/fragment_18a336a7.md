---
claim_id: 18a336a72b00d5382b186b38
entity: fragment
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\fragment.rs:14
  - entroly-wasm\src\fragment.rs:47
  - entroly-wasm\src\fragment.rs:84
  - entroly-wasm\src\fragment.rs:128
  - entroly-wasm\src\fragment.rs:141
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: fragment

**LOC:** 216

## Entities
- `pub struct ContextFragment` (struct)
- `pub fn new(fragment_id: String, content: String, token_count: u32, source: String) -> Self` (function)
- `pub fn compute_relevance(` (function)
- `pub fn softcap(x: f64, cap: f64) -> f64` (function)
- `pub fn apply_ebbinghaus_decay(` (function)
- `fn test_ebbinghaus_half_life()` (function)
- `fn test_relevance_scoring()` (function)
- `fn test_softcap_properties()` (function)
