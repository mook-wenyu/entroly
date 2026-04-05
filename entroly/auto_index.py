"""
Entroly Auto-Index — Git-aware codebase discovery and ingestion.

On first startup (or when no persistent index exists), automatically
walks all git-tracked files, ingests relevant source code, and builds
the dependency graph. Zero manual configuration needed.

Usage:
    from entroly.auto_index import auto_index
    auto_index(engine)  # Ingests all git-tracked source files
"""

from __future__ import annotations

import logging
import os
import subprocess
import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entroly.server import EntrolyEngine

logger = logging.getLogger("entroly")

# File extensions to index (covers 95%+ of production codebases)
SUPPORTED_EXTENSIONS = frozenset({
    # Systems
    ".rs", ".c", ".cpp", ".h", ".hpp", ".cc", ".hxx", ".zig",
    # Web / JS / TS
    ".js", ".ts", ".jsx", ".tsx", ".mjs", ".mts", ".cjs", ".cts",
    ".vue", ".svelte",
    # Python
    ".py", ".pyi",
    # JVM
    ".java", ".kt", ".scala",
    # .NET / C#
    ".cs", ".csx", ".fs",
    # Go
    ".go",
    # Swift / iOS
    ".swift",
    # Ruby
    ".rb",
    # PHP
    ".php",
    # Dart / Flutter
    ".dart",
    # Elixir / Erlang
    ".ex", ".exs",
    # Lua
    ".lua",
    # R
    ".r",
    # Shell / Config
    ".sh", ".bash", ".zsh",
    ".toml", ".yaml", ".yml", ".json",
    # Terraform / IaC
    ".tf", ".hcl",
    # Docs that matter
    ".md", ".rst",
    # SQL
    ".sql",
    # Docker / CI
    ".dockerfile",
})

# Files to always skip regardless of extension
SKIP_PATTERNS = frozenset({
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Cargo.lock",
    "poetry.lock", "Pipfile.lock", "composer.lock", "Gemfile.lock",
    ".DS_Store", "thumbs.db",
})

# Max file size to ingest (50 KB — larger files are usually generated)
MAX_FILE_BYTES = 50 * 1024

# Gap #45: Hard ceiling for massive files (500 KB) — never even attempt to read
ABSOLUTE_MAX_BYTES = 500 * 1024

# Gap #46: Binary/media file extensions — skip without error
BINARY_EXTENSIONS = frozenset({
    # Images
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".ico", ".svg", ".webp", ".tiff",
    # Audio/Video
    ".mp3", ".mp4", ".avi", ".mov", ".wav", ".flac", ".ogg", ".webm",
    # Archives
    ".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".xz",
    # Compiled/Binary
    ".wasm", ".so", ".dll", ".dylib", ".a", ".o", ".obj", ".exe", ".bin",
    ".pyc", ".pyo", ".class", ".jar",
    # Documents/Media
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    # Fonts
    ".ttf", ".otf", ".woff", ".woff2", ".eot",
    # Database
    ".db", ".sqlite", ".sqlite3",
    # Other binary
    ".dat", ".pak", ".map",
})

# Max files to index in a single pass (configurable via ENTROLY_MAX_FILES)
MAX_FILES = int(os.environ.get("ENTROLY_MAX_FILES", "5000"))


