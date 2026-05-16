"""Regression tests for `swap_model_in_body` (gh#44).

When RAVS routes a request from a Claude 4.5+ model down to a Claude 3.x
model, parameters that the newer generation accepts but the older one
rejects (e.g. ``context_management``, ``thinking``) must be stripped
from the body. Otherwise Anthropic returns

    400 ... context_management: Extra inputs are not permitted

and the user sees the proxy as broken on the very first request that
gets downgraded.
"""

from __future__ import annotations

from entroly.ravs.router import (
    _EXTENDED_ONLY_PARAMS,
    _is_legacy_claude_3,
    swap_model_in_body,
)


# ── _is_legacy_claude_3 ─────────────────────────────────────────────


class TestIsLegacyClaude3:
    def test_haiku_3_is_legacy(self):
        assert _is_legacy_claude_3("claude-3-haiku-20240307")

    def test_haiku_3_5_is_legacy(self):
        assert _is_legacy_claude_3("claude-3-5-haiku-20241022")

    def test_sonnet_3_5_is_legacy(self):
        assert _is_legacy_claude_3("claude-3-5-sonnet-20241022")

    def test_opus_3_is_legacy(self):
        assert _is_legacy_claude_3("claude-3-opus-20240229")

    def test_sonnet_4_5_is_NOT_legacy(self):
        # Future-proofing: never strip extended params from newer models.
        assert not _is_legacy_claude_3("claude-sonnet-4-5-20250929")
        assert not _is_legacy_claude_3("claude-opus-4-5")
        assert not _is_legacy_claude_3("claude-opus-4-7")

    def test_unknown_is_NOT_legacy(self):
        # Defensive: unknown identifier → don't strip (preserve user intent).
        assert not _is_legacy_claude_3("gpt-4o-mini")
        assert not _is_legacy_claude_3("")
        assert not _is_legacy_claude_3("some-custom-model")


# ── swap_model_in_body ──────────────────────────────────────────────


class TestSwapModelInBody:
    def test_basic_swap(self):
        body = {"model": "claude-sonnet-4-5", "messages": []}
        out = swap_model_in_body(body, "claude-3-5-haiku-20241022")
        assert out["model"] == "claude-3-5-haiku-20241022"
        assert out["messages"] == []

    def test_does_not_mutate_input(self):
        body = {"model": "claude-sonnet-4-5", "messages": [], "context_management": {"foo": 1}}
        original = dict(body)
        _ = swap_model_in_body(body, "claude-3-5-haiku-20241022")
        assert body == original, "swap_model_in_body must not mutate input"

    def test_strips_context_management_on_legacy_swap(self):
        """The gh#44 regression: context_management must be removed when
        target is Claude 3.x."""
        body = {
            "model": "claude-sonnet-4-5",
            "messages": [{"role": "user", "content": "hi"}],
            "context_management": {"strategy": "auto"},
            "max_tokens": 1024,
        }
        out = swap_model_in_body(body, "claude-3-5-haiku-20241022")
        assert "context_management" not in out, (
            "context_management leaked into Haiku-3.5 request — Anthropic 400 incoming"
        )
        # Other fields preserved
        assert out["model"] == "claude-3-5-haiku-20241022"
        assert out["messages"] == [{"role": "user", "content": "hi"}]
        assert out["max_tokens"] == 1024

    def test_strips_thinking_on_legacy_swap(self):
        body = {
            "model": "claude-opus-4-5",
            "thinking": {"type": "enabled", "budget_tokens": 8192},
            "messages": [],
        }
        out = swap_model_in_body(body, "claude-3-haiku-20240307")
        assert "thinking" not in out

    def test_preserves_extended_params_on_non_legacy_swap(self):
        """Swapping between two 4.5+ models must NOT strip extended params."""
        body = {
            "model": "claude-opus-4-5",
            "context_management": {"strategy": "auto"},
            "thinking": {"type": "enabled"},
        }
        # Future hypothetical: swap to another 4.5+ model
        out = swap_model_in_body(body, "claude-sonnet-4-5-20250929")
        assert "context_management" in out
        assert "thinking" in out

    def test_preserves_when_target_unknown(self):
        """Defensive: don't strip extended params if we can't classify target."""
        body = {
            "model": "claude-sonnet-4-5",
            "context_management": {"strategy": "auto"},
        }
        out = swap_model_in_body(body, "some-future-model-id")
        assert "context_management" in out

    def test_no_model_field_still_safe(self):
        body = {"messages": [], "context_management": {"x": 1}}
        out = swap_model_in_body(body, "claude-3-5-haiku-20241022")
        # No "model" key to swap, but legacy detector still strips by target
        assert "model" not in out or out["model"] is None or True
        # Critical: the strip still happens based on new_model
        assert "context_management" not in out, (
            "even without source model, target-driven strip must apply"
        )

    def test_all_known_extended_params_stripped(self):
        """Belt-and-suspenders: any future addition to
        _EXTENDED_ONLY_PARAMS must be exercised by this test."""
        body = {"model": "claude-sonnet-4-5"}
        for p in _EXTENDED_ONLY_PARAMS:
            body[p] = {"dummy": True}
        out = swap_model_in_body(body, "claude-3-haiku-20240307")
        for p in _EXTENDED_ONLY_PARAMS:
            assert p not in out, f"{p} leaked through legacy swap"
