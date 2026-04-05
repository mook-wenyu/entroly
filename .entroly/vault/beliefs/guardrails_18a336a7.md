---
claim_id: 18a336a72b1157c82b28edc8
entity: guardrails
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\guardrails.rs:24
  - entroly-wasm\src\guardrails.rs:36
  - entroly-wasm\src\guardrails.rs:142
  - entroly-wasm\src\guardrails.rs:207
  - entroly-wasm\src\guardrails.rs:224
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: guardrails

**LOC:** 570

## Entities
- `pub enum Criticality` (enum)
- `pub fn file_criticality(path: &str) -> Criticality` (function)
- `pub fn has_safety_signal(content: &str) -> bool` (function)
- `pub(crate) fn criticality_boost(criticality: Criticality) -> f64` (function)
- `pub enum TaskType` (enum)
- `pub fn classify(query: &str) -> TaskType` (function)
- `pub fn budget_multiplier(&self) -> f64` (function)
- `pub fn compute_ordering_priority(` (function)
- `pub struct FeedbackTracker` (struct)
- `pub fn new() -> Self` (function)
- `pub fn record_success(&mut self, fragment_ids: &[String])` (function)
- `pub fn record_failure(&mut self, fragment_ids: &[String])` (function)
- `fn record_reward_signal(&mut self, fragment_ids: &[String], reward: f64)` (function)
- `pub fn variance(&self, fragment_id: &str) -> f64` (function)
- `pub fn visit_count(&self, fragment_id: &str) -> u32` (function)
- `pub fn welford_mean(&self, fragment_id: &str) -> f64` (function)
- `pub fn adaptive_exploration_rate(&self, alpha_0: f64) -> f64` (function)
- `pub fn ucb_score(&self, fragment_id: &str, alpha_0: f64) -> f64` (function)
- `pub fn total_observations(&self) -> u64` (function)
- `pub fn learned_value(&self, fragment_id: &str) -> f64` (function)
- `fn test_critical_files()` (function)
- `fn test_safety_signals()` (function)
- `fn test_task_classification()` (function)
- `fn test_feedback_tracker()` (function)
- `fn test_ucb_variance_tracking()` (function)
- `fn test_raven_ucb_convergence()` (function)
