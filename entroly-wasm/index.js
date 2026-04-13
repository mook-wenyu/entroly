// Entroly — Information-theoretic context optimization for JavaScript/TypeScript.
// 
// Usage:
//   const { EntrolyEngine, autoIndex, EntrolyConfig } = require('entroly-wasm');
//
//   const engine = new EntrolyEngine();
//   autoIndex(engine);   // auto-discover and ingest codebase
//   engine.optimize(8000, "fix the auth bug");
//
// Or as MCP server:
//   npx entroly-wasm serve

const { WasmEntrolyEngine } = require('./pkg/entroly_wasm');
const { EntrolyConfig } = require('./js/config');
const { autoIndex, startIncrementalWatcher, estimateTokens } = require('./js/auto_index');
const { CheckpointManager, persistIndex, loadIndex } = require('./js/checkpoint');
const { EntrolyMCPServer } = require('./js/server');
const { runAutotune, startAutotuneDaemon, TaskProfileOptimizer, FeedbackJournal } = require('./js/autotune');
const { ValueTracker, EVOLUTION_TAX_RATE, estimateCost } = require('./js/value_tracker');
const { exportPromoted: exportAgentSkills } = require('./js/agentskills_export');
const { TelegramGateway, DiscordGateway, SlackGateway } = require('./js/gateways');
const { VaultObserver } = require('./js/vault_observer');

module.exports = {
  // Core engine (wasm)
  EntrolyEngine: WasmEntrolyEngine,
  WasmEntrolyEngine,

  // Configuration
  EntrolyConfig,

  // Codebase scanning
  autoIndex,
  startIncrementalWatcher,
  estimateTokens,

  // State persistence
  CheckpointManager,
  persistIndex,
  loadIndex,

  // MCP Server
  EntrolyMCPServer,

  // Autotune + Task-Conditioned Profiles
  runAutotune,
  startAutotuneDaemon,
  TaskProfileOptimizer,
  FeedbackJournal,

  // Self-funded evolution budget (C_spent ≤ τ·S(t))
  ValueTracker,
  EVOLUTION_TAX_RATE,
  estimateCost,

  // agentskills.io portable export
  exportAgentSkills,

  // Chat gateways (live self-evolution event stream)
  TelegramGateway,
  DiscordGateway,
  SlackGateway,

  // Observe the shared vault — works with skills promoted by the
  // Python daemon OR any node-side orchestrator. No daemon required.
  VaultObserver,
};
