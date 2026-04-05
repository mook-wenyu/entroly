---
claim_id: b9dae8g7_memory_lifecycle
entity: fragment_lifecycle
status: inferred
confidence: 0.88
sources:
  - entroly-core/src/lib.rs:349
  - entroly-core/src/lib.rs:443
  - entroly-core/src/fragment.rs:161
  - entroly-core/src/lib.rs:100
  - entroly-core/src/lib.rs:462
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - fragment_18a33f4c
  - lib_18a33f4c
  - dedup_18a33f4c
epistemic_layer: evolution
boundary_note: "Checkpoint persistence = Truth. Decay/promotion = Evolution."
---

# Fragment Lifecycle: Birth, Decay, Consolidation, Death

Every ContextFragment follows a deterministic lifecycle managed by `advance_turn()` and bounded by `max_fragments`. Understanding this lifecycle explains the memory management strategy.

## Birth: Ingestion Pipeline (lib.rs:443)

`ingest(content, source, token_count, is_pinned)` runs:
1. **Token estimation** — If token_count=0, estimates from char count using code vs. prose heuristic (non-alpha ratio > 0.4 = code = 5 chars/token, else 4)
2. **Cap check** — Rejects if fragments.len() >= max_fragments (default 10,000)
3. **ID generation** — `f{instance_hex8}_{counter_hex6}` — globally unique within process via per-instance xorshift64 seed (lib.rs:100)
4. **Dedup check** — SimHash + LSH banding. On duplicate: increment existing fragment's access_count, return early
5. **Entropy scoring** — information_score() against top-50 existing fragments (sorted by ID for determinism)
6. **Criticality** — file_criticality() + has_safety_signal(). Critical/Safety files get force-pinned
7. **Skeleton extraction** — Pattern-based structural outline for code files
8. **Dependency linking** — auto_link() in DepGraph (symbol table resolution)
9. **LSH indexing** — Insert fingerprint into multi-probe LSH tables
10. **Cache invalidation** — BFS through reverse deps with depth-weighted exponential decay

## Aging: Ebbinghaus Decay (advance_turn, lib.rs:349)

Each turn: `recency_score = exp(-decay_rate * dt)` where decay_rate = ln(2) / half_life (default 15 turns). At exactly one half-life, recency = 0.5. Fragments below `min_relevance` (default 0.05) are evicted unless pinned.

The Ebbinghaus curve means fragments lose relevance exponentially. After ~5 half-lives (75 turns), a fragment's recency is below 0.03 — effectively dead unless accessed.

## Rejuvenation

Accessing a fragment (selected by optimize()) resets turn_last_accessed and increments access_count, restarting the decay clock. Frequently-selected fragments can survive indefinitely through repeated access, creating a natural Darwinian selection pressure.

## Consolidation: Maxwell's Demon (lib.rs:400)

Every 5 turns when fragments > 10: find groups of near-duplicate fragments (Hamming <= 8), pick winner by highest feedback multiplier, transfer access counts, evict losers. This is entropy reduction — the "demon" merges redundant information, freeing capacity for new fragments.

## Death: Eviction

Three paths to eviction:
1. **Decay below threshold** — recency_score < min_relevance and not pinned
2. **Consolidation loser** — absorbed by a better near-duplicate
3. **Cap pressure** — max_fragments reached, new ingest rejected (not eviction of existing)

Pinned fragments are immortal — they survive decay and consolidation. Safety/Critical files are auto-pinned at ingestion.

## Related Modules

- **Modules:** [[cache_18a33f4c]], [[checkpoint_18a33f4c]], [[dedup_18a33f4c]], [[fragment_18a33f4c]], [[lib_18a33f4c]], [[long_term_memory_18a33f4c]]
- **Related architectures:** [[arch_dedup_hierarchy_e6a7b5d4]], [[arch_optimize_pipeline_a7c2e1f0]], [[arch_rust_python_boundary_c4e5f3b2]]
