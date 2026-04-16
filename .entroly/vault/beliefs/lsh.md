---
claim_id: 99c224a8-1632-40ef-915c-664e3d7d8858
entity: lsh
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/lsh.rs:123
  - entroly-core/src/lsh.rs:192
last_checked: 2026-04-14T04:12:29.646258+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: lsh

**Language:** rust
**Lines of code:** 314

## Types
- `pub struct LshIndex` — Multi-Probe LSH Index for sub-linear SimHash similarity search.  Public API: - `insert(fp, idx)` — called on every `ingest()` - `remove(fp, idx)` — called on eviction / dedup replacement - `query(fp) 
- `pub struct ContextScorer` —  Combines similarity (Hamming-based), recency (Ebbinghaus decay), and entropy (information density) into a single relevance score.  Ported from ebbiforge-core/src/memory/lsh.rs::ContextScorer, adapted

## Dependencies
- `std::collections::HashMap`
