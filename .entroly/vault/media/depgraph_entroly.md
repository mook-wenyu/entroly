---
title: Dependency Graph: entroly
---
flowchart LR
    autotune__TunableParam["TunableParam"]
    autotune__evaluate["evaluate"]
    autotune__TunableParam --> autotune__evaluate
    autotune__Experiment["Experiment"]
    autotune__Experiment --> autotune__evaluate
    autotune__get["get"]
    autotune__get --> autotune__evaluate
    autotune__set["set"]
    autotune__set --> autotune__evaluate
    autotune__normalize_weights["normalize_weights"]
    autotune__normalize_weights --> autotune__evaluate
    autotune__mutate_random["mutate_random"]
    autotune__mutate_random --> autotune__evaluate
    autotune__snapshot_config["snapshot_config"]
    autotune__snapshot_config --> autotune__evaluate
    autotune__rollback_config["rollback_config"]
    autotune__rollback_config --> autotune__evaluate
    autotune__autotune["autotune"]
    autotune__autotune --> autotune__evaluate
    context_bridge__SessionContext["SessionContext"]
    test_wasm_e2e__config["config"]
    context_bridge__SessionContext --> test_wasm_e2e__config
    context_bridge__AgentBudget["AgentBudget"]
    context_bridge__AgentBudget --> test_wasm_e2e__config
    context_bridge__HeartbeatResult["HeartbeatResult"]
    context_bridge__HeartbeatResult --> test_wasm_e2e__config
    context_bridge__NkbeAllocator["NkbeAllocator"]
    context_bridge__NkbeAllocator --> test_wasm_e2e__config
    context_bridge___AgentState["_AgentState"]
    context_bridge___AgentState --> test_wasm_e2e__config
    context_bridge__CognitiveBus["CognitiveBus"]
    context_bridge__CognitiveBus --> test_wasm_e2e__config
    context_bridge___BusEvent["_BusEvent"]
    context_bridge___BusEvent --> test_wasm_e2e__config
    context_bridge___Subscriber["_Subscriber"]
    context_bridge___Subscriber --> test_wasm_e2e__config
    context_bridge___RateCell["_RateCell"]
    context_bridge___RateCell --> test_wasm_e2e__config
    context_bridge__AgentContext["AgentContext"]
    context_bridge__AgentContext --> test_wasm_e2e__config
    context_bridge__LodTier["LodTier"]
    context_bridge__LodTier --> test_wasm_e2e__config
    context_bridge__AgentState["AgentState"]
    context_bridge__AgentState --> test_wasm_e2e__config
    context_bridge__LODManager["LODManager"]
    context_bridge__LODManager --> test_wasm_e2e__config
    context_bridge__SubagentOrchestrator["SubagentOrchestrator"]
    context_bridge__SubagentOrchestrator --> test_wasm_e2e__config
    context_bridge__CronSessionManager["CronSessionManager"]
    context_bridge__CronSessionManager --> test_wasm_e2e__config
    context_bridge__MemoryBridge["MemoryBridge"]
    context_bridge__MemoryBridge --> test_wasm_e2e__config
    context_bridge__CompressionLevel["CompressionLevel"]
    context_bridge__CompressionLevel --> test_wasm_e2e__config
    context_bridge__HCCFragment["HCCFragment"]
    context_bridge__HCCFragment --> test_wasm_e2e__config
    context_bridge__HCCEngine["HCCEngine"]
    context_bridge__HCCEngine --> test_wasm_e2e__config
    context_bridge__AutoTune["AutoTune"]
    context_bridge__AutoTune --> test_wasm_e2e__config
    context_bridge__MultiAgentContext["MultiAgentContext"]
    context_bridge__MultiAgentContext --> context_bridge__AgentContext
    context_bridge__MultiAgentContext --> test_wasm_e2e__config
    context_bridge____init__["__init__"]
    context_bridge____init__ --> test_wasm_e2e__config
    context_bridge__register_agent["register_agent"]
    context_bridge__register_agent --> test_wasm_e2e__config
    context_bridge__update_fragments["update_fragments"]
    context_bridge__update_fragments --> test_wasm_e2e__config
    context_bridge__allocate["allocate"]
    context_bridge__allocate --> test_wasm_e2e__config
    context_bridge__reinforce["reinforce"]
    context_bridge__reinforce --> test_wasm_e2e__config
    context_bridge__subscribe["subscribe"]
    context_bridge__subscribe --> test_wasm_e2e__config
    context_bridge__publish["publish"]
    context_bridge__publish --> test_wasm_e2e__config
    context_bridge__drain["drain"]
    context_bridge__drain --> test_wasm_e2e__config
    context_bridge__stats["stats"]
    context_bridge__stats --> test_wasm_e2e__config
    context_bridge__observe["observe"]
    context_bridge__observe --> test_wasm_e2e__config
    context_bridge__kl_divergence["kl_divergence"]
    context_bridge__kl_divergence --> test_wasm_e2e__config
    context_bridge__is_spike["is_spike"]
    context_bridge__is_spike --> test_wasm_e2e__config
    context_bridge__ingest_workspace["ingest_workspace"]
    context_bridge__ingest_workspace --> test_wasm_e2e__config
    context_bridge__load_session_context["load_session_context"]
    context_bridge__load_session_context --> test_wasm_e2e__config
    context_bridge__allocate_budgets["allocate_budgets"]
    context_bridge__allocate_budgets --> test_wasm_e2e__config
    context_bridge__optimize_heartbeat["optimize_heartbeat"]
    context_bridge__optimize_heartbeat --> test_wasm_e2e__config
    context_bridge__filter_group_chat["filter_group_chat"]
    context_bridge__filter_group_chat --> test_wasm_e2e__config
    context_bridge__record_outcome["record_outcome"]
    context_bridge__record_outcome --> test_wasm_e2e__config
    context_bridge__publish_event["publish_event"]
    context_bridge__publish_event --> test_wasm_e2e__config
    context_bridge__drain_events["drain_events"]
    context_bridge__drain_events --> test_wasm_e2e__config
    context_bridge__get_stats["get_stats"]
    context_bridge__get_stats --> test_wasm_e2e__config
    context_bridge__register["register"]
    context_bridge__register --> test_wasm_e2e__config
    context_bridge__unregister["unregister"]
    context_bridge__unregister --> test_wasm_e2e__config
    context_bridge__update_load["update_load"]
    context_bridge__update_load --> test_wasm_e2e__config
    context_bridge__tick["tick"]
    context_bridge__tick --> test_wasm_e2e__config
    context_bridge__get_active_agents["get_active_agents"]
    context_bridge__get_active_agents --> test_wasm_e2e__config
    context_bridge__get_budget_weights["get_budget_weights"]
    context_bridge__get_budget_weights --> test_wasm_e2e__config
    context_bridge__can_spawn["can_spawn"]
    context_bridge__can_spawn --> test_wasm_e2e__config
    context_bridge__spawn["spawn"]
    context_bridge__spawn --> test_wasm_e2e__config
    context_bridge__despawn["despawn"]
    context_bridge__despawn --> test_wasm_e2e__config
    context_bridge__get_tree["get_tree"]
    context_bridge__get_tree --> test_wasm_e2e__config
    context_bridge__schedule["schedule"]
    context_bridge__schedule --> test_wasm_e2e__config
    context_bridge__unschedule["unschedule"]
    context_bridge__unschedule --> test_wasm_e2e__config
    context_bridge__get_due_jobs["get_due_jobs"]
    context_bridge__get_due_jobs --> test_wasm_e2e__config
    context_bridge__run_job["run_job"]
    context_bridge__run_job --> test_wasm_e2e__config
    context_bridge__active["active"]
    context_bridge__active --> test_wasm_e2e__config
    context_bridge__bridge_events["bridge_events"]
    context_bridge__bridge_events --> test_wasm_e2e__config
    context_bridge__recall_for_context["recall_for_context"]
    context_bridge__recall_for_context --> test_wasm_e2e__config
    context_bridge__add_fragment["add_fragment"]
    context_bridge__add_fragment --> test_wasm_e2e__config
    context_bridge__optimize["optimize"]
    context_bridge__optimize --> test_wasm_e2e__config
    context_bridge__get_content["get_content"]
    context_bridge__get_content --> test_wasm_e2e__config
    context_bridge__update["update"]
    context_bridge__update --> test_wasm_e2e__config
    context_bridge__get_weights["get_weights"]
    context_bridge__get_weights --> test_wasm_e2e__config
    context_bridge__spawn_subagent["spawn_subagent"]
    context_bridge__spawn_subagent --> test_wasm_e2e__config
    context_bridge__despawn_subagent["despawn_subagent"]
    context_bridge__despawn_subagent --> test_wasm_e2e__config
    context_bridge__get_agent_tree["get_agent_tree"]
    context_bridge__get_agent_tree --> test_wasm_e2e__config
    context_bridge__schedule_cron["schedule_cron"]
    context_bridge__schedule_cron --> test_wasm_e2e__config
    context_bridge__unschedule_cron["unschedule_cron"]
    context_bridge__unschedule_cron --> test_wasm_e2e__config
    context_bridge__get_due_cron_jobs["get_due_cron_jobs"]
    context_bridge__get_due_cron_jobs --> test_wasm_e2e__config
    context_bridge__run_cron_job["run_cron_job"]
    context_bridge__run_cron_job --> test_wasm_e2e__config
    context_bridge__load_hcc_context["load_hcc_context"]
    context_bridge__load_hcc_context --> test_wasm_e2e__config
    context_bridge__bridge_memories["bridge_memories"]
    context_bridge__bridge_memories --> test_wasm_e2e__config
    context_bridge__record_autotune_outcome["record_autotune_outcome"]
    context_bridge__record_autotune_outcome --> test_wasm_e2e__config
    context_bridge__update_agent_load["update_agent_load"]
    context_bridge__update_agent_load --> test_wasm_e2e__config
    sdk__compress["compress"]
    universal_compress__universal_compress["universal_compress"]
    sdk__compress --> universal_compress__universal_compress
    sdk__compress_messages["compress_messages"]
    sdk__compress_messages --> universal_compress__universal_compress
    server___PyDedupIndex["_PyDedupIndex"]
    server___PyDedupIndex --> autotune__autotune
    server__checkpoint["checkpoint"]
    server___PyDedupIndex --> server__checkpoint
    server___PyDedupIndex --> test_wasm_e2e__config
    server___WilsonFeedbackTracker["_WilsonFeedbackTracker"]
    server___WilsonFeedbackTracker --> autotune__autotune
    server___WilsonFeedbackTracker --> server__checkpoint
    server___WilsonFeedbackTracker --> test_wasm_e2e__config
    server__EntrolyEngine["EntrolyEngine"]
    server__EntrolyEngine --> autotune__autotune
    server__EntrolyEngine --> server__checkpoint
    server__EntrolyEngine --> test_wasm_e2e__config
    server__py_analyze_query["py_analyze_query"]
    server__py_analyze_query --> autotune__autotune
    server__py_analyze_query --> server__checkpoint
    server__py_analyze_query --> test_wasm_e2e__config
    server__py_refine_heuristic["py_refine_heuristic"]
    server__py_refine_heuristic --> autotune__autotune
    server__py_refine_heuristic --> server__checkpoint
    server__py_refine_heuristic --> test_wasm_e2e__config
    server____init__["__init__"]
    server____init__ --> autotune__autotune
    server____init__ --> server__checkpoint
    server____init__ --> test_wasm_e2e__config
    server__insert["insert"]
    server__insert --> autotune__autotune
    server__insert --> server__checkpoint
    server__insert --> test_wasm_e2e__config
    server__remove["remove"]
    server__remove --> autotune__autotune
    server__remove --> server__checkpoint
    server__remove --> test_wasm_e2e__config
    server__stats["stats"]
    server__stats --> autotune__autotune
    server__stats --> server__checkpoint
    server__stats --> test_wasm_e2e__config
    server__record_success["record_success"]
    server__record_success --> autotune__autotune
    server__record_success --> server__checkpoint
    server__record_success --> test_wasm_e2e__config
    server__record_failure["record_failure"]
    server__record_failure --> autotune__autotune
    server__record_failure --> server__checkpoint
    server__record_failure --> test_wasm_e2e__config
    server__learned_value["learned_value"]
    server__learned_value --> autotune__autotune
    server__learned_value --> server__checkpoint
    server__learned_value --> test_wasm_e2e__config
    server__advance_turn["advance_turn"]
    server__advance_turn --> autotune__autotune
    server__advance_turn --> server__checkpoint
    server__advance_turn --> test_wasm_e2e__config
    server__ingest_fragment["ingest_fragment"]
    server__ingest_fragment --> autotune__autotune
    server__ingest_fragment --> server__checkpoint
    server__ingest_fragment --> test_wasm_e2e__config
    server__optimize_context["optimize_context"]
    server__optimize_context --> autotune__autotune
    server__optimize_context --> server__checkpoint
    server__optimize_context --> test_wasm_e2e__config
    server__recall_relevant["recall_relevant"]
    server__recall_relevant --> autotune__autotune
    server__recall_relevant --> server__checkpoint
    server__recall_relevant --> test_wasm_e2e__config
    server__record_reward["record_reward"]
    server__record_reward --> autotune__autotune
    server__record_reward --> server__checkpoint
    server__record_reward --> test_wasm_e2e__config
    server__set_model["set_model"]
    server__set_model --> autotune__autotune
    server__set_model --> server__checkpoint
    server__set_model --> test_wasm_e2e__config
    server__set_cache_cost_per_token["set_cache_cost_per_token"]
    server__set_cache_cost_per_token --> autotune__autotune
    server__set_cache_cost_per_token --> server__checkpoint
    server__set_cache_cost_per_token --> test_wasm_e2e__config
    server__cache_clear["cache_clear"]
    server__cache_clear --> autotune__autotune
    server__cache_clear --> server__checkpoint
    server__cache_clear --> test_wasm_e2e__config
    server__cache_len["cache_len"]
    server__cache_len --> autotune__autotune
    server__cache_len --> server__checkpoint
    server__cache_len --> test_wasm_e2e__config
    server__cache_is_empty["cache_is_empty"]
    server__cache_is_empty --> autotune__autotune
    server__cache_is_empty --> server__checkpoint
    server__cache_is_empty --> test_wasm_e2e__config
    server__cache_hit_rate["cache_hit_rate"]
    server__cache_hit_rate --> autotune__autotune
    server__cache_hit_rate --> server__checkpoint
    server__cache_hit_rate --> test_wasm_e2e__config
    server__prefetch_related["prefetch_related"]
    server__prefetch_related --> autotune__autotune
    server__prefetch_related --> server__checkpoint
    server__prefetch_related --> test_wasm_e2e__config
    server__checkpoint --> autotune__autotune
    server__checkpoint --> server__checkpoint
    server__checkpoint --> test_wasm_e2e__config
    server__resume["resume"]
    server__resume --> autotune__autotune
    server__resume --> server__checkpoint
    server__resume --> test_wasm_e2e__config
    server__get_stats["get_stats"]
    server__get_stats --> autotune__autotune
    server__get_stats --> server__checkpoint
    server__get_stats --> test_wasm_e2e__config
    server__explain_selection["explain_selection"]
    server__explain_selection --> autotune__autotune
    server__explain_selection --> server__checkpoint
    server__explain_selection --> test_wasm_e2e__config
    server__create_mcp_server["create_mcp_server"]
    server__create_mcp_server --> autotune__autotune
    server__create_mcp_server --> server__checkpoint
    server__create_mcp_server --> test_wasm_e2e__config
    server__remember_fragment["remember_fragment"]
    server__remember_fragment --> autotune__autotune
    server__remember_fragment --> server__checkpoint
    server__remember_fragment --> test_wasm_e2e__config
    server__record_outcome["record_outcome"]
    server__record_outcome --> autotune__autotune
    server__record_outcome --> server__checkpoint
    server__record_outcome --> test_wasm_e2e__config
    server__explain_context["explain_context"]
    server__explain_context --> autotune__autotune
    server__explain_context --> server__checkpoint
    server__explain_context --> test_wasm_e2e__config
    server__checkpoint_state["checkpoint_state"]
    server__checkpoint_state --> autotune__autotune
    server__checkpoint_state --> server__checkpoint
    server__checkpoint_state --> test_wasm_e2e__config
    server__resume_state["resume_state"]
    server__resume_state --> autotune__autotune
    server__resume_state --> server__checkpoint
    server__resume_state --> test_wasm_e2e__config
    server__entroly_dashboard["entroly_dashboard"]
    server__entroly_dashboard --> autotune__autotune
    server__entroly_dashboard --> server__checkpoint
    server__entroly_dashboard --> test_wasm_e2e__config
    server__scan_for_vulnerabilities["scan_for_vulnerabilities"]
    server__scan_for_vulnerabilities --> autotune__autotune
    server__scan_for_vulnerabilities --> server__checkpoint
    server__scan_for_vulnerabilities --> test_wasm_e2e__config
    server__security_report["security_report"]
    server__security_report --> autotune__autotune
    server__security_report --> server__checkpoint
    server__security_report --> test_wasm_e2e__config
    server__analyze_codebase_health["analyze_codebase_health"]
    server__analyze_codebase_health --> autotune__autotune
    server__analyze_codebase_health --> server__checkpoint
    server__analyze_codebase_health --> test_wasm_e2e__config
    server__ingest_diagram["ingest_diagram"]
    server__ingest_diagram --> autotune__autotune
    server__ingest_diagram --> server__checkpoint
    server__ingest_diagram --> test_wasm_e2e__config
    server__ingest_voice["ingest_voice"]
    server__ingest_voice --> autotune__autotune
    server__ingest_voice --> server__checkpoint
    server__ingest_voice --> test_wasm_e2e__config
    server__ingest_diff["ingest_diff"]
    server__ingest_diff --> autotune__autotune
    server__ingest_diff --> server__checkpoint
    server__ingest_diff --> test_wasm_e2e__config
    server__epistemic_route["epistemic_route"]
    server__epistemic_route --> autotune__autotune
    server__epistemic_route --> server__checkpoint
    server__epistemic_route --> test_wasm_e2e__config
    server__vault_status["vault_status"]
    server__vault_status --> autotune__autotune
    server__vault_status --> server__checkpoint
    server__vault_status --> test_wasm_e2e__config
    server__vault_write_belief["vault_write_belief"]
    server__vault_write_belief --> autotune__autotune
    server__vault_write_belief --> server__checkpoint
    server__vault_write_belief --> test_wasm_e2e__config
    server__vault_query["vault_query"]
    server__vault_query --> autotune__autotune
    server__vault_query --> server__checkpoint
    server__vault_query --> test_wasm_e2e__config
    server__vault_write_action["vault_write_action"]
    server__vault_write_action --> autotune__autotune
    server__vault_write_action --> server__checkpoint
    server__vault_write_action --> test_wasm_e2e__config
    server__compile_beliefs["compile_beliefs"]
    server__compile_beliefs --> autotune__autotune
    server__compile_beliefs --> server__checkpoint
    server__compile_beliefs --> test_wasm_e2e__config
    server__verify_beliefs["verify_beliefs"]
    server__verify_beliefs --> autotune__autotune
    server__verify_beliefs --> server__checkpoint
    server__verify_beliefs --> test_wasm_e2e__config
    server__blast_radius["blast_radius"]
    server__blast_radius --> autotune__autotune
    server__blast_radius --> server__checkpoint
    server__blast_radius --> test_wasm_e2e__config
    server__process_change["process_change"]
    server__process_change --> autotune__autotune
    server__process_change --> server__checkpoint
    server__process_change --> test_wasm_e2e__config
    server__execute_flow["execute_flow"]
    server__execute_flow --> autotune__autotune
    server__execute_flow --> server__checkpoint
    server__execute_flow --> test_wasm_e2e__config
    server__create_skill["create_skill"]
    server__create_skill --> autotune__autotune
    server__create_skill --> server__checkpoint
    server__create_skill --> test_wasm_e2e__config
    server__manage_skills["manage_skills"]
    server__manage_skills --> autotune__autotune
    server__manage_skills --> server__checkpoint
    server__manage_skills --> test_wasm_e2e__config
    server__coverage_gaps["coverage_gaps"]
    server__coverage_gaps --> autotune__autotune
    server__coverage_gaps --> server__checkpoint
    server__coverage_gaps --> test_wasm_e2e__config
    server__refresh_beliefs["refresh_beliefs"]
    server__refresh_beliefs --> autotune__autotune
    server__refresh_beliefs --> server__checkpoint
    server__refresh_beliefs --> test_wasm_e2e__config
    server__sync_workspace_changes["sync_workspace_changes"]
    server__sync_workspace_changes --> autotune__autotune
    server__sync_workspace_changes --> server__checkpoint
    server__sync_workspace_changes --> test_wasm_e2e__config
    server__repo_file_map["repo_file_map"]
    server__repo_file_map --> autotune__autotune
    server__repo_file_map --> server__checkpoint
    server__repo_file_map --> test_wasm_e2e__config
    server__start_workspace_listener["start_workspace_listener"]
    server__start_workspace_listener --> autotune__autotune
    server__start_workspace_listener --> server__checkpoint
    server__start_workspace_listener --> test_wasm_e2e__config
    server__vault_search["vault_search"]
    server__vault_search --> autotune__autotune
    server__vault_search --> server__checkpoint
    server__vault_search --> test_wasm_e2e__config
    server__compile_docs["compile_docs"]
    server__compile_docs --> autotune__autotune
    server__compile_docs --> server__checkpoint
    server__compile_docs --> test_wasm_e2e__config
    server__export_training_data["export_training_data"]
    server__export_training_data --> autotune__autotune
    server__export_training_data --> server__checkpoint
    server__export_training_data --> test_wasm_e2e__config
    server__main["main"]
    server__main --> autotune__autotune
    server__main --> server__checkpoint
    server__main --> test_wasm_e2e__config
    anomaly__EntropyAnomaly["EntropyAnomaly"]
    entropy__boilerplate_ratio["boilerplate_ratio"]
    anomaly__EntropyAnomaly --> entropy__boilerplate_ratio
    fragment__ContextFragment["ContextFragment"]
    anomaly__EntropyAnomaly --> fragment__ContextFragment
    anomaly__AnomalyReport["AnomalyReport"]
    anomaly__AnomalyReport --> entropy__boilerplate_ratio
    anomaly__AnomalyReport --> fragment__ContextFragment
    anomaly__AnomalyType["AnomalyType"]
    anomaly__AnomalyType --> entropy__boilerplate_ratio
    anomaly__AnomalyType --> fragment__ContextFragment
    anomaly__median["median"]
    anomaly__median --> entropy__boilerplate_ratio
    anomaly__median --> fragment__ContextFragment
    anomaly__directory_of["directory_of"]
    anomaly__directory_of --> entropy__boilerplate_ratio
    anomaly__directory_of --> fragment__ContextFragment
    anomaly__scan_anomalies["scan_anomalies"]
    anomaly__scan_anomalies --> entropy__boilerplate_ratio
    anomaly__scan_anomalies --> fragment__ContextFragment
    anomaly__basename["basename"]
    anomaly__basename --> entropy__boilerplate_ratio
    anomaly__basename --> fragment__ContextFragment
    cache__CacheEntry["CacheEntry"]
    lsh__LshIndex["LshIndex"]
    cache__CacheEntry --> lsh__LshIndex
    cache__CostModel["CostModel"]
    cache__CostModel --> lsh__LshIndex
    cache__EntropySketch["EntropySketch"]
    cache__EntropySketch --> lsh__LshIndex
    cache__FrequencySketch["FrequencySketch"]
    cache__FrequencySketch --> lsh__LshIndex
    cache__ShiftDetector["ShiftDetector"]
    cache__ShiftDetector --> lsh__LshIndex
    cache__TailStats["TailStats"]
    cache__TailStats --> lsh__LshIndex
    cache__AdaptiveAlpha["AdaptiveAlpha"]
    cache__AdaptiveAlpha --> lsh__LshIndex
    cache__ThompsonGate["ThompsonGate"]
    cache__ThompsonGate --> lsh__LshIndex
    cache__SubmodularEvictor["SubmodularEvictor"]
    cache__SubmodularEvictor --> lsh__LshIndex
    cache__CausalInvalidator["CausalInvalidator"]
    cache__CausalInvalidator --> lsh__LshIndex
    cache__HitPredictor["HitPredictor"]
    cache__HitPredictor --> lsh__LshIndex
    cache__EgscConfig["EgscConfig"]
    cache__EgscConfig --> lsh__LshIndex
    cache__CacheSnapshot["CacheSnapshot"]
    cache__CacheSnapshot --> lsh__LshIndex
    cache__EgscCache["EgscCache"]
    cache__EgscCache --> lsh__LshIndex
    cache__CacheStats["CacheStats"]
    cache__CacheStats --> lsh__LshIndex
    cache__CacheLookup["CacheLookup"]
    cache__CacheLookup --> lsh__LshIndex
    channel__ContradictionReport["ContradictionReport"]
    depgraph__DepGraph["DepGraph"]
    channel__ContradictionReport --> depgraph__DepGraph
    channel__ContradictionReport --> fragment__ContextFragment
    channel__trigram_hashes["trigram_hashes"]
    channel__trigram_hashes --> depgraph__DepGraph
    channel__trigram_hashes --> fragment__ContextFragment
    channel__build_trigram_set["build_trigram_set"]
    channel__build_trigram_set --> depgraph__DepGraph
    channel__build_trigram_set --> fragment__ContextFragment
    channel__marginal_gain["marginal_gain"]
    channel__marginal_gain --> depgraph__DepGraph
    channel__marginal_gain --> fragment__ContextFragment
    channel__channel_trailing_pass["channel_trailing_pass"]
    channel__channel_trailing_pass --> depgraph__DepGraph
    channel__channel_trailing_pass --> fragment__ContextFragment
    channel__attention_weight["attention_weight"]
    channel__attention_weight --> depgraph__DepGraph
    channel__attention_weight --> fragment__ContextFragment
    channel__semantic_interleave["semantic_interleave"]
    channel__semantic_interleave --> depgraph__DepGraph
    channel__semantic_interleave --> fragment__ContextFragment
    channel__information_reward["information_reward"]
    channel__information_reward --> depgraph__DepGraph
    channel__information_reward --> fragment__ContextFragment
    channel__modulated_reward["modulated_reward"]
    channel__modulated_reward --> depgraph__DepGraph
    channel__modulated_reward --> fragment__ContextFragment
    channel__contradiction_guard["contradiction_guard"]
    channel__contradiction_guard --> depgraph__DepGraph
    channel__contradiction_guard --> fragment__ContextFragment
    channel__bookend_calibrate["bookend_calibrate"]
    channel__bookend_calibrate --> depgraph__DepGraph
    channel__bookend_calibrate --> fragment__ContextFragment
    health__ClonePair["ClonePair"]
    dedup__hamming_distance["hamming_distance"]
    health__ClonePair --> dedup__hamming_distance
    health__ClonePair --> depgraph__DepGraph
    health__ClonePair --> fragment__ContextFragment
    health__DeadSymbol["DeadSymbol"]
    health__DeadSymbol --> dedup__hamming_distance
    health__DeadSymbol --> depgraph__DepGraph
    health__DeadSymbol --> fragment__ContextFragment
    health__GodFile["GodFile"]
    health__GodFile --> dedup__hamming_distance
    health__GodFile --> depgraph__DepGraph
    health__GodFile --> fragment__ContextFragment
    health__ArchViolation["ArchViolation"]
    health__ArchViolation --> dedup__hamming_distance
    health__ArchViolation --> depgraph__DepGraph
    health__ArchViolation --> fragment__ContextFragment
    health__NamingIssue["NamingIssue"]
    health__NamingIssue --> dedup__hamming_distance
    health__NamingIssue --> depgraph__DepGraph
    health__NamingIssue --> fragment__ContextFragment
    health__HealthReport["HealthReport"]
    health__HealthReport --> dedup__hamming_distance
    health__HealthReport --> depgraph__DepGraph
    health__HealthReport --> fragment__ContextFragment
    health__CloneType["CloneType"]
    health__CloneType --> dedup__hamming_distance
    health__CloneType --> depgraph__DepGraph
    health__CloneType --> fragment__ContextFragment
    health__detect_clones["detect_clones"]
    health__detect_clones --> dedup__hamming_distance
    health__detect_clones --> depgraph__DepGraph
    health__detect_clones --> fragment__ContextFragment
    health__find_dead_symbols["find_dead_symbols"]
    health__find_dead_symbols --> dedup__hamming_distance
    health__find_dead_symbols --> depgraph__DepGraph
    health__find_dead_symbols --> fragment__ContextFragment
    health__is_generic_symbol["is_generic_symbol"]
    health__is_generic_symbol --> dedup__hamming_distance
    health__is_generic_symbol --> depgraph__DepGraph
    health__is_generic_symbol --> fragment__ContextFragment
    health__find_god_files["find_god_files"]
    health__find_god_files --> dedup__hamming_distance
    health__find_god_files --> depgraph__DepGraph
    health__find_god_files --> fragment__ContextFragment
    health__classify_layer["classify_layer"]
    health__classify_layer --> dedup__hamming_distance
    health__classify_layer --> depgraph__DepGraph
    health__classify_layer --> fragment__ContextFragment
    health__find_arch_violations["find_arch_violations"]
    health__find_arch_violations --> dedup__hamming_distance
    health__find_arch_violations --> depgraph__DepGraph
    health__find_arch_violations --> fragment__ContextFragment
    health__find_layer_in_import["find_layer_in_import"]
    health__find_layer_in_import --> dedup__hamming_distance
    health__find_layer_in_import --> depgraph__DepGraph
    health__find_layer_in_import --> fragment__ContextFragment
    health__find_naming_issues["find_naming_issues"]
    health__find_naming_issues --> dedup__hamming_distance
    health__find_naming_issues --> depgraph__DepGraph
    health__find_naming_issues --> fragment__ContextFragment
    health__compute_code_health["compute_code_health"]
    health__compute_code_health --> dedup__hamming_distance
    health__compute_code_health --> depgraph__DepGraph
    health__compute_code_health --> fragment__ContextFragment
    health__health_grade["health_grade"]
    health__health_grade --> dedup__hamming_distance
    health__health_grade --> depgraph__DepGraph
    health__health_grade --> fragment__ContextFragment
    health__analyze_health["analyze_health"]
    health__analyze_health --> dedup__hamming_distance
    health__analyze_health --> depgraph__DepGraph
    health__analyze_health --> fragment__ContextFragment
    health__basename["basename"]
    health__basename --> dedup__hamming_distance
    health__basename --> depgraph__DepGraph
    health__basename --> fragment__ContextFragment
    health__to_snake_case["to_snake_case"]
    health__to_snake_case --> dedup__hamming_distance
    health__to_snake_case --> depgraph__DepGraph
    health__to_snake_case --> fragment__ContextFragment
    health__to_pascal_case["to_pascal_case"]
    health__to_pascal_case --> dedup__hamming_distance
    health__to_pascal_case --> depgraph__DepGraph
    health__to_pascal_case --> fragment__ContextFragment
    hierarchical__HccResult["HccResult"]
    hierarchical__HccResult --> depgraph__DepGraph
    hierarchical__HccResult --> fragment__ContextFragment
    hierarchical__compress_level1["compress_level1"]
    hierarchical__compress_level1 --> depgraph__DepGraph
    hierarchical__compress_level1 --> fragment__ContextFragment
    hierarchical__extract_oneliner_from_skeleton["extract_oneliner_from_skeleton"]
    hierarchical__extract_oneliner_from_skeleton --> depgraph__DepGraph
    hierarchical__extract_oneliner_from_skeleton --> fragment__ContextFragment
    hierarchical__identify_cluster["identify_cluster"]
    hierarchical__identify_cluster --> depgraph__DepGraph
    hierarchical__identify_cluster --> fragment__ContextFragment
    hierarchical__compress_level2["compress_level2"]
    hierarchical__compress_level2 --> depgraph__DepGraph
    hierarchical__compress_level2 --> fragment__ContextFragment
    hierarchical__allocate_budget["allocate_budget"]
    hierarchical__allocate_budget --> depgraph__DepGraph
    hierarchical__allocate_budget --> fragment__ContextFragment
    hierarchical__submodular_marginal_gain["submodular_marginal_gain"]
    hierarchical__submodular_marginal_gain --> depgraph__DepGraph
    hierarchical__submodular_marginal_gain --> fragment__ContextFragment
    hierarchical__extract_module["extract_module"]
    hierarchical__extract_module --> depgraph__DepGraph
    hierarchical__extract_module --> fragment__ContextFragment
    hierarchical__hierarchical_compress["hierarchical_compress"]
    hierarchical__hierarchical_compress --> depgraph__DepGraph
    hierarchical__hierarchical_compress --> fragment__ContextFragment
    knapsack_sds__InfoFactors["InfoFactors"]
    knapsack_sds__InfoFactors --> dedup__hamming_distance
    knapsack_sds__SdsResult["SdsResult"]
    knapsack_sds__SdsResult --> dedup__hamming_distance
    knapsack_sds__Resolution["Resolution"]
    knapsack_sds__Resolution --> dedup__hamming_distance
    knapsack_sds__diversity_factor["diversity_factor"]
    knapsack_sds__diversity_factor --> dedup__hamming_distance
    knapsack_sds__compute_pairwise_diversity["compute_pairwise_diversity"]
    knapsack_sds__compute_pairwise_diversity --> dedup__hamming_distance
    knapsack_sds__ios_select["ios_select"]
    knapsack_sds__ios_select --> dedup__hamming_distance
    lib__EntrolyEngine["EntrolyEngine"]
    lib__EntrolyEngine --> cache__CacheLookup
    causal__CausalContextGraph["CausalContextGraph"]
    lib__EntrolyEngine --> causal__CausalContextGraph
    query_persona__QueryPersonaManifold["QueryPersonaManifold"]
    lib__EntrolyEngine --> query_persona__QueryPersonaManifold
    resonance__ResonanceMatrix["ResonanceMatrix"]
    lib__EntrolyEngine --> resonance__ResonanceMatrix
    lib__default_max_fragments["default_max_fragments"]
    lib__default_max_fragments --> cache__CacheLookup
    lib__default_max_fragments --> causal__CausalContextGraph
    lib__default_max_fragments --> query_persona__QueryPersonaManifold
    lib__default_max_fragments --> resonance__ResonanceMatrix
    lib__default_w_recency["default_w_recency"]
    lib__default_w_recency --> cache__CacheLookup
    lib__default_w_recency --> causal__CausalContextGraph
    lib__default_w_recency --> query_persona__QueryPersonaManifold
    lib__default_w_recency --> resonance__ResonanceMatrix
    lib__default_w_frequency["default_w_frequency"]
    lib__default_w_frequency --> cache__CacheLookup
    lib__default_w_frequency --> causal__CausalContextGraph
    lib__default_w_frequency --> query_persona__QueryPersonaManifold
    lib__default_w_frequency --> resonance__ResonanceMatrix
    lib__default_w_semantic["default_w_semantic"]
    lib__default_w_semantic --> cache__CacheLookup
    lib__default_w_semantic --> causal__CausalContextGraph
    lib__default_w_semantic --> query_persona__QueryPersonaManifold
    lib__default_w_semantic --> resonance__ResonanceMatrix
    lib__default_w_entropy["default_w_entropy"]
    lib__default_w_entropy --> cache__CacheLookup
    lib__default_w_entropy --> causal__CausalContextGraph
    lib__default_w_entropy --> query_persona__QueryPersonaManifold
    lib__default_w_entropy --> resonance__ResonanceMatrix
    lib__default_gradient_temperature["default_gradient_temperature"]
    lib__default_gradient_temperature --> cache__CacheLookup
    lib__default_gradient_temperature --> causal__CausalContextGraph
    lib__default_gradient_temperature --> query_persona__QueryPersonaManifold
    lib__default_gradient_temperature --> resonance__ResonanceMatrix
    lib__default_rng_state["default_rng_state"]
    lib__default_rng_state --> cache__CacheLookup
    lib__default_rng_state --> causal__CausalContextGraph
    lib__default_rng_state --> query_persona__QueryPersonaManifold
    lib__default_rng_state --> resonance__ResonanceMatrix
    lib__py_shannon_entropy["py_shannon_entropy"]
    lib__py_shannon_entropy --> cache__CacheLookup
    lib__py_shannon_entropy --> causal__CausalContextGraph
    lib__py_shannon_entropy --> query_persona__QueryPersonaManifold
    lib__py_shannon_entropy --> resonance__ResonanceMatrix
    lib__py_normalized_entropy["py_normalized_entropy"]
    lib__py_normalized_entropy --> cache__CacheLookup
    lib__py_normalized_entropy --> causal__CausalContextGraph
    lib__py_normalized_entropy --> query_persona__QueryPersonaManifold
    lib__py_normalized_entropy --> resonance__ResonanceMatrix
    lib__py_boilerplate_ratio["py_boilerplate_ratio"]
    lib__py_boilerplate_ratio --> cache__CacheLookup
    lib__py_boilerplate_ratio --> causal__CausalContextGraph
    lib__py_boilerplate_ratio --> query_persona__QueryPersonaManifold
    lib__py_boilerplate_ratio --> resonance__ResonanceMatrix
    lib__py_renyi_entropy_2["py_renyi_entropy_2"]
    lib__py_renyi_entropy_2 --> cache__CacheLookup
    lib__py_renyi_entropy_2 --> causal__CausalContextGraph
    lib__py_renyi_entropy_2 --> query_persona__QueryPersonaManifold
    lib__py_renyi_entropy_2 --> resonance__ResonanceMatrix
    lib__py_entropy_divergence["py_entropy_divergence"]
    lib__py_entropy_divergence --> cache__CacheLookup
    lib__py_entropy_divergence --> causal__CausalContextGraph
    lib__py_entropy_divergence --> query_persona__QueryPersonaManifold
    lib__py_entropy_divergence --> resonance__ResonanceMatrix
    lib__py_simhash["py_simhash"]
    lib__py_simhash --> cache__CacheLookup
    lib__py_simhash --> causal__CausalContextGraph
    lib__py_simhash --> query_persona__QueryPersonaManifold
    lib__py_simhash --> resonance__ResonanceMatrix
    lib__py_hamming_distance["py_hamming_distance"]
    lib__py_hamming_distance --> cache__CacheLookup
    lib__py_hamming_distance --> causal__CausalContextGraph
    lib__py_hamming_distance --> query_persona__QueryPersonaManifold
    lib__py_hamming_distance --> resonance__ResonanceMatrix
    lib__py_information_score["py_information_score"]
    lib__py_information_score --> cache__CacheLookup
    lib__py_information_score --> causal__CausalContextGraph
    lib__py_information_score --> query_persona__QueryPersonaManifold
    lib__py_information_score --> resonance__ResonanceMatrix
    lib__py_scan_content["py_scan_content"]
    lib__py_scan_content --> cache__CacheLookup
    lib__py_scan_content --> causal__CausalContextGraph
    lib__py_scan_content --> query_persona__QueryPersonaManifold
    lib__py_scan_content --> resonance__ResonanceMatrix
    lib__py_analyze_query["py_analyze_query"]
    lib__py_analyze_query --> cache__CacheLookup
    lib__py_analyze_query --> causal__CausalContextGraph
    lib__py_analyze_query --> query_persona__QueryPersonaManifold
    lib__py_analyze_query --> resonance__ResonanceMatrix
    lib__py_refine_heuristic["py_refine_heuristic"]
    lib__py_refine_heuristic --> cache__CacheLookup
    lib__py_refine_heuristic --> causal__CausalContextGraph
    lib__py_refine_heuristic --> query_persona__QueryPersonaManifold
    lib__py_refine_heuristic --> resonance__ResonanceMatrix
    lib__py_analyze_health_info["py_analyze_health_info"]
    lib__py_analyze_health_info --> cache__CacheLookup
    lib__py_analyze_health_info --> causal__CausalContextGraph
    lib__py_analyze_health_info --> query_persona__QueryPersonaManifold
    lib__py_analyze_health_info --> resonance__ResonanceMatrix
    lib__py_prune_conversation["py_prune_conversation"]
    lib__py_prune_conversation --> cache__CacheLookup
    lib__py_prune_conversation --> causal__CausalContextGraph
    lib__py_prune_conversation --> query_persona__QueryPersonaManifold
    lib__py_prune_conversation --> resonance__ResonanceMatrix
    lib__py_progressive_thresholds["py_progressive_thresholds"]
    lib__py_progressive_thresholds --> cache__CacheLookup
    lib__py_progressive_thresholds --> causal__CausalContextGraph
    lib__py_progressive_thresholds --> query_persona__QueryPersonaManifold
    lib__py_progressive_thresholds --> resonance__ResonanceMatrix
    lib__py_compress_block["py_compress_block"]
    lib__py_compress_block --> cache__CacheLookup
    lib__py_compress_block --> causal__CausalContextGraph
    lib__py_compress_block --> query_persona__QueryPersonaManifold
    lib__py_compress_block --> resonance__ResonanceMatrix
    lib__py_classify_block["py_classify_block"]
    lib__py_classify_block --> cache__CacheLookup
    lib__py_classify_block --> causal__CausalContextGraph
    lib__py_classify_block --> query_persona__QueryPersonaManifold
    lib__py_classify_block --> resonance__ResonanceMatrix
    lib__py_cross_fragment_redundancy["py_cross_fragment_redundancy"]
    lib__py_cross_fragment_redundancy --> cache__CacheLookup
    lib__py_cross_fragment_redundancy --> causal__CausalContextGraph
    lib__py_cross_fragment_redundancy --> query_persona__QueryPersonaManifold
    lib__py_cross_fragment_redundancy --> resonance__ResonanceMatrix
    lib__py_apply_ebbinghaus_decay["py_apply_ebbinghaus_decay"]
    lib__py_apply_ebbinghaus_decay --> cache__CacheLookup
    lib__py_apply_ebbinghaus_decay --> causal__CausalContextGraph
    lib__py_apply_ebbinghaus_decay --> query_persona__QueryPersonaManifold
    lib__py_apply_ebbinghaus_decay --> resonance__ResonanceMatrix
    lib__py_knapsack_optimize["py_knapsack_optimize"]
    lib__py_knapsack_optimize --> cache__CacheLookup
    lib__py_knapsack_optimize --> causal__CausalContextGraph
    lib__py_knapsack_optimize --> query_persona__QueryPersonaManifold
    lib__py_knapsack_optimize --> resonance__ResonanceMatrix
    lib__entroly_core["entroly_core"]
    lib__entroly_core --> cache__CacheLookup
    lib__entroly_core --> causal__CausalContextGraph
    lib__entroly_core --> query_persona__QueryPersonaManifold
    lib__entroly_core --> resonance__ResonanceMatrix
    semantic_dedup__DeduplicationResult["DeduplicationResult"]
    depgraph__extract_identifiers["extract_identifiers"]
    semantic_dedup__DeduplicationResult --> depgraph__extract_identifiers
    semantic_dedup__DeduplicationResult --> fragment__ContextFragment
    semantic_dedup__content_overlap["content_overlap"]
    semantic_dedup__content_overlap --> depgraph__extract_identifiers
    semantic_dedup__content_overlap --> fragment__ContextFragment
    semantic_dedup__trigram_jaccard["trigram_jaccard"]
    semantic_dedup__trigram_jaccard --> depgraph__extract_identifiers
    semantic_dedup__trigram_jaccard --> fragment__ContextFragment
    semantic_dedup__identifier_jaccard["identifier_jaccard"]
    semantic_dedup__identifier_jaccard --> depgraph__extract_identifiers
    semantic_dedup__identifier_jaccard --> fragment__ContextFragment
    semantic_dedup__semantic_deduplicate["semantic_deduplicate"]
    semantic_dedup__semantic_deduplicate --> depgraph__extract_identifiers
    semantic_dedup__semantic_deduplicate --> fragment__ContextFragment
    semantic_dedup__semantic_deduplicate_with_stats["semantic_deduplicate_with_stats"]
    semantic_dedup__semantic_deduplicate_with_stats --> depgraph__extract_identifiers
    semantic_dedup__semantic_deduplicate_with_stats --> fragment__ContextFragment
    utilization__FragmentUtilization["FragmentUtilization"]
    utilization__FragmentUtilization --> depgraph__extract_identifiers
    utilization__FragmentUtilization --> fragment__ContextFragment
    utilization__UtilizationReport["UtilizationReport"]
    utilization__UtilizationReport --> depgraph__extract_identifiers
    utilization__UtilizationReport --> fragment__ContextFragment
    utilization__trigrams["trigrams"]
    utilization__trigrams --> depgraph__extract_identifiers
    utilization__trigrams --> fragment__ContextFragment
    utilization__identifier_set["identifier_set"]
    utilization__identifier_set --> depgraph__extract_identifiers
    utilization__identifier_set --> fragment__ContextFragment
    utilization__score_utilization["score_utilization"]
    utilization__score_utilization --> depgraph__extract_identifiers
    utilization__score_utilization --> fragment__ContextFragment
    test_brutal__PaymentProcessor["PaymentProcessor"]
    test_brutal__PaymentProcessor --> lib__entroly_core
    test_brutal__Currency["Currency"]
    test_brutal__Currency --> lib__entroly_core
    test_brutal__Transaction["Transaction"]
    test_brutal__Transaction --> lib__entroly_core
    test_brutal__DatabaseConnection["DatabaseConnection"]
    test_brutal__DatabaseConnection --> lib__entroly_core
    test_brutal__test["test"]
    test_brutal__test --> lib__entroly_core
    test_brutal____init__["__init__"]
    test_brutal____init__ --> lib__entroly_core
    test_brutal__process["process"]
    test_brutal__process --> lib__entroly_core
    test_brutal__refund["refund"]
    test_brutal__refund --> lib__entroly_core
    test_brutal__get_exchange_rate["get_exchange_rate"]
    test_brutal__get_exchange_rate --> lib__entroly_core
    test_brutal__total_charged["total_charged"]
    test_brutal__total_charged --> lib__entroly_core
    test_brutal__generate_token["generate_token"]
    test_brutal__generate_token --> lib__entroly_core
    test_brutal__verify_token["verify_token"]
    test_brutal__verify_token --> lib__entroly_core
    test_brutal__connect["connect"]
    test_brutal__connect --> lib__entroly_core
    test_brutal__save["save"]
    test_brutal__save --> lib__entroly_core
    test_brutal__get["get"]
    test_brutal__get --> lib__entroly_core
    test_brutal__db["db"]
    test_brutal__db --> lib__entroly_core
    test_brutal__processor["processor"]
    test_brutal__processor --> lib__entroly_core
    test_brutal__test_process_payment_usd["test_process_payment_usd"]
    test_brutal__test_process_payment_usd --> lib__entroly_core
    test_brutal__test_refund_success["test_refund_success"]
    test_brutal__test_refund_success --> lib__entroly_core
    test_brutal__test_refund_already_refunded["test_refund_already_refunded"]
    test_brutal__test_refund_already_refunded --> lib__entroly_core
    test_brutal__test_real_session_full["test_real_session_full"]
    test_brutal__test_real_session_full --> lib__entroly_core
    test_brutal__test_selection_respects_dependency_ordering["test_selection_respects_dependency_ordering"]
    test_brutal__test_selection_respects_dependency_ordering --> lib__entroly_core
    test_brutal__test_budget_forces_tradeoffs["test_budget_forces_tradeoffs"]
    test_brutal__test_budget_forces_tradeoffs --> lib__entroly_core
    test_brutal__test_budget_with_pinned_overflow["test_budget_with_pinned_overflow"]
    test_brutal__test_budget_with_pinned_overflow --> lib__entroly_core
    test_brutal__test_budget_one_token["test_budget_one_token"]
    test_brutal__test_budget_one_token --> lib__entroly_core
    test_brutal__test_duplicate_updates_existing["test_duplicate_updates_existing"]
    test_brutal__test_duplicate_updates_existing --> lib__entroly_core
    test_brutal__test_many_duplicates_accumulate["test_many_duplicates_accumulate"]
    test_brutal__test_many_duplicates_accumulate --> lib__entroly_core
    test_brutal__test_whitespace_variants_not_deduped["test_whitespace_variants_not_deduped"]
    test_brutal__test_whitespace_variants_not_deduped --> lib__entroly_core
    test_brutal__test_feedback_convergence["test_feedback_convergence"]
    test_brutal__test_feedback_convergence --> lib__entroly_core
    test_brutal__test_feedback_negative_suppresses["test_feedback_negative_suppresses"]
    test_brutal__test_feedback_negative_suppresses --> lib__entroly_core
    test_brutal__test_explain_scores_are_bounded["test_explain_scores_are_bounded"]
    test_brutal__test_explain_scores_are_bounded --> lib__entroly_core
    test_brutal__test_explain_critical_marked["test_explain_critical_marked"]
    test_brutal__test_explain_critical_marked --> lib__entroly_core
    test_brutal__test_explain_consistency_with_optimize["test_explain_consistency_with_optimize"]
    test_brutal__test_explain_consistency_with_optimize --> lib__entroly_core
    test_brutal__test_export_import_produces_same_optimize["test_export_import_produces_same_optimize"]
    test_brutal__test_export_import_produces_same_optimize --> lib__entroly_core
    test_brutal__test_export_import_preserves_feedback["test_export_import_preserves_feedback"]
    test_brutal__test_export_import_preserves_feedback --> lib__entroly_core
    test_brutal__test_sufficiency_full_deps_present["test_sufficiency_full_deps_present"]
    test_brutal__test_sufficiency_full_deps_present --> lib__entroly_core
    test_brutal__test_sufficiency_missing_definition_warns["test_sufficiency_missing_definition_warns"]
    test_brutal__test_sufficiency_missing_definition_warns --> lib__entroly_core
    test_brutal__test_dep_boost_changes_selection["test_dep_boost_changes_selection"]
    test_brutal__test_dep_boost_changes_selection --> lib__entroly_core
    test_brutal__test_exploration_fires_over_many_calls["test_exploration_fires_over_many_calls"]
    test_brutal__test_exploration_fires_over_many_calls --> lib__entroly_core
    test_brutal__test_no_exploration_when_rate_zero["test_no_exploration_when_rate_zero"]
    test_brutal__test_no_exploration_when_rate_zero --> lib__entroly_core
    test_brutal__test_ingest_1000_fragments["test_ingest_1000_fragments"]
    test_brutal__test_ingest_1000_fragments --> lib__entroly_core
    test_brutal__test_optimize_1000_fragments["test_optimize_1000_fragments"]
    test_brutal__test_optimize_1000_fragments --> lib__entroly_core
    test_brutal__test_rapid_advance_turns["test_rapid_advance_turns"]
    test_brutal__test_rapid_advance_turns --> lib__entroly_core
    test_brutal__test_recall_semantic_ranking["test_recall_semantic_ranking"]
    test_brutal__test_recall_semantic_ranking --> lib__entroly_core
    test_brutal__test_recall_top_k_respected["test_recall_top_k_respected"]
    test_brutal__test_recall_top_k_respected --> lib__entroly_core
    test_brutal__test_auth_content_safety["test_auth_content_safety"]
    test_brutal__test_auth_content_safety --> lib__entroly_core
    test_brutal__PASS["PASS"]
    test_brutal__PASS --> lib__entroly_core
    test_brutal__FAIL["FAIL"]
    test_brutal__FAIL --> lib__entroly_core
    test_brutal__REAL_FILES["REAL_FILES"]
    test_brutal__REAL_FILES --> lib__entroly_core
    test_brutal__CACHE_TTL["CACHE_TTL"]
    test_brutal__CACHE_TTL --> lib__entroly_core
    test_brutal__SECRET_KEY["SECRET_KEY"]
    test_brutal__SECRET_KEY --> lib__entroly_core
    test_integration__DataPipeline["DataPipeline"]
    test_integration__DataPipeline --> lib__entroly_core
    test_integration__test["test"]
    test_integration__test --> lib__entroly_core
    test_integration__test_default_constructor["test_default_constructor"]
    test_integration__test_default_constructor --> lib__entroly_core
    test_integration__test_custom_params["test_custom_params"]
    test_integration__test_custom_params --> lib__entroly_core
    test_integration__test_exploration_rate_clamp["test_exploration_rate_clamp"]
    test_integration__test_exploration_rate_clamp --> lib__entroly_core
    test_integration__test_basic_ingest["test_basic_ingest"]
    test_integration__test_basic_ingest --> lib__entroly_core
    test_integration__test_ingest_with_explicit_tokens["test_ingest_with_explicit_tokens"]
    test_integration__test_ingest_with_explicit_tokens --> lib__entroly_core
    test_integration__test_token_estimation_code_vs_prose["test_token_estimation_code_vs_prose"]
    test_integration__test_token_estimation_code_vs_prose --> lib__entroly_core
    test_integration__test_pinned_ingest["test_pinned_ingest"]
    test_integration__test_pinned_ingest --> lib__entroly_core
    test_integration__test_empty_content["test_empty_content"]
    test_integration__test_empty_content --> lib__entroly_core
    test_integration__test_large_content["test_large_content"]
    test_integration__test_large_content --> lib__entroly_core
    test_integration__test_multiple_ingests["test_multiple_ingests"]
    test_integration__test_multiple_ingests --> lib__entroly_core
    test_integration__test_criticality["test_criticality"]
    test_integration__test_criticality --> lib__entroly_core
    test_integration__test_license_safety["test_license_safety"]
    test_integration__test_license_safety --> lib__entroly_core
    test_integration__test_security_warning_safety["test_security_warning_safety"]
    test_integration__test_security_warning_safety --> lib__entroly_core
    test_integration__test_normal_code_not_pinned["test_normal_code_not_pinned"]
    test_integration__test_normal_code_not_pinned --> lib__entroly_core
    test_integration__test_entropy_honest_for_critical["test_entropy_honest_for_critical"]
    test_integration__test_entropy_honest_for_critical --> lib__entroly_core
    test_integration__test_entropy_varies_with_content["test_entropy_varies_with_content"]
    test_integration__test_entropy_varies_with_content --> lib__entroly_core
    test_integration__test_exact_duplicate["test_exact_duplicate"]
    test_integration__test_exact_duplicate --> lib__entroly_core
    test_integration__test_different_content_not_duplicate["test_different_content_not_duplicate"]
    test_integration__test_different_content_not_duplicate --> lib__entroly_core
    test_integration__test_near_duplicate["test_near_duplicate"]
    test_integration__test_near_duplicate --> lib__entroly_core
    test_integration__test_dep_graph_auto_link["test_dep_graph_auto_link"]
    test_integration__test_dep_graph_auto_link --> lib__entroly_core
    test_integration__test_dep_graph_import_detection["test_dep_graph_import_detection"]
    test_integration__test_dep_graph_import_detection --> lib__entroly_core
    test_integration__test_dep_graph_order_matters["test_dep_graph_order_matters"]
    test_integration__test_dep_graph_order_matters --> lib__entroly_core
    test_integration__test_dep_graph_empty["test_dep_graph_empty"]
    test_integration__test_dep_graph_empty --> lib__entroly_core
    test_integration__test_bug_tracing["test_bug_tracing"]
    test_integration__test_bug_tracing --> lib__entroly_core
    test_integration__test_refactoring["test_refactoring"]
    test_integration__test_refactoring --> lib__entroly_core
    test_integration__test_code_generation["test_code_generation"]
    test_integration__test_code_generation --> lib__entroly_core
    test_integration__test_testing["test_testing"]
    test_integration__test_testing --> lib__entroly_core
    test_integration__test_unknown_task["test_unknown_task"]
    test_integration__test_unknown_task --> lib__entroly_core
    test_integration__test_optimize_empty["test_optimize_empty"]
    test_integration__test_optimize_empty --> lib__entroly_core
    test_integration__test_optimize_selects_within_budget["test_optimize_selects_within_budget"]
    test_integration__test_optimize_selects_within_budget --> lib__entroly_core
    test_integration__test_optimize_adaptive_budget["test_optimize_adaptive_budget"]
    test_integration__test_optimize_adaptive_budget --> lib__entroly_core
    test_integration__test_optimize_pinned_always_included["test_optimize_pinned_always_included"]
    test_integration__test_optimize_pinned_always_included --> lib__entroly_core
    test_integration__test_optimize_sufficiency["test_optimize_sufficiency"]
    test_integration__test_optimize_sufficiency --> lib__entroly_core
    test_integration__test_optimize_returns_ordered["test_optimize_returns_ordered"]
    test_integration__test_optimize_returns_ordered --> lib__entroly_core
    test_integration__test_feedback_success["test_feedback_success"]
    test_integration__test_feedback_success --> lib__entroly_core
    test_integration__test_feedback_failure["test_feedback_failure"]
    test_integration__test_feedback_failure --> lib__entroly_core
    test_integration__test_feedback_affects_ranking["test_feedback_affects_ranking"]
    test_integration__test_feedback_affects_ranking --> lib__entroly_core
    test_integration__test_feedback_empty_ids["test_feedback_empty_ids"]
    test_integration__test_feedback_empty_ids --> lib__entroly_core
    test_integration__test_feedback_nonexistent_id["test_feedback_nonexistent_id"]
    test_integration__test_feedback_nonexistent_id --> lib__entroly_core
    test_integration__test_explain_before_optimize["test_explain_before_optimize"]
    test_integration__test_explain_before_optimize --> lib__entroly_core
    test_integration__test_explain_after_optimize["test_explain_after_optimize"]
    test_integration__test_explain_after_optimize --> lib__entroly_core
    test_integration__test_recall_empty["test_recall_empty"]
    test_integration__test_recall_empty --> lib__entroly_core
    test_integration__test_recall_returns_ranked["test_recall_returns_ranked"]
    test_integration__test_recall_returns_ranked --> lib__entroly_core
    test_integration__test_advance_turn["test_advance_turn"]
    test_integration__test_advance_turn --> lib__entroly_core
    test_integration__test_decay_evicts_stale["test_decay_evicts_stale"]
    test_integration__test_decay_evicts_stale --> lib__entroly_core
    test_integration__test_pinned_survives_decay["test_pinned_survives_decay"]
    test_integration__test_pinned_survives_decay --> lib__entroly_core
    test_integration__test_critical_file_survives_decay["test_critical_file_survives_decay"]
    test_integration__test_critical_file_survives_decay --> lib__entroly_core
    test_integration__test_export_import_roundtrip["test_export_import_roundtrip"]
    test_integration__test_export_import_roundtrip --> lib__entroly_core
    test_integration__test_import_invalid_json["test_import_invalid_json"]
    test_integration__test_import_invalid_json --> lib__entroly_core
    test_integration__test_stats_structure["test_stats_structure"]
    test_integration__test_stats_structure --> lib__entroly_core
    test_integration__test_shannon_entropy["test_shannon_entropy"]
    test_integration__test_shannon_entropy --> lib__entroly_core
    test_integration__test_simhash["test_simhash"]
    test_integration__test_simhash --> lib__entroly_core
    test_integration__test_hamming_distance["test_hamming_distance"]
    test_integration__test_hamming_distance --> lib__entroly_core
    test_integration__test_normalized_entropy["test_normalized_entropy"]
    test_integration__test_normalized_entropy --> lib__entroly_core
    test_integration__test_boilerplate_ratio["test_boilerplate_ratio"]
    test_integration__test_boilerplate_ratio --> lib__entroly_core
    test_integration__test_unicode_content["test_unicode_content"]
    test_integration__test_unicode_content --> lib__entroly_core
    test_integration__test_binary_like_content["test_binary_like_content"]
    test_integration__test_binary_like_content --> lib__entroly_core
    test_integration__test_very_long_source_path["test_very_long_source_path"]
    test_integration__test_very_long_source_path --> lib__entroly_core
    test_integration__test_optimize_zero_budget["test_optimize_zero_budget"]
    test_integration__test_optimize_zero_budget --> lib__entroly_core
    test_integration__test_recall_zero_k["test_recall_zero_k"]
    test_integration__test_recall_zero_k --> lib__entroly_core
    test_integration____init__["__init__"]
    test_integration____init__ --> lib__entroly_core
    test_integration__ingest_event["ingest_event"]
    test_integration__ingest_event --> lib__entroly_core
    test_integration__flush["flush"]
    test_integration__flush --> lib__entroly_core
    test_integration__test_skeleton_populated_on_ingest_python["test_skeleton_populated_on_ingest_python"]
    test_integration__test_skeleton_populated_on_ingest_python --> lib__entroly_core
    test_integration__test_skeleton_token_count_less_than_full["test_skeleton_token_count_less_than_full"]
    test_integration__test_skeleton_token_count_less_than_full --> lib__entroly_core
    test_integration__test_no_skeleton_for_non_code["test_no_skeleton_for_non_code"]
    test_integration__test_no_skeleton_for_non_code --> lib__entroly_core
    test_integration__test_skeleton_present_for_js["test_skeleton_present_for_js"]
    test_integration__test_skeleton_present_for_js --> lib__entroly_core
    test_integration__test_optimize_uses_skeleton_when_budget_tight["test_optimize_uses_skeleton_when_budget_tight"]
    test_integration__test_optimize_uses_skeleton_when_budget_tight --> lib__entroly_core
    test_integration__test_optimize_prefers_full_when_budget_allows["test_optimize_prefers_full_when_budget_allows"]
    test_integration__test_optimize_prefers_full_when_budget_allows --> lib__entroly_core
    test_integration__test_optimize_variant_field_always_present["test_optimize_variant_field_always_present"]
    test_integration__test_optimize_variant_field_always_present --> lib__entroly_core
    test_integration__PASS["PASS"]
    test_integration__PASS --> lib__entroly_core
    test_integration__FAIL["FAIL"]
    test_integration__FAIL --> lib__entroly_core
    test_integration__CRITICAL_FILES["CRITICAL_FILES"]
    test_integration__CRITICAL_FILES --> lib__entroly_core
    test_integration__SAFETY_FILES["SAFETY_FILES"]
    test_integration__SAFETY_FILES --> lib__entroly_core
    test_integration__IMPORTANT_FILES["IMPORTANT_FILES"]
    test_integration__IMPORTANT_FILES --> lib__entroly_core
    test_integration__NORMAL_FILES["NORMAL_FILES"]
    test_integration__NORMAL_FILES --> lib__entroly_core
    test_integration__PYTHON_CODE["PYTHON_CODE"]
    test_integration__PYTHON_CODE --> lib__entroly_core
    test_integration__MAX_BUFFER["MAX_BUFFER"]
    test_integration__MAX_BUFFER --> lib__entroly_core
    test_integration__DEFAULT_BATCH["DEFAULT_BATCH"]
    test_integration__DEFAULT_BATCH --> lib__entroly_core
    test_integration__JS_CODE["JS_CODE"]
    test_integration__JS_CODE --> lib__entroly_core
    lib__WasmEntrolyEngine["WasmEntrolyEngine"]
    lib__WasmEntrolyEngine --> causal__CausalContextGraph
    lib__WasmEntrolyEngine --> query_persona__QueryPersonaManifold
    lib__WasmEntrolyEngine --> resonance__ResonanceMatrix
    lib__json_to_js["json_to_js"]
    lib__json_to_js --> causal__CausalContextGraph
    lib__json_to_js --> query_persona__QueryPersonaManifold
    lib__json_to_js --> resonance__ResonanceMatrix
    functional_test__run_functional_test["run_functional_test"]
    functional_test__run_functional_test --> lib__entroly_core
    functional_test__run_functional_test --> test_wasm_e2e__config
    test_e2e__test_knapsack_selects_optimal_subset["test_knapsack_selects_optimal_subset"]
    test_e2e__test_knapsack_selects_optimal_subset --> lib__entroly_core
    test_e2e__test_knapsack_selects_optimal_subset --> server__checkpoint
    test_e2e__test_knapsack_selects_optimal_subset --> test_wasm_e2e__config
    test_e2e__test_knapsack_respects_pinned["test_knapsack_respects_pinned"]
    test_e2e__test_knapsack_respects_pinned --> lib__entroly_core
    test_e2e__test_knapsack_respects_pinned --> server__checkpoint
    test_e2e__test_knapsack_respects_pinned --> test_wasm_e2e__config
    test_e2e__test_ebbinghaus_decay["test_ebbinghaus_decay"]
    test_e2e__test_ebbinghaus_decay --> lib__entroly_core
    test_e2e__test_ebbinghaus_decay --> server__checkpoint
    test_e2e__test_ebbinghaus_decay --> test_wasm_e2e__config
    test_e2e__test_entropy_all_same_chars["test_entropy_all_same_chars"]
    test_e2e__test_entropy_all_same_chars --> lib__entroly_core
    test_e2e__test_entropy_all_same_chars --> server__checkpoint
    test_e2e__test_entropy_all_same_chars --> test_wasm_e2e__config
    test_e2e__test_entropy_increases_with_diversity["test_entropy_increases_with_diversity"]
    test_e2e__test_entropy_increases_with_diversity --> lib__entroly_core
    test_e2e__test_entropy_increases_with_diversity --> server__checkpoint
    test_e2e__test_entropy_increases_with_diversity --> test_wasm_e2e__config
    test_e2e__test_boilerplate_detection["test_boilerplate_detection"]
    test_e2e__test_boilerplate_detection --> lib__entroly_core
    test_e2e__test_boilerplate_detection --> server__checkpoint
    test_e2e__test_boilerplate_detection --> test_wasm_e2e__config
    test_e2e__test_cross_fragment_redundancy["test_cross_fragment_redundancy"]
    test_e2e__test_cross_fragment_redundancy --> lib__entroly_core
    test_e2e__test_cross_fragment_redundancy --> server__checkpoint
    test_e2e__test_cross_fragment_redundancy --> test_wasm_e2e__config
    test_e2e__test_simhash_identical_texts["test_simhash_identical_texts"]
    test_e2e__test_simhash_identical_texts --> lib__entroly_core
    test_e2e__test_simhash_identical_texts --> server__checkpoint
    test_e2e__test_simhash_identical_texts --> test_wasm_e2e__config
    test_e2e__test_simhash_similar_texts_close["test_simhash_similar_texts_close"]
    test_e2e__test_simhash_similar_texts_close --> lib__entroly_core
    test_e2e__test_simhash_similar_texts_close --> server__checkpoint
    test_e2e__test_simhash_similar_texts_close --> test_wasm_e2e__config
    test_e2e__test_dedup_index_catches_duplicates["test_dedup_index_catches_duplicates"]
    test_e2e__test_dedup_index_catches_duplicates --> lib__entroly_core
    test_e2e__test_dedup_index_catches_duplicates --> server__checkpoint
    test_e2e__test_dedup_index_catches_duplicates --> test_wasm_e2e__config
    test_e2e__test_dedup_index_allows_different["test_dedup_index_allows_different"]
    test_e2e__test_dedup_index_allows_different --> lib__entroly_core
    test_e2e__test_dedup_index_allows_different --> server__checkpoint
    test_e2e__test_dedup_index_allows_different --> test_wasm_e2e__config
    test_e2e__test_import_extraction["test_import_extraction"]
    test_e2e__test_import_extraction --> lib__entroly_core
    test_e2e__test_import_extraction --> server__checkpoint
    test_e2e__test_import_extraction --> test_wasm_e2e__config
    test_e2e__test_test_file_inference["test_test_file_inference"]
    test_e2e__test_test_file_inference --> lib__entroly_core
    test_e2e__test_test_file_inference --> server__checkpoint
    test_e2e__test_test_file_inference --> test_wasm_e2e__config
    test_e2e__test_co_access_learning["test_co_access_learning"]
    test_e2e__test_co_access_learning --> lib__entroly_core
    test_e2e__test_co_access_learning --> server__checkpoint
    test_e2e__test_co_access_learning --> test_wasm_e2e__config
    test_e2e__test_checkpoint_save_and_load["test_checkpoint_save_and_load"]
    test_e2e__test_checkpoint_save_and_load --> lib__entroly_core
    test_e2e__test_checkpoint_save_and_load --> server__checkpoint
    test_e2e__test_checkpoint_save_and_load --> test_wasm_e2e__config
    test_e2e__test_full_engine_pipeline["test_full_engine_pipeline"]
    test_e2e__test_full_engine_pipeline --> lib__entroly_core
    test_e2e__test_full_engine_pipeline --> server__checkpoint
    test_e2e__test_full_engine_pipeline --> test_wasm_e2e__config
    test_e2e__test_positive_feedback_raises_fragment_value["test_positive_feedback_raises_fragment_value"]
    test_e2e__test_positive_feedback_raises_fragment_value --> lib__entroly_core
    test_e2e__test_positive_feedback_raises_fragment_value --> server__checkpoint
    test_e2e__test_positive_feedback_raises_fragment_value --> test_wasm_e2e__config
    test_e2e__test_negative_feedback_suppresses_fragment["test_negative_feedback_suppresses_fragment"]
    test_e2e__test_negative_feedback_suppresses_fragment --> lib__entroly_core
    test_e2e__test_negative_feedback_suppresses_fragment --> server__checkpoint
    test_e2e__test_negative_feedback_suppresses_fragment --> test_wasm_e2e__config
    test_e2e__test_recall_correct_after_eviction["test_recall_correct_after_eviction"]
    test_e2e__test_recall_correct_after_eviction --> lib__entroly_core
    test_e2e__test_recall_correct_after_eviction --> server__checkpoint
    test_e2e__test_recall_correct_after_eviction --> test_wasm_e2e__config
    test_e2e__test_fragment_guard_flags_secrets["test_fragment_guard_flags_secrets"]
    test_e2e__test_fragment_guard_flags_secrets --> lib__entroly_core
    test_e2e__test_fragment_guard_flags_secrets --> server__checkpoint
    test_e2e__test_fragment_guard_flags_secrets --> test_wasm_e2e__config
    test_e2e__test_fragment_guard_passes_clean_code["test_fragment_guard_passes_clean_code"]
    test_e2e__test_fragment_guard_passes_clean_code --> lib__entroly_core
    test_e2e__test_fragment_guard_passes_clean_code --> server__checkpoint
    test_e2e__test_fragment_guard_passes_clean_code --> test_wasm_e2e__config
    test_e2e__test_provenance_hallucination_risk["test_provenance_hallucination_risk"]
    test_e2e__test_provenance_hallucination_risk --> lib__entroly_core
    test_e2e__test_provenance_hallucination_risk --> server__checkpoint
    test_e2e__test_provenance_hallucination_risk --> test_wasm_e2e__config
    test_e2e__test_export_import_preserves_prism_covariance["test_export_import_preserves_prism_covariance"]
    test_e2e__test_export_import_preserves_prism_covariance --> lib__entroly_core
    test_e2e__test_export_import_preserves_prism_covariance --> server__checkpoint
    test_e2e__test_export_import_preserves_prism_covariance --> test_wasm_e2e__config
    test_e2e__test_token_budget_zero_uses_default["test_token_budget_zero_uses_default"]
    test_e2e__test_token_budget_zero_uses_default --> lib__entroly_core
    test_e2e__test_token_budget_zero_uses_default --> server__checkpoint
    test_e2e__test_token_budget_zero_uses_default --> test_wasm_e2e__config
    test_ios__TestSDSDiversityPenalty["TestSDSDiversityPenalty"]
    test_ios__TestSDSDiversityPenalty --> lib__entroly_core
    test_ios__TestSDSBudgetRespect["TestSDSBudgetRespect"]
    test_ios__TestSDSBudgetRespect --> lib__entroly_core
    test_ios__TestSDSFeedbackIntegration["TestSDSFeedbackIntegration"]
    test_ios__TestSDSFeedbackIntegration --> lib__entroly_core
    test_ios__TestMRKResolutionSelection["TestMRKResolutionSelection"]
    test_ios__TestMRKResolutionSelection --> lib__entroly_core
    test_ios__TestMRKCoverageImprovement["TestMRKCoverageImprovement"]
    test_ios__TestMRKCoverageImprovement --> lib__entroly_core
    test_ios__TestECDBQueryFactor["TestECDBQueryFactor"]
    test_ios__TestECDBQueryFactor --> lib__entroly_core
    test_ios__TestECDBCodebaseFactor["TestECDBCodebaseFactor"]
    test_ios__TestECDBCodebaseFactor --> lib__entroly_core
    test_ios__TestECDBBounds["TestECDBBounds"]
    test_ios__TestECDBBounds --> lib__entroly_core
    test_ios__TestContextBlockFormatting["TestContextBlockFormatting"]
    test_ios__TestContextBlockFormatting --> lib__entroly_core
    test_ios__TestIOSEndToEnd["TestIOSEndToEnd"]
    test_ios__TestIOSEndToEnd --> lib__entroly_core
    test_ios__TestIOSPerformance["TestIOSPerformance"]
    test_ios__TestIOSPerformance --> lib__entroly_core
    test_ios__TestMathProperties["TestMathProperties"]
    test_ios__TestMathProperties --> lib__entroly_core
    test_ios__TestEdgeCases["TestEdgeCases"]
    test_ios__TestEdgeCases --> lib__entroly_core
    test_ios__TestIOSRegressionFixes["TestIOSRegressionFixes"]
    test_ios__TestIOSRegressionFixes --> lib__entroly_core
    test_ios__make_engine["make_engine"]
    test_ios__make_engine --> lib__entroly_core
    test_ios__ingest_fragment["ingest_fragment"]
    test_ios__ingest_fragment --> lib__entroly_core
    test_ios__test_diverse_selection_over_redundant["test_diverse_selection_over_redundant"]
    test_ios__test_diverse_selection_over_redundant --> lib__entroly_core
    test_ios__test_diversity_score_reported["test_diversity_score_reported"]
    test_ios__test_diversity_score_reported --> lib__entroly_core
    test_ios__test_similar_fragments_low_diversity["test_similar_fragments_low_diversity"]
    test_ios__test_similar_fragments_low_diversity --> lib__entroly_core
    test_ios__test_all_unique_content_high_diversity["test_all_unique_content_high_diversity"]
    test_ios__test_all_unique_content_high_diversity --> lib__entroly_core
    test_ios__test_budget_never_exceeded["test_budget_never_exceeded"]
    test_ios__test_budget_never_exceeded --> lib__entroly_core
    test_ios__test_zero_budget["test_zero_budget"]
    test_ios__test_zero_budget --> lib__entroly_core
    test_ios__test_boosted_fragment_preferred["test_boosted_fragment_preferred"]
    test_ios__test_boosted_fragment_preferred --> lib__entroly_core
    test_ios__test_full_resolution_with_generous_budget["test_full_resolution_with_generous_budget"]
    test_ios__test_full_resolution_with_generous_budget --> lib__entroly_core
    test_ios__test_skeleton_resolution_with_tight_budget["test_skeleton_resolution_with_tight_budget"]
    test_ios__test_skeleton_resolution_with_tight_budget --> lib__entroly_core
    test_ios__test_reference_resolution_exists["test_reference_resolution_exists"]
    test_ios__test_reference_resolution_exists --> lib__entroly_core
    test_ios__test_mrk_disabled_uses_full_only["test_mrk_disabled_uses_full_only"]
    test_ios__test_mrk_disabled_uses_full_only --> lib__entroly_core
    test_ios__test_more_files_covered_with_mrk["test_more_files_covered_with_mrk"]
    test_ios__test_more_files_covered_with_mrk --> lib__entroly_core
    test_ios__test_specific_query_small_budget["test_specific_query_small_budget"]
    test_ios__test_specific_query_small_budget --> lib__entroly_core
    test_ios__test_vague_query_large_budget["test_vague_query_large_budget"]
    test_ios__test_vague_query_large_budget --> lib__entroly_core
    test_ios__test_medium_vagueness_near_static["test_medium_vagueness_near_static"]
    test_ios__test_medium_vagueness_near_static --> lib__entroly_core
    test_ios__test_budget_monotonic_in_vagueness["test_budget_monotonic_in_vagueness"]
    test_ios__test_budget_monotonic_in_vagueness --> lib__entroly_core
    test_ios__test_larger_codebase_larger_budget["test_larger_codebase_larger_budget"]
    test_ios__test_larger_codebase_larger_budget --> lib__entroly_core
    test_ios__test_codebase_factor_caps_at_2x["test_codebase_factor_caps_at_2x"]
    test_ios__test_codebase_factor_caps_at_2x --> lib__entroly_core
    test_ios__test_minimum_budget["test_minimum_budget"]
    test_ios__test_minimum_budget --> lib__entroly_core
    test_ios__test_maximum_budget["test_maximum_budget"]
    test_ios__test_maximum_budget --> lib__entroly_core
    test_ios__test_model_aware_budget["test_model_aware_budget"]
    test_ios__test_model_aware_budget --> lib__entroly_core
    test_ios__test_full_fragments_in_code_fences["test_full_fragments_in_code_fences"]
    test_ios__test_full_fragments_in_code_fences --> lib__entroly_core
    test_ios__test_skeleton_fragments_grouped["test_skeleton_fragments_grouped"]
    test_ios__test_skeleton_fragments_grouped --> lib__entroly_core
    test_ios__test_reference_fragments_listed["test_reference_fragments_listed"]
    test_ios__test_reference_fragments_listed --> lib__entroly_core
    test_ios__test_empty_fragments_returns_empty["test_empty_fragments_returns_empty"]
    test_ios__test_empty_fragments_returns_empty --> lib__entroly_core
    test_ios__test_resolution_ordering["test_resolution_ordering"]
    test_ios__test_resolution_ordering --> lib__entroly_core
    test_ios__test_pipeline_produces_valid_output["test_pipeline_produces_valid_output"]
    test_ios__test_pipeline_produces_valid_output --> lib__entroly_core
    test_ios__test_ios_vs_legacy_both_valid["test_ios_vs_legacy_both_valid"]
    test_ios__test_ios_vs_legacy_both_valid --> lib__entroly_core
    test_ios__test_ios_enabled_flag_in_result["test_ios_enabled_flag_in_result"]
    test_ios__test_ios_enabled_flag_in_result --> lib__entroly_core
    test_ios__test_ios_disabled_no_flag["test_ios_disabled_no_flag"]
    test_ios__test_ios_disabled_no_flag --> lib__entroly_core
    test_ios__test_1000_fragments_under_100ms["test_1000_fragments_under_100ms"]
    test_ios__test_1000_fragments_under_100ms --> lib__entroly_core
    test_ios__test_diversity_factor_bounds["test_diversity_factor_bounds"]
    test_ios__test_diversity_factor_bounds --> lib__entroly_core
    test_ios__test_ecdb_sigmoid_shape["test_ecdb_sigmoid_shape"]
    test_ios__test_ecdb_sigmoid_shape --> lib__entroly_core
    test_ios__test_ecdb_query_factor_formula["test_ecdb_query_factor_formula"]
    test_ios__test_ecdb_query_factor_formula --> lib__entroly_core
    test_ios__test_single_fragment["test_single_fragment"]
    test_ios__test_single_fragment --> lib__entroly_core
    test_ios__test_all_pinned["test_all_pinned"]
    test_ios__test_all_pinned --> lib__entroly_core
    test_ios__test_budget_smaller_than_smallest["test_budget_smaller_than_smallest"]
    test_ios__test_budget_smaller_than_smallest --> lib__entroly_core
    test_ios__test_empty_query["test_empty_query"]
    test_ios__test_empty_query --> lib__entroly_core
    test_ios__test_unicode_content["test_unicode_content"]
    test_ios__test_unicode_content --> lib__entroly_core
    test_ios__test_negative_feedback_does_not_backfill_bad_reference["test_negative_feedback_does_not_backfill_bad_reference"]
    test_ios__test_negative_feedback_does_not_backfill_bad_reference --> lib__entroly_core
    test_ios__test_ios_exploration_can_vary_selected_set["test_ios_exploration_can_vary_selected_set"]
    test_ios__test_ios_exploration_can_vary_selected_set --> lib__entroly_core
    test_ios__test_exploration_does_not_seed_exploit_cache["test_exploration_does_not_seed_exploit_cache"]
    test_ios__test_exploration_does_not_seed_exploit_cache --> lib__entroly_core
    test_ios__test_explain_selection_includes_compressed_variants["test_explain_selection_includes_compressed_variants"]
    test_ios__test_explain_selection_includes_compressed_variants --> lib__entroly_core
    test_rust_cogops__AuthService["AuthService"]
    test_rust_cogops__AuthService --> lib__entroly_core
    test_rust_cogops__check["check"]
    test_rust_cogops__check --> lib__entroly_core
    test_rust_cogops__verify_token["verify_token"]
    test_rust_cogops__verify_token --> lib__entroly_core
    test_rust_cogops__rotate_keys["rotate_keys"]
    test_rust_cogops__rotate_keys --> lib__entroly_core
    test_rust_cogops__PASS["PASS"]
    test_rust_cogops__PASS --> lib__entroly_core