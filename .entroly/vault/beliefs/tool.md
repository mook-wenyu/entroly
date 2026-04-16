---
claim_id: f909a01a-0906-4f2c-8490-567077d0fb5c
entity: tool
status: inferred
confidence: 0.75
sources:
  - .entroly/vault/evolution/skills/ddb2e2969bb0/tool.py:11
  - .entroly/vault/evolution/skills/ddb2e2969bb0/tool.py:16
  - .entroly/vault/evolution/skills/ddb2e2969bb0/tool.py:8
last_checked: 2026-04-14T04:12:29.379629+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: tool

**Language:** python
**Lines of code:** 24


## Functions
- `def matches(query: str) -> bool` — Check if this skill should handle the query.
- `def execute(query: str, context: dict) -> dict` — Execute the skill logic.

## Dependencies
- `re`
