"""
Entroly — Information-Theoretic Context Optimization for Agentic AI
========================================================================

An MCP server that mathematically optimizes what goes into an LLM's
context window. Uses knapsack dynamic programming, Shannon entropy scoring,
SimHash deduplication, and predictive pre-fetching to cut token costs by
50–70% while improving agent accuracy.

Quick Setup (Cursor)::

    Add to .cursor/mcp.json:
    {
      "mcpServers": {
        "entroly": {
          "command": "entroly"
        }
      }
    }

Quick Setup (Claude Code)::

    claude mcp add entroly -- entroly

"""

from pathlib import Path

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover - Python <3.8 compatibility
    PackageNotFoundError = Exception  # type: ignore[assignment]
    version = None  # type: ignore[assignment]

_FALLBACK_VERSION = "0.8.5"


def _read_source_version() -> str | None:
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    if not pyproject_path.exists():
        return None

    in_project = False
    for raw_line in pyproject_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "[project]":
            in_project = True
            continue
        if in_project and line.startswith("["):
            return None
        if not in_project or "=" not in line:
            continue

        key, _, value = line.partition("=")
        if key.strip() == "version":
            return value.strip().strip('"').strip("'")
    return None


def _read_installed_version() -> str | None:
    if version is None:
        return None
    try:
        return version("entroly")
    except PackageNotFoundError:
        return None


__version__ = _read_source_version() or _read_installed_version() or _FALLBACK_VERSION

# SDK: 3-line integration for any AI application
try:
    from .sdk import compress, compress_messages  # noqa: F401
except ImportError:
    pass  # Graceful degradation if dependencies missing
