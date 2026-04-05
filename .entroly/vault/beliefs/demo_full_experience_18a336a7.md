---
claim_id: 18a336a7307b6d4830930348
entity: demo_full_experience
status: inferred
confidence: 0.75
sources:
  - examples\demo_full_experience.py:18
  - examples\demo_full_experience.py:56
  - examples\demo_full_experience.py:63
  - examples\demo_full_experience.py:73
  - examples\demo_full_experience.py:78
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: demo_full_experience

**LOC:** 781

## Entities
- `class S:` (class)
- `def get_user(user_id)` (function)
- `def delete_user(user_id)` (function)
- `def parameterized_query(cursor, query, params)` (function)
- `def build_where_clause(filters: dict) -> tuple[str, list]` (function)
- `class User:` (class)
- `def verify_password(self, password: str) -> bool` (function)
- `def has_permission(self, permission: str) -> bool` (function)
- `def send_welcome_email(user)` (function)
- `def app()` (function)
- `def client(app)` (function)
- `def db(app)` (function)
- `def validate_email(email: str) -> bool` (function)
- `def validate_phone(phone: str) -> bool` (function)
- `def validate_password(pw: str) -> tuple[bool, str]` (function)
- `def render_homepage()` (function)
- `def api_health()` (function)
- `def get_user(user_id)` (function)
- `def delete_user(user_id)` (function)
- `def act1_the_pain()` (function)
- `def act2_installation()` (function)
- `def act3_real_engine()` (function)
- `def act4_dashboard(engine)` (function)
- `def act5_autotuner()` (function)
- `def main()` (function)
