---
claim_id: 18a336a71535a0a8154d36a8
entity: autotune
status: stale
confidence: 0.75
sources:
  - entroly-wasm\js\autotune.js:31
  - entroly-wasm\js\autotune.js:122
  - entroly-wasm\js\autotune.js:134
  - entroly-wasm\js\autotune.js:149
  - entroly-wasm\js\autotune.js:282
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: autotune

**LOC:** 627

## Entities
- `class FeedbackJournal {` (class)
- `function extractWeights(w) {` (function)
- `function normalizeWeights(w) {` (function)
- `function optimize(episodes, currentWeights) {` (function)
- `function computeExplorationBonus(episodes) {` (function)
- `function findConfigPath() {` (function)
- `function loadConfig() {` (function)
- `function saveConfig(config) {` (function)
- `function optimizeFromJournal(checkpointDir) {` (function)
- `function hotReloadWeights(engine) {` (function)
- `function startAutotuneDaemon(engine, checkpointDir, intervalMs = 30000) {` (function)
- `function runAutotune() {` (function)
- `function classifyQuery(query) {` (function)
- `class TaskProfileOptimizer {` (class)
