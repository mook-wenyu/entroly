---
claim_id: 586f0565-9927-4e20-a96d-392c03a2f557
entity: evolution_daemon
status: inferred
confidence: 0.75
sources:
  - entroly/evolution_daemon.py:51
  - entroly/evolution_daemon.py:65
  - entroly/evolution_daemon.py:108
  - entroly/evolution_daemon.py:122
  - entroly/evolution_daemon.py:129
  - entroly/evolution_daemon.py:144
  - entroly/evolution_daemon.py:270
last_checked: 2026-04-14T04:12:29.452111+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: evolution_daemon

**Language:** python
**Lines of code:** 279

## Types
- `class EvolutionDaemon()` — Background daemon for autonomous self-improvement. Orchestrates the 3 pillars: 1. ROI-gated evolution (ValueTracker budget guardrail) 2. Structural synthesis first ($0), LLM fallback (budget-gated) 3.

## Functions
- `def __init__(
        self,
        vault: Any,
        evolution_logger: Any,
        value_tracker: Any,
        feedback_journal: Any = None,
        rust_engine: Any = None,
    )`
- `def start(self) -> None` — Start the daemon in a background thread.
- `def stop(self) -> None` — Gracefully stop the daemon.
- `def record_activity(self) -> None` — Reset the dreaming idle timer (called on user queries).
- `def run_once(self) -> dict[str, Any]` — Execute one daemon cycle. 1. Process pending skill gaps (structural first, LLM fallback) 2. Dream if idle
- `def stats(self) -> dict[str, Any]` — Return daemon statistics.

## Dependencies
- `__future__`
- `logging`
- `threading`
- `time`
- `typing`
