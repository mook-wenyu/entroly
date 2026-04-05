---
claim_id: 18a33f4c_canonical_flows
entity: cogops_canonical_flows
status: inferred
confidence: 0.90
sources:
  - cogops.rs:170
  - cogops.rs:186
  - epistemic_router.py:56
  - epistemic_router.py:88
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - cogops_18a33f4c
  - epistemic_router_18a33f4c
  - arch_cogops_epistemic_engine_a8c9d7f6
epistemic_layer: action
---

# CogOps Canonical Flows

Every use case in the system maps to exactly one of these five flows. The [[epistemic_router_18a33f4c]] selects the flow at ingress time.

## Flow 1: Fast Answer

**Path:** Query -> Router -> Belief -> Action

The happy path. A belief exists, is fresh (not stale), verified, and the query is low-risk. The router reads directly from the belief store and produces an action output without touching Truth or Verification.

**When:** Belief exists AND confidence >= threshold AND last_checked recent AND risk = low.

**Modules involved:** [[query_refiner_18a33f4c]], [[epistemic_router_18a33f4c]], [[cognitive_bus_18a33f4c]], [[knapsack_18a33f4c]]

## Flow 2: Verify Before Answer

**Path:** Query -> Router -> Belief -> Verification -> Action

A belief exists but is stale, low-confidence, or the query is high-risk. The verification layer challenges the belief before using it.

**When:** Belief exists AND (stale OR low confidence OR risk = high).

**Modules involved:** [[query_refiner_18a33f4c]], [[epistemic_router_18a33f4c]], [[anomaly_18a33f4c]], [[health_18a33f4c]], [[guardrails_18a33f4c]], [[knapsack_18a33f4c]]

## Flow 3: Compile On Demand

**Path:** Query -> Router -> Truth -> Belief -> Verification -> Action

No belief exists for the query. The system must read reality (Truth), compile a new belief, verify it, then act.

**When:** No matching belief exists.

**Modules involved:** [[query_refiner_18a33f4c]], [[sast_18a33f4c]], [[depgraph_18a33f4c]], [[skeleton_18a33f4c]], [[belief_compiler_18a33f4c]], [[verification_engine_18a33f4c]], [[knapsack_18a33f4c]]

## Flow 4: Change-Driven Pipeline

**Path:** Event -> Truth -> Belief -> Verification -> Action

Triggered by external events (PR, commit, incident). The change listener detects the event, Truth re-reads affected files, beliefs are recompiled, verified, and actions generated.

**When:** Git event, file change, or incident trigger.

**Modules involved:** [[change_listener_18a33f4c]], [[change_pipeline_18a33f4c]], [[sast_18a33f4c]], [[depgraph_18a33f4c]], [[belief_compiler_18a33f4c]], [[verification_engine_18a33f4c]], [[flow_orchestrator_18a33f4c]]

## Flow 5: Self-Improvement Loop

**Path:** Failures -> Verification -> Evolution -> Belief

When the system repeatedly fails at a task type, verification detects the pattern, evolution synthesizes a new skill or tunes parameters, and updated beliefs are compiled.

**When:** Repeated failures detected in verification metrics.

**Modules involved:** [[anomaly_18a33f4c]], [[verification_engine_18a33f4c]], [[skill_engine_18a33f4c]], [[autotune_18a33f4c]], [[evolution_logger_18a33f4c]], [[belief_compiler_18a33f4c]]

## Routing Matrix

| Belief exists? | Fresh? | Verified? | Risk? | Flow |
|---|---|---|---|---|
| Yes | Yes | Yes | Low | 1 - Fast Answer |
| Yes | Yes | Yes | High | 2 - Verify Before Answer |
| Yes | No | Any | Any | 2 - Verify Before Answer |
| Yes | Yes | No | Any | 2 - Verify Before Answer |
| No | - | - | Any | 3 - Compile On Demand |
| Event | - | - | - | 4 - Change-Driven Pipeline |
| Failures | - | - | - | 5 - Self-Improvement Loop |

## Intent Classification Table

| Intent | Default Flow | Override Condition |
|---|---|---|
| architecture | 1 | No belief -> 3 |
| pr_brief | 4 | Always change-driven |
| code_generation | 1 | No belief -> 3 |
| report | 1 | Stale -> 2 |
| research | 3 | Always compiles fresh |
| incident | 4 | Always change-driven |
| audit | 2 | Always verifies |
| reuse | 1 | No belief -> 3 |
| onboarding | 1 | No belief -> 3 |
| test_gap | 2 | Always verifies |
| release | 2 | Always verifies |
| repair | 5 | Always self-improvement |
| general | 1 | No belief -> 3 |
