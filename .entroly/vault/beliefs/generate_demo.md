---
claim_id: d15c28ec-e3f1-44a8-9467-083a291accad
entity: generate_demo
status: inferred
confidence: 0.75
sources:
  - docs/generate_demo.py:135
  - docs/generate_demo.py:215
  - docs/generate_demo.py:389
  - docs/generate_demo.py:26
  - docs/generate_demo.py:43
  - docs/generate_demo.py:122
  - docs/generate_demo.py:123
  - docs/generate_demo.py:124
  - docs/generate_demo.py:125
  - docs/generate_demo.py:126
last_checked: 2026-04-14T04:12:29.390631+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: generate_demo

**Language:** python
**Lines of code:** 416


## Functions
- `def generate_svg() -> str` — Generate an animated SVG terminal recording with SMIL animations.
- `def generate_html() -> str` — Generate an interactive HTML page with the terminal animation.
- `def main()`

## Dependencies
- `__future__`
- `argparse`
- `math`
- `pathlib`
- `sys`
