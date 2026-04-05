---
claim_id: 18a336a72a7037582a87cd58
entity: causal
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\causal.rs:98
  - entroly-wasm\src\causal.rs:112
  - entroly-wasm\src\causal.rs:140
  - entroly-wasm\src\causal.rs:154
  - entroly-wasm\src\causal.rs:175
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: causal

**LOC:** 1065

## Entities
- `pub struct CausalTrace` (struct)
- `pub struct InterventionEstimate` (struct)
- `pub struct TemporalLinkEntry` (struct)
- `pub struct CausalStats` (struct)
- `pub struct CausalContextGraph` (struct)
- `fn default() -> Self` (function)
- `pub fn new() -> Self` (function)
- `pub fn record_trace(` (function)
- `pub fn gravity_bonuses(&self, candidate_ids: &[&str]) -> HashMap<String, f64>` (function)
- `pub fn temporal_bonuses(` (function)
- `pub fn decay_tick(&mut self, current_turn: u32)` (function)
- `pub fn is_empty(&self) -> bool` (function)
- `pub fn tracked_fragments(&self) -> usize` (function)
- `pub fn interventional_fragments(&self) -> usize` (function)
- `pub fn temporal_link_count(&self) -> usize` (function)
- `pub fn gravity_source_count(&self) -> usize` (function)
- `pub fn mean_causal_mass(&self) -> f64` (function)
- `pub fn top_causal_fragments(&self, n: usize) -> Vec<(String, f64, f64, f64)>` (function)
- `pub fn top_temporal_chains(&self, n: usize) -> Vec<(String, String, f64, f64)>` (function)
- `pub fn stats(&self) -> CausalStats` (function)
- `fn recompute_causal_effects(&mut self)` (function)
- `fn recompute_temporal_effects(&mut self)` (function)
- `fn recompute_gravity_field(&mut self)` (function)
- `fn evict_temporal_links(&mut self, current_turn: u32)` (function)
- `fn make_ids(names: &[&str]) -> Vec<String>` (function)
- `fn test_new_graph_is_empty()` (function)
- `fn test_single_trace_updates_estimates()` (function)
- `fn test_interventional_vs_observational_separation()` (function)
- `fn test_confounding_bias_detection()` (function)
- `fn test_temporal_links_created()` (function)
- `fn test_temporal_effect_computation()` (function)
- `fn test_gravity_bonuses_positive_effect()` (function)
- `fn test_gravity_zero_for_negative_effect()` (function)
- `fn test_temporal_bonuses_computation()` (function)
- `fn test_decay_tick_removes_stale_links()` (function)
- `fn test_base_rate_tracking()` (function)
- `fn test_circular_buffer_capacity()` (function)
- `fn test_confidence_increases_with_trials()` (function)
- `fn test_top_causal_fragments()` (function)
- `fn test_stats_consistency()` (function)
- `fn test_empty_selected_ignored()` (function)
- `fn test_nan_outcome_ignored()` (function)
- `fn test_self_links_excluded()` (function)
- `fn test_serde_roundtrip()` (function)
- `fn test_temporal_eviction_under_capacity()` (function)
