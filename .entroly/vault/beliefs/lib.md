---
claim_id: 32c7fcde-3b62-4cfc-9351-580699c15297
entity: lib
status: inferred
confidence: 0.75
sources:
  - entroly-core/src/lib.rs:73
  - entroly-core/src/lib.rs:3764
  - entroly-core/src/lib.rs:3765
  - entroly-core/src/lib.rs:3766
  - entroly-core/src/lib.rs:3767
  - entroly-core/src/lib.rs:3768
  - entroly-core/src/lib.rs:3769
  - entroly-core/src/lib.rs:3770
  - entroly-core/src/lib.rs:3778
  - entroly-core/src/lib.rs:3784
last_checked: 2026-04-14T04:12:29.645232+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: lib

**Language:** rust
**Lines of code:** 4520

## Types
- `pub struct EntrolyEngine` — The core engine that orchestrates all subsystems.  Modeled after ebbiforge-core HippocampusEngine: ingest → SimHash → dedup check → entropy score → store optimize → Ebbinghaus decay → knapsack DP → ra

## Functions
- `fn default_max_fragments() -> usize`
- `fn default_w_recency() -> f64`
- `fn default_w_frequency() -> f64`
- `fn default_w_semantic() -> f64`
- `fn default_w_entropy() -> f64`
- `fn default_gradient_temperature() -> f64`
- `fn default_rng_state() -> u64`
- `fn py_shannon_entropy(text: &str) -> f64` — Compute Shannon entropy of a text string (bits per character).
- `fn py_normalized_entropy(text: &str) -> f64` — Compute normalized Shannon entropy [0, 1].
- `fn py_boilerplate_ratio(text: &str) -> f64` — Compute boilerplate ratio [0, 1].
- `fn py_renyi_entropy_2(text: &str) -> f64` — Compute Rényi entropy of order 2 (collision entropy). More sensitive to concentrated probability mass than Shannon entropy.
- `fn py_entropy_divergence(text: &str) -> f64` — Shannon–Rényi divergence: H₁(X) - H₂(X). High divergence indicates noise or encoded data, not useful context.
- `fn py_simhash(text: &str) -> u64` — Compute 64-bit SimHash fingerprint.
- `fn py_hamming_distance(a: u64, b: u64) -> u32` — Compute Hamming distance between two fingerprints.
- `fn py_information_score(text: &str, other_fragments: Vec<String>) -> f64` — Compute information density score [0, 1].
- `fn py_scan_content(content: &str, source: &str) -> String` — Scan content for security vulnerabilities — returns JSON-encoded SastReport.
- `fn py_analyze_query(
    query: &str,
    fragment_summaries: Vec<String>,
) -> (f64, Vec<String>, bool, String)`
- `fn py_refine_heuristic(query: &str, fragment_summaries: Vec<String>) -> String`
- `fn py_analyze_health_info() -> String` — Health analysis is available via engine.analyze_health() (a #[pymethod]). This standalone function is intentionally minimal.
- `fn py_prune_conversation(
    _py: Python,
    blocks: Vec<Bound<'_, PyDict>>,
    token_budget: u32,
    decay_lambda: f64,
    protect_last: usize,
) -> PyResult<String>` — Prune a conversation to fit within a token budget.  Uses multi-choice knapsack via KKT dual bisection with causal DAG coherence enforcement.  Returns JSON-encoded PruneResult.  `blocks` is a list of d
- `fn py_progressive_thresholds(
    blocks: Vec<Bound<'_, PyDict>>,
    utilization: f64,
    recency_cutoff: usize,
) -> PyResult<String>` — Progressive compression: assign resolutions based on context utilization. Returns JSON: [{index, resolution}]
- `fn py_compress_block(
    role: &str,
    content: &str,
    token_count: u32,
    resolution: &str,
    tool_name: Option<String>,
) -> String` — Compress a single block at a given resolution level. Returns the compressed text.
- `fn py_classify_block(role: &str, content: &str, tool_name: Option<String>) -> String` — Classify a conversation block by role and content. Returns: "user", "assistant", "tool_call", "tool_result", "thinking", "system"
- `fn py_cross_fragment_redundancy(text: &str, others: Vec<String>) -> f64` — Cross-fragment redundancy: how much of `text` is already covered by `others` [0,1].
- `fn py_apply_ebbinghaus_decay(
    fragments: Vec<ContextFragment>,
    current_turn: u32,
    half_life: u32,
) -> Vec<ContextFragment>` — Apply Ebbinghaus decay in-place to a list of ContextFragments. Mutates recency_score based on turns elapsed since turn_last_accessed.
- `fn py_knapsack_optimize(
    fragments: Vec<ContextFragment>,
    token_budget: u32,
) -> (Vec<ContextFragment>, HashMap<String, f64>)` — Convenience knapsack optimizer for standalone use (default weights, empty feedback). Returns (selected_fragments, stats_dict).
- `fn entroly_core(m: &Bound<'_, PyModule>) -> PyResult<()>`

## Dependencies
- `cache::CacheLookup`
- `causal::CausalContextGraph`
- `dedup::`
- `depgraph::`
- `entropy::`
- `fragment::`
- `guardrails::`
- `knapsack::`
- `knapsack_sds::`
- `prism::PrismOptimizer`
- `prism::PrismOptimizer5D`
- `pyo3::prelude::`
- `pyo3::types::PyDict`
- `query_persona::QueryPersonaManifold`
- `rayon::prelude::`
- `resonance::ResonanceMatrix`
- `serde::`
- `std::collections::`
- `std::sync::atomic::`
