---
claim_id: 18a33f4c_epistemic_router_doc
entity: cogops_epistemic_router
status: inferred
confidence: 0.90
sources:
  - epistemic_router.py:39
  - epistemic_router.py:56
  - epistemic_router.py:88
  - epistemic_router.py:172
  - cogops.rs:170
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - epistemic_router_18a33f4c
  - cogops_18a33f4c
  - arch_cogops_epistemic_engine_a8c9d7f6
epistemic_layer: action
---

# CogOps Epistemic Router (Ingress Controller)

The epistemic router is the single entry point for all queries entering the CogOps system. It lives in the **Action layer** but decides which other layers to invoke. It is the ingress controller for the entire epistemic topology.

## Four Inspection Signals

1. **Intent** -- What does the user want? Classified into one of 13 intent types (architecture, pr_brief, code_generation, report, research, incident, audit, reuse, onboarding, test_gap, release, repair, general). Uses zero-allocation keyword scanning.

2. **Belief coverage** -- Does a relevant belief exist in the vault? Checks the belief store for entities matching the query's target modules/files.

3. **Freshness and confidence** -- Is the matching belief fresh enough? Checks `last_checked` timestamp against staleness threshold and `confidence` against minimum threshold.

4. **Risk** -- Is this a high-risk query? Audit, incident, release, and test_gap intents are automatically high-risk. Code generation for critical paths is high-risk.

## Routing Decision

Given the four signals, the router selects exactly one of the 5 canonical flows:

- **Fast Answer (Flow 1):** Belief exists, fresh, verified, low-risk
- **Verify Before Answer (Flow 2):** Belief exists but stale/unverified/risky
- **Compile On Demand (Flow 3):** No belief exists
- **Change-Driven (Flow 4):** External event trigger
- **Self-Improvement (Flow 5):** Repeated failure pattern

See [[cogops_canonical_flows_18a33f4c]] for full flow documentation.

## Implementation

The router is implemented in two layers:
- **Rust (cogops.rs:170):** Zero-allocation keyword-based intent classifier for hot-path performance
- **Python (epistemic_router.py:56):** Higher-level orchestration with belief store queries and freshness checks

## Key Relationships

- [[server_18a33f4c]] -- Receives queries from the MCP server
- [[query_refiner_18a33f4c]] -- Pre-processes queries before routing
- [[auto_index_18a33f4c]] -- Triggered by Flow 3 when no beliefs exist
- [[guardrails_18a33f4c]] -- Consulted for risk assessment in signal 4
- [[belief_compiler_18a33f4c]] -- Invoked by Flows 3, 4, 5
- [[verification_engine_18a33f4c]] -- Invoked by Flows 2, 4, 5
