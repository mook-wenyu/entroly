---
claim_id: 18a336a72be1af542bf94554
entity: query_persona
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\query_persona.rs:73
  - entroly-wasm\src\query_persona.rs:79
  - entroly-wasm\src\query_persona.rs:86
  - entroly-wasm\src\query_persona.rs:120
  - entroly-wasm\src\query_persona.rs:133
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: query_persona

**LOC:** 842

## Entities
- `pub struct RbfKernel` (struct)
- `pub fn new(sigma: f32) -> Self` (function)
- `pub fn silverman(particles: &[Vec<f32>]) -> Self` (function)
- `pub fn eval(&self, x: &[f32], y: &[f32]) -> f32` (function)
- `pub struct ParticleCloud` (struct)
- `pub fn new(dim: usize, max_particles: usize) -> Self` (function)
- `pub fn add_particle(&mut self, x: &[f32])` (function)
- `pub fn affinity(&self, t: &[f32], kernel: &RbfKernel) -> f32` (function)
- `pub fn mmd_squared(&self, other: &ParticleCloud, kernel: &RbfKernel) -> f32` (function)
- `pub fn effective_support(&self, kernel: &RbfKernel) -> f32` (function)
- `pub fn merge(&mut self, other: &ParticleCloud)` (function)
- `pub struct QueryArchetype` (struct)
- `pub fn new(id: String, default_weights: [f64; 4], tick: u64) -> Self` (function)
- `pub fn affinity(&self, query_features: &[f32]) -> f32` (function)
- `pub fn record_result(&mut self, gradient: &[f64; 4], success: bool)` (function)
- `pub fn update_kernel(&mut self)` (function)
- `pub struct PitmanYorProcess` (struct)
- `pub fn new(alpha: f32, discount: f32) -> Self` (function)
- `pub fn new_archetype_prob(&self, n_existing: usize) -> f32` (function)
- `pub fn existing_weight(&self, n_k: u64) -> f32` (function)
- `pub fn update_weights(&self, archetypes: &mut [QueryArchetype])` (function)
- `pub fn build_query_features(` (function)
- `pub struct QueryPersonaManifold` (struct)
- `pub fn new(` (function)
- `pub fn population(&self) -> usize` (function)
- `pub fn assign(&mut self, query_features: &[f32]) -> (String, [f64; 4], bool)` (function)
- `pub fn record_result(` (function)
- `pub fn get_weights(&self, archetype_id: &str) -> [f64; 4]` (function)
- `pub fn lifecycle_tick(&mut self)` (function)
- `pub fn stats(&self) -> ManifoldStats` (function)
- `fn birth_archetype(&mut self, query_features: &[f32]) -> String` (function)
- `fn check_fusion(&mut self)` (function)
- `pub struct ManifoldStats` (struct)
- `pub struct ArchetypeInfo` (struct)
- `fn make_features(primary: usize, vagueness: f32) -> Vec<f32>` (function)
- `fn default_weights() -> [f64; 4]` (function)
- `fn test_rbf_kernel_self()` (function)
- `fn test_rbf_kernel_distance()` (function)
- `fn test_birth_on_empty()` (function)
- `fn test_repeated_assignment_converges()` (function)
- `fn test_different_queries_can_birth()` (function)
- `fn test_death_by_decay()` (function)
- `fn test_fusion_identical_archetypes()` (function)
- `fn test_per_archetype_weight_learning()` (function)
- `fn test_mmd_identical_clouds()` (function)
- `fn test_build_query_features()` (function)
- `fn test_manifold_stats()` (function)
- `fn test_max_archetypes_cap()` (function)
- `fn test_pitman_yor_probability()` (function)
