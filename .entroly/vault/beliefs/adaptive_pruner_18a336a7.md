---
claim_id: 18a336a708495a4c0860f04c
entity: adaptive_pruner
status: stale
confidence: 0.75
sources:
  - entroly\adaptive_pruner.py:38
  - entroly\adaptive_pruner.py:49
  - entroly\adaptive_pruner.py:58
  - entroly\adaptive_pruner.py:81
  - entroly\adaptive_pruner.py:127
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: adaptive_pruner

**LOC:** 161

## Entities
- `class EntrolyPruner:` (class)
- `def __init__(self)` (function)
- `def available(self) -> bool` (function)
- `def apply_feedback(self, fragment_id: str, feedback: float) -> bool` (function)
- `class FragmentGuard:` (class)
- `def __init__(self)` (function)
- `def available(self) -> bool` (function)
- `def scan(self, content: str, source: str = "") -> list[str]` (function)
