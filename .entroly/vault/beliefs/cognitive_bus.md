---
claim_id: c53f512e-a06f-4dbf-87db-257d7bdee4c2
entity: cognitive_bus
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/cognitive_bus.rs:134
  - entroly-core/src/cognitive_bus.rs:440
  - entroly-core/src/cognitive_bus.rs:61
last_checked: 2026-04-14T04:12:29.561073+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: cognitive_bus

**Language:** rust
**Lines of code:** 898

## Types
- `pub struct BusEvent` — An event published on the cognitive bus.
- `pub struct CognitiveBus` — - Hippocampus memory (salience-based remember/recall bridge) - NKBE allocator (events influence budget reallocation)  Memory-aware routing: - Events with salience > threshold are flagged for hippocamp
- `pub enum EventType` — Event types routable on the cognitive bus. Maps to agentOS 25 event types, grouped into 4 zones.

## Dependencies
- `crate::dedup::`
- `pyo3::prelude::`
- `pyo3::types::PyDict`
- `std::cmp::Ordering`
- `std::collections::`
