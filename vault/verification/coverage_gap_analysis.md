---
challenges: vault-wide
result: flagged
confidence_delta: -0.05
checked_at: 2026-04-04T21:00:00Z
method: source_belief_cross_reference
---

# Verification: Coverage Gap Analysis

Cross-referenced all source modules in `entroly/` and `entroly-core/src/` against belief files in `vault/beliefs/`.

## Entroly Python Modules (entroly/)

| Module | Belief File | Status |
|---|---|---|
| __init__.py | (package init -- no belief needed) | N/A |
| _docker_launcher.py | [[_docker_launcher_18a33f4c]] | Covered |
| adaptive_pruner.py | [[adaptive_pruner_18a33f4c]] | Covered |
| auto_index.py | [[auto_index_18a33f4c]] | Covered |
| autotune.py | [[autotune_18a33f4c]] | Covered |
| belief_compiler.py | [[belief_compiler_18a33f4c]] | Covered |
| benchmark_harness.py | [[benchmark_harness_18a33f4c]] | Covered |
| change_listener.py | [[change_listener_18a33f4c]] | Covered |
| change_pipeline.py | [[change_pipeline_18a33f4c]] | Covered |
| checkpoint.py | [[checkpoint_18a33f4c]] | Covered |
| cli.py | [[cli_18a33f4c]] | Covered |
| config.py | [[config_18a33f4c]] | Covered |
| context_bridge.py | [[context_bridge_18a33f4c]] | Covered |
| dashboard.py | [[dashboard_18a33f4c]] | Covered |
| entroly_mcp_client.py | [[entroly_mcp_client_18a33f4c]] | Covered |
| epistemic_router.py | [[epistemic_router_18a33f4c]] | Covered |
| evolution_logger.py | [[evolution_logger_18a33f4c]] | Covered |
| flow_orchestrator.py | [[flow_orchestrator_18a33f4c]] | Covered |
| integrate_entroly_mcp.py | [[integrate_entroly_mcp_18a33f4c]] | Covered |
| long_term_memory.py | [[long_term_memory_18a33f4c]] | Covered |
| multimodal.py | [[multimodal_18a33f4c]] | Covered |
| prefetch.py | [[prefetch_18a33f4c]] | Covered |
| provenance.py | [[provenance_18a33f4c]] | Covered |
| proxy.py | [[proxy_18a33f4c]] | Covered |
| proxy_config.py | [[proxy_config_18a33f4c]] | Covered |
| proxy_transform.py | [[proxy_transform_18a33f4c]] | Covered |
| query_refiner.py | [[query_refiner_18a33f4c]] | Covered |
| repo_map.py | [[repo_map_18a33f4c]] | Covered |
| server.py | [[server_18a33f4c]] | Covered |
| skill_engine.py | [[skill_engine_18a33f4c]] | Covered |
| value_tracker.py | [[value_tracker_18a33f4c]] | Covered |
| vault.py | [[vault_18a33f4c]] | Covered |
| verification_engine.py | [[verification_engine_18a33f4c]] | Covered |

**Python coverage: 33/33 (100%)**

## Entroly-Core Rust Modules (entroly-core/src/)

| Module | Belief File | Status |
|---|---|---|
| anomaly.rs | [[anomaly_18a33f4c]] | Covered |
| cache.rs | [[cache_18a33f4c]] | Covered |
| causal.rs | [[causal_18a33f4c]] | Covered |
| channel.rs | [[channel_18a33f4c]] | Covered |
| cognitive_bus.rs | [[cognitive_bus_18a33f4c]] | Covered |
| cogops.rs | [[cogops_18a33f4c]] | Covered |
| conversation_pruner.rs | [[conversation_pruner_18a33f4c]] | Covered |
| dedup.rs | [[dedup_18a33f4c]] | Covered |
| depgraph.rs | [[depgraph_18a33f4c]] | Covered |
| entropy.rs | [[entropy_18a33f4c]] | Covered |
| fragment.rs | [[fragment_18a33f4c]] | Covered |
| guardrails.rs | [[guardrails_18a33f4c]] | Covered |
| health.rs | [[health_18a33f4c]] | Covered |
| hierarchical.rs | [[hierarchical_18a33f4c]] | Covered |
| knapsack.rs | [[knapsack_18a33f4c]] | Covered |
| knapsack_sds.rs | [[knapsack_sds_18a33f4c]] | Covered |
| lib.rs | [[lib_18a33f4c]] | Covered |
| lsh.rs | [[lsh_18a33f4c]] | Covered |
| nkbe.rs | [[nkbe_18a33f4c]] | Covered |
| prism.rs | [[prism_18a33f4c]] | Covered |
| query.rs | [[query_18a33f4c]] | Covered |
| query_persona.rs | [[query_persona_18a33f4c]] | Covered |
| resonance.rs | [[resonance_18a33f4c]] | Covered |
| sast.rs | [[sast_18a33f4c]] | Covered |
| semantic_dedup.rs | [[semantic_dedup_18a33f4c]] | Covered |
| skeleton.rs | [[skeleton_18a33f4c]] | Covered |
| utilization.rs | [[utilization_18a33f4c]] | Covered |

**Rust coverage: 27/27 (100%)**

## Architecture Beliefs

12 architecture beliefs cover cross-cutting concerns:
- [[arch_cogops_epistemic_engine_a8c9d7f6]]
- [[arch_optimize_pipeline_a7c2e1f0]]
- [[arch_rl_learning_loop_b3d4f2a1]]
- [[arch_rust_python_boundary_c4e5f3b2]]
- [[arch_information_theory_stack_d5f6a4c3]]
- [[arch_dedup_hierarchy_e6a7b5d4]]
- [[arch_multi_resolution_f7b8c6e5]]
- [[arch_memory_lifecycle_b9dae8g7]]
- [[arch_scoring_dimensions_caf1b9h8]]
- [[arch_closed_loop_feedback_dbg2ca9i]]
- [[arch_concurrency_model_ecf3db0j]]
- [[arch_query_resolution_flow_fda4ec1k]]

## CogOps Documentation Beliefs

4 canonical specification beliefs:
- [[cogops_canonical_flows_18a33f4c]]
- [[cogops_epistemic_router_18a33f4c]]
- [[cogops_use_cases_18a33f4c]]
- [[cogops_vault_contract_18a33f4c]]

## Gaps Identified

| Gap | Severity | Note |
|---|---|---|
| Vault directories verification/, actions/ are empty | High | No runtime outputs yet. System has not exercised Flows 1-5 live. |
| evolution/skills/ is empty | Medium | No skills synthesized. Flow 5 has not triggered. |
| media/ is empty | Low | No generated diagrams yet. |

## Finding

**FLAGGED**: Source-to-belief coverage is 100% (60/60 modules). However, the Verification, Action, and Evolution output directories are empty, meaning the system has compiled understanding but has not yet exercised it. The vault is structurally complete but operationally dormant.
