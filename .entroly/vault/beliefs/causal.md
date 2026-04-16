---
claim_id: 64c40083-0af2-4b61-a846-c05c333387dc
entity: causal
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/causal.rs:154
  - entroly-core/src/causal.rs:175
last_checked: 2026-04-14T04:12:29.552123+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: causal

**Language:** rust
**Lines of code:** 1066

## Types
- `pub struct CausalStats` — Statistics for observability.
- `pub struct CausalContextGraph` — Causal Context Graph — learns fragment causal effects via natural experiments.  Uses the exploration mechanism as an instrumental variable to separate true causal effects from selection bias, discover

## Dependencies
- `serde::`
- `std::collections::`
