---
claim_id: 18a336a72a3704602a4e9a60
entity: anomaly
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\anomaly.rs:44
  - entroly-wasm\src\anomaly.rs:55
  - entroly-wasm\src\anomaly.rs:65
  - entroly-wasm\src\anomaly.rs:85
  - entroly-wasm\src\anomaly.rs:93
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: anomaly

**LOC:** 378

## Entities
- `pub enum AnomalyType` (enum)
- `pub fn label(&self) -> &'static str` (function)
- `pub struct EntropyAnomaly` (struct)
- `pub struct AnomalyReport` (struct)
- `fn median(sorted: &[f64]) -> f64` (function)
- `fn directory_of(source: &str) -> String` (function)
- `pub fn scan_anomalies(fragments: &[&ContextFragment]) -> AnomalyReport` (function)
- `fn basename(path: &str) -> &str` (function)
- `fn make_frag(id: &str, source: &str, entropy: f64, content: &str) -> ContextFragment` (function)
- `fn test_spike_detection()` (function)
- `fn test_drop_detection()` (function)
- `fn test_small_group_skipped()` (function)
- `fn test_uniform_group_no_anomalies()` (function)
- `fn test_cross_directory_isolation()` (function)
