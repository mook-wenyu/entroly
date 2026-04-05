---
claim_id: 18a33f4c_auto_index_01
entity: auto_index
status: inferred
confidence: 0.75
sources:
  - auto_index.py:28
  - auto_index.py:107
  - auto_index.py:177
  - auto_index.py:207
  - auto_index.py:356
last_checked: 2026-04-04T21:00:00Z
derived_from:
  - cogops_compiler
  - sast
  - server_18a33f4c
epistemic_layer: belief
---

# Module: auto_index

**Language:** py
**Lines of code:** 441

Git-aware codebase discovery and ingestion module. On first startup (or when no persistent index exists), walks all git-tracked files, ingests relevant source code, and builds the dependency graph with zero manual configuration.

## Types
- `SUPPORTED_EXTENSIONS` -- Frozen set of 50+ file extensions covering systems, web, JVM, .NET, Go, Swift, Ruby, PHP, Dart, Elixir, Lua, R, shell, IaC, docs, and SQL.
- `SKIP_PATTERNS` -- Lock files and OS artifacts to always skip.
- `BINARY_EXTENSIONS` -- Images, audio/video, archives, compiled, fonts, databases to skip without error.

## Functions
- `_git_ls_files(project_dir: str) -> list[str]` -- Gets all git-tracked files respecting .gitignore via `git ls-files`.
- `_walk_fallback(project_dir: str) -> list[str]` -- Fallback file discovery via os.walk when git is unavailable, skipping hidden dirs and common vendor directories.
- `_load_entrolyignore(project_dir: str) -> list[str]` -- Loads .entrolyignore glob patterns (one per line, like .gitignore).
- `_matches_ignore(rel_path: str) -> bool` -- Checks if a path matches any .entrolyignore pattern using fnmatch.
- `_should_index(rel_path: str) -> bool` -- Central indexing decision: checks skip patterns, binary extensions, .entrolyignore, Dockerfile special case, and supported extensions.
- `_estimate_tokens(content: str) -> int` -- Fast token estimation at ~4 chars per token.
- `auto_index(engine, project_dir, force) -> dict` -- Main entry point. Discovers files via git or walk fallback, reads them in parallel with ThreadPoolExecutor (up to 8 workers), ingests via engine.ingest_fragment, then triggers dep graph build. Returns summary with file count, tokens, duration.
- `start_incremental_watcher(engine, project_dir, interval_s) -> None` -- Starts a daemon thread that periodically re-scans for new/modified files by tracking mtimes, ingesting up to 100 changed files per scan cycle.

## Related Modules
- [[server_18a33f4c]] -- EntrolyEngine that auto_index ingests fragments into
- [[fragment_18a33f4c]] -- Fragment type that gets created during ingestion
- [[depgraph_18a33f4c]] -- Dependency graph built after indexing completes
- [[config_18a33f4c]] -- Configuration for MAX_FILES via ENTROLY_MAX_FILES env var
- [[change_listener_18a33f4c]] -- Complementary change detection for the evolution layer
