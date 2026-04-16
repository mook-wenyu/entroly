---
claim_id: 18a336a72bb4bfd02bcc55d0
entity: prism
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\prism.rs:33
  - entroly-wasm\src\prism.rs:39
  - entroly-wasm\src\prism.rs:43
  - entroly-wasm\src\prism.rs:50
  - entroly-wasm\src\prism.rs:55
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: prism

**LOC:** 761

## Entities
- `pub struct SymMatrixN` (struct)
- `pub fn new() -> Self` (function)
- `pub fn identity() -> Self` (function)
- `pub fn get(&self, i: usize, j: usize) -> f64` (function)
- `pub fn set(&mut self, i: usize, j: usize, val: f64)` (function)
- `pub fn update_ema(&mut self, g: &[f64], beta: f64)` (function)
- `pub fn jacobi_eigendecomposition(&self) -> (SymMatrixN<N>, Vec<f64>)` (function)
- `pub fn from_array(data: [[f64; 4]; 4]) -> Self` (function)
- `pub fn to_array(&self) -> [[f64; 4]; 4]` (function)
- `pub struct PrismOptimizerN` (struct)
- `pub fn new(learning_rate: f64) -> Self` (function)
- `pub fn compute_update(&mut self, g: &[f64]) -> Vec<f64>` (function)
- `pub fn condition_number(&self) -> f64` (function)
- `pub fn eigenvalues(&self) -> Vec<f64>` (function)
- `pub fn spectral_energy(&self) -> Vec<f64>` (function)
- `pub fn compute_update_4d(&mut self, g: &[f64; 4]) -> [f64; 4]` (function)
- `pub fn condition_number_4d(&self) -> f64` (function)
- `pub fn from_4d(opt4: &PrismOptimizer) -> Self` (function)
- `pub fn resonance_diagnostics(&self) -> ResonanceDiagnostics` (function)
- `pub struct ResonanceDiagnostics` (struct)
- `fn test_jacobi_eigendecomposition_diagonal_4d()` (function)
- `fn test_anisotropic_shaping_dampens_noise_4d()` (function)
- `fn test_4d_backward_compat_api()` (function)
- `fn test_jacobi_eigendecomposition_5d()` (function)
- `fn test_5d_resonance_damping()` (function)
- `fn test_5d_from_4d_preserves_covariance()` (function)
- `fn test_5d_cross_correlation_emergence()` (function)
- `fn test_5d_condition_number_increases_with_resonance()` (function)
- `fn test_spectral_energy_sums_to_one()` (function)
- `fn test_sym_matrix4_array_roundtrip()` (function)
- `fn test_5d_non_diagonal_eigendecomposition()` (function)
