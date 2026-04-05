---
claim_id: ecf3db0j_concurrency
entity: concurrency_model
status: inferred
confidence: 0.85
sources:
  - entroly-core/src/entropy.rs:387
  - entroly-core/src/lib.rs:64
  - entroly-core/src/lib.rs:269
  - entroly-core/src/cognitive_bus.rs:52
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - lib_18a33f4c
  - entropy_18a33f4c
  - cognitive_bus_18a33f4c
epistemic_layer: action
boundary_note: "Thread pools = Action. Resource scheduling = Belief."
---

# Concurrency Model: Single-Threaded Engine + Rayon Parallelism

Entroly's concurrency model is deliberately simple at the API level but uses parallelism internally where it matters.

## Engine-Level: Single-Threaded Ownership

`EntrolyEngine` is a `#[pyclass]` with `&mut self` methods. PyO3 holds the GIL during calls, making all engine mutations single-threaded. There is no internal locking, no Arc/Mutex, no async. This is by design: context optimization is a request-response operation, not a long-lived concurrent service.

## Multi-Instance Isolation

Multiple `EntrolyEngine` instances can coexist in one process. Each gets a unique `instance_id` via `INSTANCE_SEED` (global AtomicU64, lib.rs:64). Fragment IDs use format `f{instance_hex}_{counter_hex}`, guaranteeing disjoint ID spaces. No shared mutable state between engines.

## Internal Parallelism: Rayon

`cross_fragment_redundancy()` (entropy.rs:387) parallelizes n-gram extraction across other fragments when `others.len() > 10` using `rayon::par_iter()`. This is safe because it operates on immutable borrowed slices — no shared mutable state.

This is the ONLY use of Rayon in the codebase. The decision to not parallelize other operations (knapsack DP, LSH queries, resonance scoring) is deliberate: for N<10K fragments, single-threaded performance is sufficient and avoids thread pool overhead.

## Cognitive Bus: Async-Ready Architecture

The CognitiveBus (cognitive_bus.rs) has an inherently concurrent design — per-subscriber priority queues, Welford spike detection for immediate broadcast, event routing. However, the current implementation is synchronous (no tokio, no async). The per-agent queue structure (MAX_QUEUE_PER_AGENT=256, BinaryHeap per subscriber) is designed to be upgraded to async channels without structural changes.

## PRNG: Deterministic Exploration

Exploration uses xorshift64 PRNG seeded from instance_id (lib.rs:269). No thread-local random, no system entropy. This means exploration is deterministic given the same seed, which is important for reproducibility in benchmarking and debugging.

## Related Modules

- **Modules:** [[channel_18a33f4c]], [[cognitive_bus_18a33f4c]], [[entropy_18a33f4c]], [[lib_18a33f4c]], [[server_18a33f4c]]
- **Related architectures:** [[arch_information_theory_stack_d5f6a4c3]], [[arch_optimize_pipeline_a7c2e1f0]], [[arch_rust_python_boundary_c4e5f3b2]]
