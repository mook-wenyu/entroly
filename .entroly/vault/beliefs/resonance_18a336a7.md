---
claim_id: 18a336a72bf667a02c0dfda0
entity: resonance
status: stale
confidence: 0.75
sources:
  - entroly-wasm\src\resonance.rs:61
  - entroly-wasm\src\resonance.rs:64
  - entroly-wasm\src\resonance.rs:73
  - entroly-wasm\src\resonance.rs:78
  - entroly-wasm\src\resonance.rs:91
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: resonance

**LOC:** 712

## Entities
- `pub struct PairKey` (struct)
- `fn new(a: &str, b: &str) -> Self` (function)
- `fn to_key_string(&self) -> String` (function)
- `fn from_key_string(s: &str) -> Option<Self>` (function)
- `pub fn serialize<S>(map: &HashMap<PairKey, super::ResonanceEntry>, serializer: S) -> Result<S::Ok, S::Error>` (function)
- `pub fn deserialize<'de, D>(deserializer: D) -> Result<HashMap<PairKey, super::ResonanceEntry>, D::Error>` (function)
- `pub struct PairKeyMapVisitor` (struct)
- `fn expecting(&self, f: &mut fmt::Formatter) -> fmt::Result` (function)
- `fn visit_map<M: MapAccess<'de>>(self, mut access: M) -> Result<Self::Value, M::Error>` (function)
- `pub struct ResonanceEntry` (struct)
- `pub struct ResonanceMatrix` (struct)
- `fn default() -> Self` (function)
- `pub fn new() -> Self` (function)
- `pub fn record_outcome(&mut self, fragment_ids: &[String], reward: f64, current_turn: u32)` (function)
- `pub fn resonance_bonus(&self, candidate_id: &str, selected_ids: &[&str]) -> f64` (function)
- `pub fn batch_resonance_bonuses(` (function)
- `pub fn decay_tick(&mut self)` (function)
- `pub fn len(&self) -> usize` (function)
- `pub fn is_empty(&self) -> bool` (function)
- `pub fn top_pairs(&self, top_k: usize) -> Vec<(String, String, f64, u32)>` (function)
- `pub fn mean_strength(&self) -> f64` (function)
- `pub struct ConsolidationResult` (struct)
- `pub fn find_consolidation_groups(` (function)
- `pub struct CoverageEstimate` (struct)
- `pub fn estimate_coverage(` (function)
- `fn test_resonance_symmetric()` (function)
- `fn test_resonance_positive_reinforcement()` (function)
- `fn test_resonance_negative_suppression()` (function)
- `fn test_resonance_cold_start_zero()` (function)
- `fn test_resonance_decay()` (function)
- `fn test_resonance_multiple_partners()` (function)
- `fn test_consolidation_near_duplicates()` (function)
- `fn test_consolidation_pinned_exempt()` (function)
- `fn test_coverage_high_overlap()` (function)
- `fn test_coverage_low_overlap()` (function)
- `fn test_coverage_zero_selected()` (function)
- `fn test_coverage_monotone_in_overlap()` (function)
- `fn test_chapman_estimator_accuracy()` (function)
