---
claim_id: db818240-28f6-429e-b51b-fdce8151c3b5
entity: architecture::entroly
status: inferred
confidence: 0.7
sources:
  - C:\Users\abhis\entroly/
last_checked: 2026-04-14T04:12:09.444114+00:00
derived_from:
  - belief_compiler
  - architecture_synthesizer
---

# Architecture: entroly

Architecture overview for `entroly`.

**Total modules:** 152
**Total LOC:** 100,754

## Module Index
- **tool** (python) — 0 types, 2 fns, 24 LOC
- **accuracy** (python) — 2 types, 3 fns, 655 LOC
- **autotune** (python) — 2 types, 9 fns, 379 LOC
- **compare** (python) — 0 types, 5 fns, 395 LOC
- **evaluate** (python) — 0 types, 7 fns, 306 LOC
- **needle_heatmap** (python) — 0 types, 4 fns, 194 LOC
- **generate_demo** (python) — 0 types, 3 fns, 416 LOC
- **anomaly** (rust) — 2 types, 4 fns, 379 LOC
- **cache** (rust) — 15 types, 0 fns, 2968 LOC
- **causal** (rust) — 2 types, 0 fns, 1066 LOC
- **channel** (rust) — 1 types, 10 fns, 1331 LOC
- **cognitive_bus** (rust) — 2 types, 0 fns, 898 LOC
- **cogops** (rust) — 7 types, 38 fns, 2324 LOC
- **conversation_pruner** (rust) — 2 types, 11 fns, 1468 LOC
- **dedup** (rust) — 1 types, 4 fns, 256 LOC
- **depgraph** (rust) — 2 types, 8 fns, 1433 LOC
- **entropy** (rust) — 0 types, 13 fns, 650 LOC
- **fragment** (rust) — 1 types, 3 fns, 268 LOC
- **guardrails** (rust) — 1 types, 4 fns, 594 LOC
- **health** (rust) — 6 types, 14 fns, 851 LOC
- **hierarchical** (rust) — 1 types, 8 fns, 750 LOC
- **knapsack** (rust) — 2 types, 8 fns, 628 LOC
- **knapsack_sds** (rust) — 2 types, 3 fns, 733 LOC
- **lib** (rust) — 1 types, 27 fns, 4520 LOC
- **lsh** (rust) — 2 types, 0 fns, 314 LOC
- **nkbe** (rust) — 3 types, 3 fns, 508 LOC
- **prism** (rust) — 3 types, 0 fns, 762 LOC
- **query** (rust) — 1 types, 10 fns, 423 LOC
- **query_persona** (rust) — 7 types, 1 fns, 843 LOC
- **resonance** (rust) — 3 types, 2 fns, 713 LOC
- **sast** (rust) — 3 types, 12 fns, 2882 LOC
- **semantic_dedup** (rust) — 1 types, 5 fns, 264 LOC
- **skeleton** (rust) — 1 types, 26 fns, 2574 LOC
- **utilization** (rust) — 2 types, 3 fns, 237 LOC
- **test_brutal** (python) — 4 types, 43 fns, 733 LOC
- **test_integration** (python) — 1 types, 71 fns, 818 LOC
- **agentskills_export** (javascript) — 0 types, 3 fns, 130 LOC
- **auto_index** (javascript) — 0 types, 9 fns, 263 LOC
- **autotune** (javascript) — 2 types, 12 fns, 628 LOC
- **checkpoint** (javascript) — 1 types, 2 fns, 109 LOC
- **cli** (javascript) — 1 types, 14 fns, 322 LOC
- **cogops** (javascript) — 5 types, 9 fns, 514 LOC
- **config** (javascript) — 1 types, 1 fns, 54 LOC
- **gateways** (javascript) — 4 types, 0 fns, 171 LOC
- **multimodal** (javascript) — 0 types, 3 fns, 65 LOC
- **repo_map** (javascript) — 0 types, 2 fns, 113 LOC
- **server** (javascript) — 2 types, 0 fns, 466 LOC
- **skills** (javascript) — 1 types, 0 fns, 125 LOC
- **value_tracker** (javascript) — 1 types, 2 fns, 182 LOC
- **vault** (javascript) — 1 types, 7 fns, 238 LOC
- **vault_observer** (javascript) — 1 types, 1 fns, 130 LOC
- **workspace** (javascript) — 1 types, 0 fns, 117 LOC
- **entroly_wasm.d** (typescript) — 1 types, 0 fns, 157 LOC
- **entroly_wasm** (javascript) — 1 types, 7 fns, 469 LOC
- **anomaly** (rust) — 2 types, 4 fns, 379 LOC
- **cache** (rust) — 15 types, 0 fns, 2968 LOC
- **causal** (rust) — 2 types, 0 fns, 1066 LOC
- **channel** (rust) — 1 types, 10 fns, 1331 LOC
- **cognitive_bus** (rust) — 2 types, 0 fns, 887 LOC
- **conversation_pruner** (rust) — 2 types, 11 fns, 1468 LOC
- **dedup** (rust) — 1 types, 4 fns, 256 LOC
- **depgraph** (rust) — 2 types, 8 fns, 1433 LOC
- **entropy** (rust) — 0 types, 11 fns, 581 LOC
- **fragment** (rust) — 1 types, 3 fns, 217 LOC
- **guardrails** (rust) — 1 types, 3 fns, 571 LOC
- **health** (rust) — 6 types, 14 fns, 851 LOC
- **hierarchical** (rust) — 1 types, 8 fns, 750 LOC
- **knapsack** (rust) — 2 types, 8 fns, 628 LOC
- **knapsack_sds** (rust) — 2 types, 3 fns, 637 LOC
- **lib** (rust) — 1 types, 1 fns, 1643 LOC
- **lsh** (rust) — 2 types, 0 fns, 314 LOC
- **nkbe** (rust) — 3 types, 3 fns, 480 LOC
- **prism** (rust) — 3 types, 0 fns, 762 LOC
- **query** (rust) — 1 types, 8 fns, 394 LOC
- **query_persona** (rust) — 7 types, 1 fns, 843 LOC
- **resonance** (rust) — 3 types, 2 fns, 713 LOC
- **sast** (rust) — 3 types, 12 fns, 2882 LOC
- **semantic_dedup** (rust) — 1 types, 5 fns, 264 LOC
- **skeleton** (rust) — 1 types, 26 fns, 2574 LOC
- **utilization** (rust) — 2 types, 3 fns, 237 LOC
- **test_autotune** (javascript) — 0 types, 2 fns, 129 LOC
- **test_wasm_e2e** (javascript) — 1 types, 4 fns, 252 LOC
- **_docker_launcher** (python) — 0 types, 1 fns, 194 LOC
- **adaptive_pruner** (python) — 2 types, 8 fns, 163 LOC
- **auto_index** (python) — 0 types, 2 fns, 569 LOC
- **autotune** (python) — 5 types, 32 fns, 1242 LOC
- **belief_compiler** (python) — 5 types, 15 fns, 701 LOC
- **benchmark_harness** (python) — 0 types, 1 fns, 120 LOC
- **cache_aligner** (python) — 1 types, 4 fns, 116 LOC
- **ccr** (python) — 1 types, 7 fns, 151 LOC
- **change_listener** (python) — 2 types, 5 fns, 239 LOC
- **change_pipeline** (python) — 5 types, 6 fns, 425 LOC
- **checkpoint** (python) — 2 types, 10 fns, 582 LOC
- **cli** (python) — 1 types, 36 fns, 3193 LOC
- **config** (python) — 1 types, 0 fns, 97 LOC
- **context_bridge** (python) — 21 types, 72 fns, 2018 LOC
- **dashboard** (python) — 1 types, 4 fns, 866 LOC
- **entroly_mcp_client** (python) — 0 types, 0 fns, 25 LOC
- **epistemic_router** (python) — 6 types, 8 fns, 663 LOC
- **evolution_daemon** (python) — 1 types, 6 fns, 279 LOC
- **evolution_logger** (python) — 2 types, 5 fns, 221 LOC
- **flow_orchestrator** (python) — 2 types, 3 fns, 470 LOC
- **agentskills** (python) — 0 types, 1 fns, 178 LOC
- **discord_gateway** (python) — 1 types, 5 fns, 161 LOC
- **langchain** (python) — 1 types, 5 fns, 132 LOC
- **slack_gateway** (python) — 1 types, 5 fns, 154 LOC
- **telegram_gateway** (python) — 1 types, 5 fns, 294 LOC
- **long_term_memory** (python) — 2 types, 9 fns, 318 LOC
- **multimodal** (python) — 2 types, 4 fns, 875 LOC
- **prefetch** (python) — 2 types, 10 fns, 367 LOC
- **provenance** (python) — 2 types, 8 fns, 185 LOC
- **proxy** (python) — 6 types, 29 fns, 2169 LOC
- **proxy_config** (python) — 1 types, 3 fns, 383 LOC
- **proxy_transform** (python) — 0 types, 18 fns, 1724 LOC
- **query_refiner** (python) — 1 types, 7 fns, 173 LOC
- **repo_map** (python) — 1 types, 2 fns, 211 LOC
- **sdk** (python) — 0 types, 2 fns, 248 LOC
- **server** (python) — 3 types, 67 fns, 2715 LOC
- **skill_engine** (python) — 7 types, 15 fns, 907 LOC
- **universal_compress** (python) — 0 types, 8 fns, 517 LOC
- **value_tracker** (python) — 1 types, 13 fns, 461 LOC
- **vault** (python) — 4 types, 13 fns, 520 LOC
- **verification_engine** (python) — 6 types, 6 fns, 500 LOC
- **demo_full_experience** (python) — 1 types, 7 fns, 788 LOC
- **demo_value** (python) — 1 types, 7 fns, 403 LOC
- **bump_version** (python) — 0 types, 1 fns, 50 LOC
- **extractor** (python) — 0 types, 3 fns, 72 LOC
- **extractor_cogops** (python) — 0 types, 3 fns, 69 LOC
- **super_extractor** (python) — 0 types, 4 fns, 87 LOC
- **vault_graph_cli** (python) — 1 types, 7 fns, 247 LOC
- **functional_test** (python) — 0 types, 1 fns, 137 LOC
- **test_apa** (python) — 5 types, 34 fns, 311 LOC
- **test_auth** (python) — 0 types, 1 fns, 61 LOC
- **test_change_listener** (python) — 0 types, 4 fns, 48 LOC
- **test_cogops_smoke** (python) — 1 types, 3 fns, 200 LOC
- **test_context_bridge** (python) — 8 types, 36 fns, 439 LOC
- **test_deep_functional** (python) — 0 types, 45 fns, 851 LOC
- **test_e2e** (python) — 0 types, 24 fns, 643 LOC
- **test_ecc** (python) — 3 types, 16 fns, 223 LOC
- **test_egtc_v2** (python) — 20 types, 73 fns, 842 LOC
- **test_functional** (python) — 0 types, 29 fns, 824 LOC
- **test_intensive_functional** (python) — 0 types, 30 fns, 831 LOC
- **test_ios** (python) — 14 types, 45 fns, 805 LOC
- **test_mcp_protocol** (python) — 0 types, 4 fns, 159 LOC
- **test_production_e2e** (python) — 0 types, 4 fns, 556 LOC
- **test_proxy_providers** (python) — 17 types, 88 fns, 885 LOC
- **test_real_user** (python) — 0 types, 6 fns, 418 LOC
- **test_repo_map** (python) — 0 types, 2 fns, 26 LOC
- **test_rust_cogops** (python) — 1 types, 3 fns, 133 LOC
- **test_zero_token_autonomy** (python) — 10 types, 43 fns, 617 LOC
- **test_zero_token_invariants** (python) — 0 types, 2 fns, 139 LOC
- **translate_readme** (python) — 0 types, 1 fns, 44 LOC

## Language Distribution
- rust: 55,766 LOC
- python: 40,354 LOC
- javascript: 4,477 LOC
- typescript: 157 LOC
