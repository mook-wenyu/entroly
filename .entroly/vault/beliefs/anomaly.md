---
claim_id: 597b7f08-74ce-4019-be62-0e442f04833a
entity: anomaly
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/anomaly.rs:65
  - entroly-core/src/anomaly.rs:85
  - entroly-core/src/anomaly.rs:44
  - entroly-core/src/anomaly.rs:93
  - entroly-core/src/anomaly.rs:106
  - entroly-core/src/anomaly.rs:119
  - entroly-core/src/anomaly.rs:264
last_checked: 2026-04-14T04:12:29.534720+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: anomaly

**Language:** rust
**Lines of code:** 379

## Types
- `pub struct EntropyAnomaly` — A single entropy anomaly detected in the codebase.
- `pub struct AnomalyReport` — Full anomaly scan report.
- `pub enum AnomalyType`

## Functions
- `fn median(sorted: &[f64]) -> f64` — Compute the median of a sorted slice.
- `fn directory_of(source: &str) -> String` — Extract directory from a source path. "src/handlers/auth.rs" → "src/handlers" "auth.rs" → ""
- `fn scan_anomalies(fragments: &[&ContextFragment]) -> AnomalyReport` — Scan all fragments for entropy anomalies using robust Z-scores.  Groups fragments by directory, computes MAD-based Z-scores within each group, and flags fragments with |z| > 2.5.
- `fn basename(path: &str) -> &str`

## Dependencies
- `crate::entropy::boilerplate_ratio`
- `crate::fragment::ContextFragment`
- `serde::`
- `std::collections::HashMap`
