---
claim_id: 18a336a70f6343d80f7ad9d8
entity: test_brutal
status: inferred
confidence: 0.75
sources:
  - entroly-core\tests\test_brutal.py:23
  - entroly-core\tests\test_brutal.py:53
  - entroly-core\tests\test_brutal.py:54
  - entroly-core\tests\test_brutal.py:59
  - entroly-core\tests\test_brutal.py:68
last_checked: 2026-04-04T17:12:49Z
derived_from:
  - cogops_compiler
---

# Module: test_brutal

**LOC:** 732

## Entities
- `def test(name, fn)` (function)
- `class PaymentProcessor:` (class)
- `def __init__(self, db_conn, fee_pct: float = 0.029)` (function)
- `def process(self, amount: decimal.Decimal, currency: Currency,` (function)
- `def refund(self, txn_id: str) -> bool` (function)
- `def get_exchange_rate(from_currency: str, to_currency: str) -> float` (function)
- `class Currency:` (class)
- `class Transaction:` (class)
- `def total_charged(self) -> float` (function)
- `def generate_token(user_id: int, expiry_seconds: int = 3600) -> str` (function)
- `def verify_token(token: str) -> Optional[int]` (function)
- `class DatabaseConnection:` (class)
- `def __init__(self, dsn: str)` (function)
- `def connect(self)` (function)
- `def save(self, obj: Any) -> None` (function)
- `def get(self, txn_id: str) -> Optional[Any]` (function)
- `def db()` (function)
- `def processor(db)` (function)
- `def test_process_payment_usd(processor, db)` (function)
- `def test_refund_success(processor, db)` (function)
- `def test_refund_already_refunded(processor, db)` (function)
- `def test_real_session_full()` (function)
- `def test_selection_respects_dependency_ordering()` (function)
- `def test_budget_forces_tradeoffs()` (function)
- `def test_budget_with_pinned_overflow()` (function)
- `def test_budget_one_token()` (function)
- `def test_duplicate_updates_existing()` (function)
- `def test_many_duplicates_accumulate()` (function)
- `def test_whitespace_variants_not_deduped()` (function)
- `def test_feedback_convergence()` (function)
- `def test_feedback_negative_suppresses()` (function)
- `def test_explain_scores_are_bounded()` (function)
- `def test_explain_critical_marked()` (function)
- `def test_explain_consistency_with_optimize()` (function)
- `def test_export_import_produces_same_optimize()` (function)
- `def test_export_import_preserves_feedback()` (function)
- `def test_sufficiency_full_deps_present()` (function)
- `def test_sufficiency_missing_definition_warns()` (function)
- `def test_dep_boost_changes_selection()` (function)
- `def test_exploration_fires_over_many_calls()` (function)
- `def test_no_exploration_when_rate_zero()` (function)
- `def test_ingest_1000_fragments()` (function)
- `def test_optimize_1000_fragments()` (function)
- `def test_rapid_advance_turns()` (function)
- `def test_recall_semantic_ranking()` (function)
- `def test_recall_top_k_respected()` (function)
- `def test_auth_content_safety()` (function)
