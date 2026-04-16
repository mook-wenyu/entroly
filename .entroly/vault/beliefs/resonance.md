---
claim_id: d4666ff5-92ac-4ef8-8207-87725d601ee2
entity: resonance
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/resonance.rs:136
  - entroly-core/src/resonance.rs:293
  - entroly-core/src/resonance.rs:392
  - entroly-core/src/resonance.rs:327
  - entroly-core/src/resonance.rs:458
last_checked: 2026-04-14T04:12:29.664992+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: resonance

**Language:** rust
**Lines of code:** 713

## Types
- `pub struct ResonanceMatrix` — The Resonance Matrix — learns which fragment pairs produce synergistic LLM outputs through outcome tracking.
- `pub struct ConsolidationResult` — Fragment Consolidation Result
- `pub struct CoverageEstimate` — Coverage estimation result.

## Functions
- `fn find_consolidation_groups(
    fragments: &[(String, u64, f64, bool, u32)` — By consolidating based on *outcome* (which version led to better LLM outputs), we're doing Maxwell's Demon: reducing entropy by keeping the thermodynamically "useful" variant.  # Complexity: O(N²) pai
- `fn estimate_coverage(
    selected_count: usize,
    semantic_candidates: usize,   // N₁: fragments found by SimHash similarity
    structural_candidates: usize, // N₂: fragments found by dep graph traversal
    overlap: usize,               // m: fragments found by BOTH methods
) -> CoverageEstimate` — - Zero overlap: degenerate case, falls back to union size estimate.  # Confidence Estimation  The coefficient of variation of the Chapman estimator is approximately: CV = sqrt((N₁ + 1)(N₂ + 1)(N₁ − m)

## Dependencies
- `serde::`
- `std::collections::HashMap`
