---
claim_id: a8c9d7f6_cogops_epistemic
entity: cogops_epistemic_engine
status: inferred
confidence: 0.85
sources:
  - entroly-core/src/cogops.rs:1
  - entroly-core/src/cogops.rs:170
  - entroly-core/src/cogops.rs:186
  - entroly-core/src/cogops.rs:218
last_checked: 2026-04-04T12:00:00Z
derived_from:
  - cogops_18a33f4c
  - epistemic_router_18a33f4c
  - belief_compiler_18a33f4c
epistemic_layer: action
---

# CogOps: The Epistemic Engine Parallel to Context Optimization

CogOps (cogops.rs) is a complete second engine alongside EntrolyEngine. While EntrolyEngine optimizes WHAT context to show the LLM, CogOps manages the KNOWLEDGE layer — beliefs about the codebase that persist across sessions.

## Architecture: Six Sub-Engines

1. **EpistemicRouter** — Intent classification + flow routing. 12 intent types (Architecture, PrBrief, CodeGeneration, etc.) mapped to 5 epistemic flows (FastAnswer, VerifyBefore, CompileOnDemand, ChangeDriven, SelfImprovement). Uses zero-allocation keyword scan (cogops.rs:170).

2. **BeliefCompiler** — Extracts code entities (functions, classes, structs, traits, enums) from source code and compiles them into belief artifacts with claim_id, confidence, sources, and derived_from chains.

3. **VerificationEngine** — Contradiction detection, staleness checking, blast radius estimation. Checks whether existing beliefs are still consistent with current code.

4. **ChangePipeline** — Diff analysis, PR briefs, code review findings. Maps file changes to affected beliefs.

5. **FlowOrchestrator** — Chains the 5 canonical flows end-to-end.

6. **SkillEngine** — Skill synthesis, benchmarking, promotion.

## The Two-System Design

EntrolyEngine and CogOpsEngine operate at different time scales:
- **EntrolyEngine**: Per-query, per-turn. Optimizes context window for immediate LLM call.
- **CogOpsEngine**: Per-session, per-commit. Manages durable knowledge that survives across conversations.

They share no state at runtime. CogOps reads/writes the vault (filesystem), while EntrolyEngine operates entirely in memory. The bridge is that CogOps-compiled beliefs can be ingested as context fragments by EntrolyEngine.

## Entity Extraction: Pattern-Based, No Dependencies

Entity extraction (cogops.rs:218) uses pure string matching — no regex, no tree-sitter, no AST parsing. Supports Python, Rust, and JavaScript/TypeScript. This is intentional: the extraction needs to be fast (runs on every ingestion) and dependency-free (the Rust core has minimal dependencies).

The trade-off is lower extraction quality for complex syntax (nested classes, decorators, generics). But for the belief compilation use case, signatures and names are sufficient — the full content is in the fragment itself.

## Risk Assessment

Risk level (Low/Medium/High) is assessed from query keywords (cogops.rs:200). High-risk keywords include security, vulnerability, PII, compliance terms. This gates whether the VerifyBefore flow is triggered, adding an extra verification step before answering security-sensitive queries.

## Related Modules

- **Modules:** [[belief_compiler_18a33f4c]], [[cogops_18a33f4c]], [[epistemic_router_18a33f4c]], [[flow_orchestrator_18a33f4c]], [[vault_18a33f4c]]