def _git_ls_files(project_dir: str) -> list[str]:
    """Get all git-tracked files, respecting .gitignore."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0:
            return [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass
    return []


def _walk_fallback(project_dir: str) -> list[str]:
    """Fallback file discovery when git is not available."""
    files = []
    for root, dirs, filenames in os.walk(project_dir):
        # Skip hidden dirs, node_modules, __pycache__, .git, etc.
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".")
            and d not in {"node_modules", "__pycache__", "target", "dist",
                         "build", ".git", "venv", ".venv", "env"}
        ]
        for fname in filenames:
            rel = os.path.relpath(os.path.join(root, fname), project_dir)
            files.append(rel)
            if len(files) >= MAX_FILES:
                return files
    return files


def _load_entrolyignore(project_dir: str) -> list[str]:
    """Load .entrolyignore patterns (one glob per line, like .gitignore).

    Supports simple glob patterns: *.generated.ts, vendor/**, test_fixtures/*
    """
    ignore_path = os.path.join(project_dir, ".entrolyignore")
    if not os.path.isfile(ignore_path):
        return []
    try:
        with open(ignore_path) as f:
            return [
                line.strip() for line in f
                if line.strip() and not line.startswith("#")
            ]
    except OSError:
        return []


# Module-level cache for ignore patterns (set per auto_index call)
_ignore_patterns: list[str] = []


def _matches_ignore(rel_path: str) -> bool:
    """Check if a path matches any .entrolyignore pattern."""
    import fnmatch
    for pattern in _ignore_patterns:
        if fnmatch.fnmatch(rel_path, pattern):
            return True
        # Also match against basename for patterns like "*.generated.ts"
        if fnmatch.fnmatch(os.path.basename(rel_path), pattern):
            return True
    return False


def _should_index(rel_path: str) -> bool:
    """Decide whether a file should be indexed."""
    basename = os.path.basename(rel_path)

    # Skip lock files and system files
    if basename in SKIP_PATTERNS:
        return False

    # Gap #46: Skip binary/media files cleanly
    _, ext = os.path.splitext(basename)
    if ext.lower() in BINARY_EXTENSIONS:
        return False

    # Gap #35: .entrolyignore support
    if _ignore_patterns and _matches_ignore(rel_path):
        return False

    # Dockerfile special case (no extension)
    if basename.startswith("Dockerfile"):
        return True

    # Check extension
    return ext.lower() in SUPPORTED_EXTENSIONS


def _estimate_tokens(content: str) -> int:
    """Fast token estimation: ~4 chars per token for code."""
    return max(1, len(content) // 4)


def auto_index(
    engine: EntrolyEngine,
    project_dir: str | None = None,
    force: bool = False,
) -> dict:
    """Auto-index a project's codebase into the Entroly engine.

    Args:
        engine: The EntrolyEngine instance to index into.
        project_dir: Root directory to scan. Defaults to cwd.
        force: If True, re-index even if fragments already exist.

    Returns:
        Summary dict with indexed file count, token count, and duration.
    """
    project_dir = project_dir or os.getcwd()
    project_dir = os.path.abspath(project_dir)

    # Gap #35: Load .entrolyignore patterns
    global _ignore_patterns
    _ignore_patterns = _load_entrolyignore(project_dir)
    if _ignore_patterns:
        logger.info(f".entrolyignore loaded: {len(_ignore_patterns)} patterns")

    # Skip if engine already has fragments (loaded from persistent index)
    if not force and engine._use_rust:
        existing = engine._rust.fragment_count()
        if existing > 0:
            logger.info(
                f"Auto-index skipped: {existing} fragments already loaded "
                f"from persistent index"
            )
            return {
                "status": "skipped",
                "reason": "persistent_index_loaded",
                "existing_fragments": existing,
            }

    t0 = time.perf_counter()

    # Discover files
    files = _git_ls_files(project_dir)
    if not files:
        files = _walk_fallback(project_dir)
        discovery = "walk"
    else:
        discovery = "git"

    # Filter to indexable files
    all_indexable = [f for f in files if _should_index(f)]
    if len(all_indexable) > MAX_FILES:
        logger.warning(
            f"Codebase has {len(all_indexable)} indexable files, capping at {MAX_FILES}. "
            f"Set ENTROLY_MAX_FILES to increase the limit."
        )
    indexable = all_indexable[:MAX_FILES]

    # Parallel file reading for I/O-bound speedup
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _read_file(rel_path: str) -> tuple | None:
        """Read a single file. Returns (content, rel_path, tokens) or None."""
        abs_path = os.path.join(project_dir, rel_path)
        try:
            size = os.path.getsize(abs_path)
            # Gap #45: Hard ceiling — never read massive files
            if size > ABSOLUTE_MAX_BYTES:
                logger.debug(f"Skipping massive file ({size:,}B): {rel_path}")
                return ("skip_size",)
            if size > MAX_FILE_BYTES or size == 0:
                return ("skip_size",) if size > MAX_FILE_BYTES else None
        except OSError:
            return None
        # Gap #46: Quick binary detection — check for null bytes in first 8KB
        try:
            with open(abs_path, "rb") as fb:
                header = fb.read(8192)
                if b"\x00" in header:
                    return ("skip_read",)  # Binary file
        except OSError:
            return ("skip_read",)
        try:
            with open(abs_path, encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except (OSError, UnicodeDecodeError):
            return ("skip_read",)
        if not content.strip():
            return None
        tokens = _estimate_tokens(content)
        return (content, rel_path, tokens)

    indexed = 0
    total_tokens = 0
    skipped_size = 0
    skipped_read = 0

    max_workers = min(8, (os.cpu_count() or 4))
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_read_file, rp): rp for rp in indexable}
        for future in as_completed(futures):
            result_data = future.result()
            if result_data is None:
                continue
            if result_data == ("skip_size",):
                skipped_size += 1
                continue
            if result_data == ("skip_read",):
                skipped_read += 1
                continue

            content, rel_path, tokens = result_data
            engine.ingest_fragment(
                content=content,
                source=f"file:{rel_path}",
                token_count=tokens,
                is_pinned=False,
            )
            indexed += 1
            total_tokens += tokens

    elapsed = time.perf_counter() - t0

    # Build dependency graph from import analysis
    if engine._use_rust and indexed > 0:
        try:
            # Trigger a lightweight optimize to build the dep graph
            # (dep graph is built during optimize, not ingest)
            engine.optimize_context(token_budget=1, query="")
        except Exception:
            pass  # Non-critical, dep graph will build on first real optimize

    logger.info(
        f"Auto-indexed {indexed} files ({total_tokens:,} tokens) "
        f"in {elapsed:.1f}s via {discovery} "
        f"[skipped: {skipped_size} too large, {skipped_read} unreadable]"
    )

    return {
        "status": "indexed",
        "files_indexed": indexed,
        "total_tokens": total_tokens,
        "duration_s": round(elapsed, 2),
        "discovery_method": discovery,
        "skipped_too_large": skipped_size,
        "skipped_unreadable": skipped_read,
        "project_dir": project_dir,
    }


def start_incremental_watcher(
    engine: EntrolyEngine,
    project_dir: str | None = None,
    interval_s: int = 120,
) -> None:
    """Start a background thread that periodically re-scans for new/modified files.

    Addresses the stale-index problem: files created or modified during a session
    are picked up without restarting the server.
    """
    import threading

    project_dir = project_dir or os.getcwd()
    project_dir = os.path.abspath(project_dir)

    # Track what we've already indexed (by mtime)
    _indexed_mtimes: dict[str, float] = {}

    def _initial_snapshot():
        """Capture mtimes of all currently indexed files."""
        files = _git_ls_files(project_dir) or []
        for rel_path in files:
            abs_path = os.path.join(project_dir, rel_path)
            try:
                _indexed_mtimes[rel_path] = os.path.getmtime(abs_path)
            except OSError:
                pass

    def _scan_loop():
        _initial_snapshot()
        while True:
            time.sleep(interval_s)
            try:
                _incremental_scan()
            except Exception as e:
                logger.debug(f"Incremental re-index error: {e}")

    def _incremental_scan():
        files = _git_ls_files(project_dir) or []
        new_or_modified = []

        for rel_path in files:
            if not _should_index(rel_path):
                continue
            abs_path = os.path.join(project_dir, rel_path)
            try:
                mtime = os.path.getmtime(abs_path)
            except OSError:
                continue
            prev_mtime = _indexed_mtimes.get(rel_path)
            if prev_mtime is None or mtime > prev_mtime:
                new_or_modified.append(rel_path)
                _indexed_mtimes[rel_path] = mtime

        if not new_or_modified:
            return

        count = 0
        for rel_path in new_or_modified[:100]:  # cap per scan
            abs_path = os.path.join(project_dir, rel_path)
            try:
                size = os.path.getsize(abs_path)
                if size > MAX_FILE_BYTES or size == 0:
                    continue
                with open(abs_path, encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                if not content.strip():
                    continue
                tokens = _estimate_tokens(content)
                engine.ingest_fragment(
                    content=content,
                    source=f"file:{rel_path}",
                    token_count=tokens,
                    is_pinned=False,
                )
                count += 1
            except (OSError, UnicodeDecodeError):
                continue

        if count > 0:
            logger.info(f"Incremental re-index: {count} new/modified files ingested")

    t = threading.Thread(target=_scan_loop, daemon=True, name="entroly-watcher")
    t.start()
    logger.info(f"File watcher started (re-scan every {interval_s}s)")
