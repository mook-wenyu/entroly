---
claim_id: 0b9113ae-5bc2-442f-95a2-c073ded9005d
entity: sdk
status: inferred
confidence: 0.75
sources:
  - entroly/sdk.py:36
  - entroly/sdk.py:88
last_checked: 2026-04-14T04:12:29.498157+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: sdk

**Language:** python
**Lines of code:** 248


## Functions
- `def compress(
    content: str,
    budget: int | None = None,
    content_type: str | None = None,
    target_ratio: float = 0.3,
) -> str`
- `def compress_messages(
    messages: list[dict[str, Any]],
    budget: int = 50_000,
    preserve_last_n: int = 4,
) -> list[dict[str, Any]]`

## Dependencies
- `.universal_compress`
- `__future__`
- `typing`
