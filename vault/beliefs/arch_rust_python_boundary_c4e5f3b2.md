---
claim_id: c4e5f3b2_rust_python_boundary
entity: rust_python_boundary
status: inferred
confidence: 0.90
sources:
  - entroly-core/src/lib.rs:8
  - entroly-core/src/query.rs:305
  - entroly-core/src/cogops.rs:1
  - entroly/query_refiner.py:1
  - entroly/context_bridge.py:18
  - entroly-core/src/nkbe.rs:52
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - lib_18a33f4c
  - query_refiner_18a33f4c
  - context_bridge_18a33f4c
epistemic_layer: action
boundary_note: "FFI bridge = Action. Type contracts = Truth."
---

# Rust/Python Boundary: The PyO3 Contract

Entroly follows a strict architectural principle: **all computation in Rust, all I/O in Python**. This belief documents the boundary surface and the rationale.

## The Rule

- Rust: entropy scoring, knapsack optimization, SimHash, LSH, dependency graphs, PRISM weight learning, causal inference, resonance tracking, conversation pruning
- Python: MCP protocol handling, LLM API calls (OpenAI/Anthropic), file I/O, HTTP serving, configuration loading

## PyO3 Binding Surface

Three Rust types are exposed as Python classes via `#[pyclass]`:

1. **`EntrolyEngine`** (lib.rs:72) — The primary orchestrator. Methods: `ingest()`, `optimize()`, `record_success()`, `record_failure()`, `advance_turn()`, `health_report()`, etc. All return `PyObject` (usually `PyDict`).

2. **`NkbeAllocator`** (nkbe.rs:52) — Multi-agent budget allocation. Separate class because it manages multiple agents, each with their own fragment sets.

3. **`CogOpsEngine`** (cogops.rs, exposed via lib.rs) — Epistemic engine for belief compilation, verification, and change-driven flows.

Four Rust functions are exposed as standalone `#[pyfunction]`:

- `py_analyze_query()` (query.rs:311) — Query vagueness + key term extraction
- `py_refine_heuristic()` (query.rs:328) — Deterministic query grounding

## Graceful Degradation Pattern

Python code always wraps Rust imports in try/except (query_refiner.py:25):
```
try:
    from entroly_core import py_analyze_query
except ImportError:
    def py_analyze_query(...):  # pure-Python fallback
```

This means the system works (degraded) without the compiled Rust extension. The fallback implementations are intentionally simple — they preserve the API contract but lose the performance and sophistication of the Rust implementation.

## Data Serialization at the Boundary

All cross-boundary data is serialized as Python dicts (PyDict). The Rust side constructs dicts item-by-item via `result.set_item()` (lib.rs:596-608). No Pydantic models or protobuf — raw dicts for minimal overhead.

For EGSC cache, Rust serializes results to JSON strings (serde_json) and deserializes on cache hit. This is the only place where JSON enters the Rust side.

## Why This Split Matters

1. **50x performance**: Shannon entropy, SimHash, knapsack DP all run in tight Rust loops with stack-allocated histograms and zero-copy string slicing
2. **No Python GIL contention**: Rayon parallelism in cross_fragment_redundancy (entropy.rs:387) works because the computation is entirely in Rust
3. **Deployment flexibility**: The Python layer can be MCP server, HTTP API, CLI, or library — the Rust core is transport-agnostic

## Related Modules

- **Modules:** [[autotune_18a33f4c]], [[belief_compiler_18a33f4c]], [[checkpoint_18a33f4c]], [[context_bridge_18a33f4c]], [[lib_18a33f4c]], [[proxy_18a33f4c]], [[query_refiner_18a33f4c]], [[server_18a33f4c]]
- **Related architectures:** [[arch_concurrency_model_ecf3db0j]], [[arch_memory_lifecycle_b9dae8g7]], [[arch_query_resolution_flow_fda4ec1k]]
