---
claim_id: 3c034130-690d-4467-a621-4e3c9dd8ce66
entity: prism
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/prism.rs:33
  - entroly-core/src/prism.rs:203
  - entroly-core/src/prism.rs:450
last_checked: 2026-04-14T04:12:29.656342+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: prism

**Language:** rust
**Lines of code:** 762

## Types
- `pub struct SymMatrixN` — An NxN symmetric matrix stored as a flat array for tracking gradient covariance.  Uses `N * N` flat layout (row-major) since const generic expressions like `[f64; N * N]` require nightly features. The
- `pub struct PrismOptimizerN` — of their individual contributions. PRISM learns to weight this signal relative to the four individual-fragment dimensions.  Key insight: resonance gradients are inherently noisier than individual scor
- `pub struct ResonanceDiagnostics` — Diagnostics for the resonance dimension in 5D PRISM.

## Dependencies
- `serde::`
- `std::f64`
