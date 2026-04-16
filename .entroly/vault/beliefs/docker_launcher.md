---
claim_id: 7f0cc7e4-f09f-41c5-8088-b17428a56ee1
entity: _docker_launcher
status: inferred
confidence: 0.75
sources:
  - entroly/_docker_launcher.py:90
  - entroly/_docker_launcher.py:22
last_checked: 2026-04-14T04:12:29.392685+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: _docker_launcher

**Language:** python
**Lines of code:** 194


## Functions
- `def launch() -> None` — Main entry point — docker launch or native fallback. Routes CLI subcommands (init, dashboard, health, autotune, benchmark, status, proxy) to the local CLI handler. Only `serve` and bare `entroly` go t

## Dependencies
- `__future__`
- `os`
- `pathlib`
- `subprocess`
- `sys`
- `time`
