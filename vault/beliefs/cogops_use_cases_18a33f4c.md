---
claim_id: 18a33f4c_use_cases
entity: cogops_use_cases
status: inferred
confidence: 0.85
sources:
  - cogops.rs:170
  - epistemic_router.py:56
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - cogops_canonical_flows_18a33f4c
  - cogops_epistemic_router_18a33f4c
epistemic_layer: action
---

# CogOps Use Case Map (22 Use Cases)

Every use case maps to exactly one canonical flow. The [[cogops_epistemic_router_18a33f4c]] classifies the intent and routes accordingly.

## Architecture Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 1 | "Explain the cache architecture" | 1 - Fast Answer | [[query_refiner_18a33f4c]], [[cognitive_bus_18a33f4c]] |
| 2 | "How does the scoring pipeline work?" | 1 - Fast Answer | [[query_refiner_18a33f4c]], [[knapsack_18a33f4c]] |
| 3 | "Map the dependency graph of module X" | 3 - Compile On Demand | [[sast_18a33f4c]], [[depgraph_18a33f4c]], [[belief_compiler_18a33f4c]] |

## PR Brief Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 4 | "Summarize this PR's changes" | 4 - Change-Driven | [[change_listener_18a33f4c]], [[change_pipeline_18a33f4c]] |
| 5 | "What's the blast radius of this diff?" | 4 - Change-Driven | [[depgraph_18a33f4c]], [[change_pipeline_18a33f4c]] |

## Code Generation Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 6 | "Generate a test for cache.rs" | 1 - Fast Answer | [[knapsack_18a33f4c]], [[context_bridge_18a33f4c]] |
| 7 | "Implement a new endpoint" | 3 - Compile On Demand | [[sast_18a33f4c]], [[skeleton_18a33f4c]], [[belief_compiler_18a33f4c]] |

## Report Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 8 | "Show me module health dashboard" | 1 - Fast Answer | [[dashboard_18a33f4c]], [[health_18a33f4c]] |
| 9 | "Generate coverage report" | 2 - Verify Before Answer | [[health_18a33f4c]], [[verification_engine_18a33f4c]] |

## Research Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 10 | "Find all usages of EntrolyEngine" | 3 - Compile On Demand | [[sast_18a33f4c]], [[query_refiner_18a33f4c]] |
| 11 | "What patterns does this codebase use?" | 3 - Compile On Demand | [[skeleton_18a33f4c]], [[belief_compiler_18a33f4c]] |

## Incident Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 12 | "Production error in proxy module" | 4 - Change-Driven | [[anomaly_18a33f4c]], [[proxy_18a33f4c]] |
| 13 | "Memory leak investigation" | 4 - Change-Driven | [[health_18a33f4c]], [[utilization_18a33f4c]] |

## Audit Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 14 | "Audit security of guardrails module" | 2 - Verify Before Answer | [[guardrails_18a33f4c]], [[verification_engine_18a33f4c]] |
| 15 | "Check dependency vulnerabilities" | 2 - Verify Before Answer | [[depgraph_18a33f4c]], [[anomaly_18a33f4c]] |

## Reuse and Onboarding Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 16 | "Find reusable utility functions" | 1 - Fast Answer | [[lib_18a33f4c]], [[semantic_dedup_18a33f4c]] |
| 17 | "Onboard me to the knapsack module" | 1 - Fast Answer | [[knapsack_18a33f4c]], [[context_bridge_18a33f4c]] |

## Test Gap Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 18 | "Which modules lack test coverage?" | 2 - Verify Before Answer | [[health_18a33f4c]], [[verification_engine_18a33f4c]] |
| 19 | "Generate missing tests for cache" | 2 - Verify Before Answer | [[cache_18a33f4c]], [[benchmark_harness_18a33f4c]] |

## Release Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 20 | "Pre-release checklist for v0.7" | 2 - Verify Before Answer | [[guardrails_18a33f4c]], [[health_18a33f4c]] |

## Repair Intent

| # | Use Case | Flow | Key Modules |
|---|---|---|---|
| 21 | "Fix recurring context overflow failures" | 5 - Self-Improvement | [[autotune_18a33f4c]], [[skill_engine_18a33f4c]] |
| 22 | "Improve query relevance scoring" | 5 - Self-Improvement | [[resonance_18a33f4c]], [[evolution_logger_18a33f4c]] |
