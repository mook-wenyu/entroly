---
claim_id: 18a336a70bc95f280be0f528
entity: proxy_transform
status: stale
confidence: 0.75
sources:
  - entroly\proxy_transform.py:62
  - entroly\proxy_transform.py:103
  - entroly\proxy_transform.py:121
  - entroly\proxy_transform.py:245
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: proxy_transform

**LOC:** 860

## Entities
- `def extract_user_message(body: Dict[str, Any], provider: str) -> str` (function)
- `def extract_model(body: Dict[str, Any], path: str = "") -> str` (function)
- `def compute_token_budget(model: str, config: ProxyConfig) -> int` (function)
- `def calibrated_token_count(content: str, source: str = "") -> int` (function)
