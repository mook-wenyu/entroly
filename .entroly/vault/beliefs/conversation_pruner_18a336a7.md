---
claim_id: 18a336a72aaf8bd82ac721d8
entity: conversation_pruner
status: inferred
confidence: 0.75
sources:
  - entroly-wasm\src\conversation_pruner.rs:96
  - entroly-wasm\src\conversation_pruner.rs:109
  - entroly-wasm\src\conversation_pruner.rs:120
  - entroly-wasm\src\conversation_pruner.rs:134
  - entroly-wasm\src\conversation_pruner.rs:147
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: conversation_pruner

**LOC:** 1467

## Entities
- `pub enum BlockKind` (enum)
- `pub fn protection_weight(&self) -> f64` (function)
- `pub fn label(&self) -> &'static str` (function)
- `pub enum Resolution` (enum)
- `pub fn token_fraction(&self) -> f64` (function)
- `pub fn info_retained(&self) -> f64` (function)
- `pub fn info_loss(&self) -> f64` (function)
- `pub fn as_str(&self) -> &'static str` (function)
- `pub fn all() -> &'static [Resolution]` (function)
- `pub struct ConvBlock` (struct)
- `pub struct PruneResult` (struct)
- `pub fn classify_block(role: &str, content: &str, tool_name: Option<&str>) -> BlockKind` (function)
- `fn infer_dependencies(blocks: &[ConvBlock]) -> Vec<Vec<usize>>` (function)
- `fn build_forward_refs(deps: &[Vec<usize>]) -> HashMap<usize, usize>` (function)
- `fn score_block(` (function)
- `fn compute_all_forward_overlaps(blocks: &[ConvBlock]) -> Vec<f64>` (function)
- `pub struct McItem` (struct)
- `fn kkt_multichoice_bisect(` (function)
- `fn enforce_dag_coherence(` (function)
- `fn protect_recent(` (function)
- `pub fn compress_block(block: &ConvBlock, resolution: Resolution) -> String` (function)
- `pub fn prune_conversation(` (function)
- `pub fn progressive_thresholds(` (function)
- `fn make_block(index: usize, role: &str, content: &str, tokens: u32) -> ConvBlock` (function)
- `fn make_tool_block(index: usize, role: &str, content: &str, tokens: u32, tool: &str) -> ConvBlock` (function)
- `fn test_classify_block_types()` (function)
- `fn test_prune_empty()` (function)
- `fn test_prune_everything_fits()` (function)
- `fn test_user_messages_never_pruned()` (function)
- `fn test_system_messages_never_pruned()` (function)
- `fn test_tool_results_pruned_first()` (function)
- `fn test_thinking_blocks_most_aggressively_pruned()` (function)
- `fn test_dag_coherence_propagates()` (function)
- `fn test_dag_coherence_no_upward_propagation()` (function)
- `fn test_infer_tool_result_depends_on_tool_call()` (function)
- `fn test_infer_assistant_depends_on_tool_result()` (function)
- `fn test_compress_skeleton_tool_result()` (function)
- `fn test_compress_digest()` (function)
- `fn test_compress_fingerprint()` (function)
- `fn test_progressive_no_compression_below_70pct()` (function)
- `fn test_progressive_tool_results_skeleton_at_75pct()` (function)
- `fn test_progressive_aggressive_at_92pct()` (function)
- `fn test_resolution_ordering()` (function)
- `fn test_200_blocks_under_100ms()` (function)
- `fn test_forward_overlap_recent_block_gets_default()` (function)
- `fn test_noise_penalty_reduces_value_of_noisy_blocks()` (function)
- `fn test_non_sequential_block_indices_no_panic()` (function)
- `fn test_budget_zero()` (function)
- `fn test_budget_exceeds_total()` (function)
- `fn test_compress_block_empty_content()` (function)
- `fn test_negative_decay_lambda_clamped()` (function)
- `fn test_forward_overlap_multiple_blocks()` (function)
- `fn test_progressive_thresholds_position_based_recency()` (function)
- `fn stress_random_indices_never_panic()` (function)
- `fn stress_budget_boundaries()` (function)
- `fn stress_protected_messages_invariant()` (function)
- `fn stress_compress_all_resolutions_all_kinds()` (function)
- `fn stress_dag_coherence_post_pruning()` (function)
- `fn stress_500_blocks_under_200ms()` (function)
- `fn stress_progressive_thresholds_all_utilizations()` (function)
- `fn stress_forward_overlap_correctness()` (function)
