---
claim_id: 798fa2fd-c6da-4ec6-8aa0-575266768423
entity: demo_value
status: inferred
confidence: 0.75
sources:
  - examples\demo_value.py:27
  - examples\demo_value.py:46
  - examples\demo_value.py:52
  - examples\demo_value.py:61
  - examples\demo_value.py:68
  - examples\demo_value.py:71
  - examples\demo_value.py:74
  - examples\demo_value.py:151
  - examples\demo_value.py:81
  - examples\demo_value.py:94
last_checked: 2026-04-14T04:12:09.413931+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: demo_value

**Language:** python
**Lines of code:** 403

## Types
- `class C()`

## Functions
- `def bar(value, max_val, width=30, color=C.GREEN)` — Render a Unicode progress bar.
- `def sparkline(values, color=C.CYAN)` — Render a sparkline chart from a list of values.
- `def header(text, width=72)` — Render a styled header.
- `def subheader(text)`
- `def metric(label, value, color=C.WHITE, indent=4)`
- `def divider(char="─", width=72)`
- `def run_demo()`

## Dependencies
- `json`
- `sys`
- `time`
