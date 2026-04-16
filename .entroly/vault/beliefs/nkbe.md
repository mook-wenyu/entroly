---
claim_id: 12fb8f0c-da19-413d-9723-d0ab96570123
entity: nkbe
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/nkbe.rs:32
  - entroly-core/src/nkbe.rs:42
  - entroly-core/src/nkbe.rs:53
  - entroly-core/src/nkbe.rs:362
  - entroly-core/src/nkbe.rs:390
  - entroly-core/src/nkbe.rs:402
last_checked: 2026-04-14T04:12:29.651334+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: nkbe

**Language:** rust
**Lines of code:** 508

## Types
- `pub struct AgentBudgetState` — Per-agent state for budget allocation.
- `pub struct NkbeFragment` — Fragment descriptor for NKBE allocation.
- `pub struct NkbeAllocator` — NKBE Allocator — multi-agent token budget allocation.  Implements two-phase KKT bisection with Nash Bargaining refinement and REINFORCE gradient for RL weight learning.

## Functions
- `fn reinforce_gradient(
    features: &[[f64; 4]],    // Per-fragment feature vectors
    selections: &[bool],       // Whether each fragment was selected
    reward: f64,               // Outcome quality
    probabilities: &[f64],     // Selection probabilities p*ᵢ
    tau: f64,                  // Temperature
) -> [f64; 4]` — REINFORCE gradient computation for 4D scoring weights.  ∂E[R]/∂wₖ = Σᵢ (aᵢ − p*ᵢ) · R · σ'(zᵢ/τ) · featureᵢₖ  Returns gradient vector [Δw_recency, Δw_frequency, Δw_semantic, Δw_entropy].
- `fn sigmoid(x: f64) -> f64` — Numerically stable sigmoid.
- `fn softplus(x: f64) -> f64` — Numerically stable softplus: log(1 + exp(x)).

## Dependencies
- `pyo3::prelude::`
- `pyo3::types::PyDict`
- `std::collections::HashMap`
