---
claim_id: 18a336a72a9965882ab0fb88
entity: cognitive_bus
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\cognitive_bus.rs:59
  - entroly-wasm\src\cognitive_bus.rs:87
  - entroly-wasm\src\cognitive_bus.rs:107
  - entroly-wasm\src\cognitive_bus.rs:132
  - entroly-wasm\src\cognitive_bus.rs:146
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: cognitive_bus

**LOC:** 886

## Entities
- `pub enum EventType` (enum)
- `fn from_str(s: &str) -> Self` (function)
- `fn as_str(&self) -> &str` (function)
- `pub struct BusEvent` (struct)
- `pub struct PrioritizedEvent` (struct)
- `fn eq(&self, other: &Self) -> bool` (function)
- `fn partial_cmp(&self, other: &Self) -> Option<Ordering>` (function)
- `fn cmp(&self, other: &Self) -> Ordering` (function)
- `pub struct WelfordAccumulator` (struct)
- `fn new() -> Self` (function)
- `fn update(&mut self, x: f64) -> (f64, f64)` (function)
- `fn is_spike(&self, x: f64, k: f64) -> bool` (function)
- `pub struct PoissonRate` (struct)
- `fn new() -> Self` (function)
- `fn observe(&mut self, current_count: u64, current_time: f64)` (function)
- `fn kl_surprise(&self, observed_rate: f64) -> f64` (function)
- `pub struct Subscriber` (struct)
- `fn new(agent_id: &str) -> Self` (function)
- `fn compute_novelty(&self, event_hash: u64) -> f64` (function)
- `fn compute_mutual_info(&self, event_hash: u64) -> f64` (function)
- `fn compute_priority(&mut self, event: &BusEvent, current_time: f64) -> f64` (function)
- `fn check_spike(&mut self, priority: f64) -> bool` (function)
- `fn enqueue(&mut self, event: BusEvent, priority: f64)` (function)
- `fn drain(&mut self, limit: usize) -> Vec<BusEvent>` (function)
- `fn is_subscribed(&self, event_type: &EventType) -> bool` (function)
- `pub struct CognitiveBus` (struct)
- `pub fn new(memory_salience_threshold: f64) -> Self` (function)
- `pub fn subscribe(&mut self, agent_id: &str, event_types: Vec<String>)` (function)
- `pub fn unsubscribe(&mut self, agent_id: &str)` (function)
- `pub fn set_task_context(&mut self, agent_id: &str, task_text: &str)` (function)
- `pub fn tick(&mut self)` (function)
- `pub fn set_tick(&mut self, tick: f64)` (function)
- `pub fn publish(` (function)
- `pub fn drain(&mut self, agent_id: &str, limit: usize) -> Vec<serde_json::Value>` (function)
- `pub fn drain_memory_bridge(&mut self) -> Vec<serde_json::Value>` (function)
- `pub fn queue_depth(&self, agent_id: &str) -> usize` (function)
- `pub fn stats(&self) -> serde_json::Value` (function)
- `pub fn drain_raw(&mut self, agent_id: &str, limit: usize) -> Vec<BusEvent>` (function)
- `pub fn drain_memory_bridge_raw(&mut self) -> Vec<BusEvent>` (function)
- `fn test_welford_basic()` (function)
- `fn test_welford_needs_minimum_samples()` (function)
- `fn test_poisson_rate_kl()` (function)
- `fn test_subscriber_novelty_first_event()` (function)
- `fn test_subscriber_novelty_duplicate()` (function)
- `fn test_subscriber_mutual_info_no_task()` (function)
- `fn test_subscriber_mutual_info_same_task()` (function)
- `fn test_bus_publish_and_drain()` (function)
- `fn test_bus_dedup_prevents_duplicate()` (function)
- `fn test_bus_memory_bridge()` (function)
- `fn test_bus_type_filtering()` (function)
- `fn test_bus_no_self_routing()` (function)
- `fn test_bus_task_context_boosts_priority()` (function)
- `fn test_bus_stats_counters()` (function)
