---
claim_id: c0abf9e6-3de3-4971-b2de-ec6de3d9280c
entity: needle_heatmap
status: inferred
confidence: 0.75
sources:
  - bench/needle_heatmap.py:29
  - bench/needle_heatmap.py:47
  - bench/needle_heatmap.py:107
  - bench/needle_heatmap.py:163
last_checked: 2026-04-14T04:12:29.389047+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: needle_heatmap

**Language:** python
**Lines of code:** 194


## Functions
- `def generate_heatmap(
    results: dict,
    output_path: str = "needle_heatmap.png",
    title: str = "NeedleInAHaystack: Entroly vs Baseline",
)`
- `def build_matrix(data)`
- `def run_needle_sweep(
    model: str = "gpt-4o-mini",
    sizes: list[int] | None = None,
    depths: list[float] | None = None,
    budget: int = 50_000,
) -> dict`
- `def main()`

## Dependencies
- `__future__`
- `json`
- `os`
- `pathlib`
- `sys`
