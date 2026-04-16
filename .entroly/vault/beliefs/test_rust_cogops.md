---
claim_id: 28131433-a651-4be0-89a6-d22a75802715
entity: test_rust_cogops
status: stale
confidence: 0.75
sources:
  - tests\test_rust_cogops.py:28
  - tests\test_rust_cogops.py:7
  - tests\test_rust_cogops.py:30
  - tests\test_rust_cogops.py:32
  - tests\test_rust_cogops.py:6
last_checked: 2026-04-14T04:12:09.438986+00:00
derived_from:
  - belief_compiler
  - sast
---

# Module: test_rust_cogops

**Language:** python
**Lines of code:** 133

## Types
- `class AuthService()` — Handles authentication.

## Functions
- `def check(name, cond)`
- `def verify_token(self, token: str) -> bool`
- `def rotate_keys(self)` — entities = e.extract_entities(py_code, "auth_service.py") check("Python extraction", len(entities) >= 2) names = [x["name"] for x in entities] check("Found AuthService", "AuthService" in names) check(

## Dependencies
- `entroly_core`
- `json`
- `tempfile`

## Linked Beliefs
- [[entroly_core]]
