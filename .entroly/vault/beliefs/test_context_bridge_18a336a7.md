---
claim_id: 18a336a7310f9cd4312732d4
entity: test_context_bridge
status: stale
confidence: 0.75
sources:
  - tests\test_context_bridge.py:30
  - tests\test_context_bridge.py:32
  - tests\test_context_bridge.py:38
  - tests\test_context_bridge.py:45
  - tests\test_context_bridge.py:61
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_context_bridge

**LOC:** 438

## Entities
- `class TestLODManager:` (class)
- `def test_register_sets_dormant(self)` (function)
- `def test_register_with_parent_increments_depth(self)` (function)
- `def test_hysteresis_prevents_premature_transition(self)` (function)
- `def test_dormant_to_active_promotion(self)` (function)
- `def test_active_to_dormant_demotion(self)` (function)
- `def test_saturation_alert(self)` (function)
- `def test_unregister_reparents_children(self)` (function)
- `def test_fibonacci_hash_scatter(self)` (function)
- `def test_budget_weights(self)` (function)
- `class TestNkbeAllocator:` (class)
- `def test_single_agent_gets_full_budget(self)` (function)
- `def test_two_equal_agents_roughly_equal_split(self)` (function)
- `def test_higher_weight_gets_more(self)` (function)
- `def test_minimum_budget_respected(self)` (function)
- `def test_reinforce_adjusts_weights(self)` (function)
- `class TestCognitiveBus:` (class)
- `def test_publish_and_drain(self)` (function)
- `def test_novelty_dedup(self)` (function)
- `def test_stats(self)` (function)
- `class TestHCCEngine:` (class)
- `def test_all_reference_when_tight_budget(self)` (function)
- `def test_high_relevance_gets_full(self)` (function)
- `def test_marginal_gain_ordering(self)` (function)
- `def test_retention_values_correct(self)` (function)
- `class TestAutoTune:` (class)
- `def test_initial_weights(self)` (function)
- `def test_positive_outcome_reinforces(self)` (function)
- `def test_negative_outcome_decreases(self)` (function)
- `def test_drift_penalty_prevents_runaway(self)` (function)
- `def test_polyak_averaging_is_slower(self)` (function)
- `def test_ema_outcome_tracking(self)` (function)
- `class TestMemoryBridge:` (class)
- `def test_graceful_degradation(self)` (function)
- `def test_salience_mapping(self)` (function)
- `class TestCompression:` (class)
- `def test_skeleton_keeps_definitions(self)` (function)
- `def process_file(path)` (function)
- `def test_reference_is_one_line(self)` (function)
- `def test_skeleton_keeps_key_markers(self)` (function)
- `class TestIntegrationPipeline:` (class)
- `def test_lod_nkbe_integration(self)` (function)
- `def test_hcc_autotune_feedback_loop(self)` (function)
- `def test_bus_lod_cron_pipeline(self)` (function)
