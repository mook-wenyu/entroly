"""
AdaptivePruner Bridge for Entroly
======================================

Wires the Rust-backed AdaptivePruner into the feedback loop.

The key addition: `historical_success` — a dimension that entroly's
Rust engine doesn't have. Over time, the RL weight updates learn which
scoring features matter most for THIS user's codebase.

Weight update rule:
    weight += lr * feedback * feature_value  (clamped to [-1, 1])

Falls back to no-op if the Rust backend is not installed.
"""

from __future__ import annotations

from dataclasses import dataclass
import importlib
import logging
from typing import Any

logger = logging.getLogger(__name__)

def _load_optional_class(class_name: str) -> tuple[type[Any] | None, str | None]:
    errors: list[str] = []
    for module_name in ("entroly_core", "ebbiforge_core"):
        try:
            module = importlib.import_module(module_name)
            return getattr(module, class_name), None
        except (ImportError, AttributeError) as exc:
            errors.append(f"{module_name}.{class_name}: {exc}")
    return None, " | ".join(errors)


_RustPruner, _PRUNER_IMPORT_ERROR = _load_optional_class("AdaptivePruner")
_PRUNER_AVAILABLE = _RustPruner is not None

_RustGuard, _GUARD_IMPORT_ERROR = _load_optional_class("CodeQualityGuard")
_GUARD_AVAILABLE = _RustGuard is not None


@dataclass(frozen=True)
class OptionalComponentStatus:
    name: str
    available: bool
    detail: str


def get_optional_component_status() -> dict[str, OptionalComponentStatus]:
    return {
        "adaptive_pruner": OptionalComponentStatus(
            name="AdaptivePruner",
            available=_PRUNER_AVAILABLE,
            detail=(
                "AdaptivePruner 可用"
                if _PRUNER_AVAILABLE
                else (_PRUNER_IMPORT_ERROR or "未安装 native 可选组件")
            ),
        ),
        "fragment_guard": OptionalComponentStatus(
            name="FragmentGuard",
            available=_GUARD_AVAILABLE,
            detail=(
                "CodeQualityGuard 可用"
                if _GUARD_AVAILABLE
                else (_GUARD_IMPORT_ERROR or "未安装 native 可选组件")
            ),
        ),
    }


class EntrolyPruner:
    """
    Adaptive RL pruner with optional Rust backend.

    Extends entroly's Wilson-score feedback with a `historical_success`
    dimension: fragments that previously helped get boosted, those that didn't
    get down-weighted over time.

    Zero-config: if the Rust backend is unavailable, all methods are no-ops.
    """

    def __init__(self):
        self._pruner = _RustPruner() if _PRUNER_AVAILABLE else None
        self._fragment_features: dict[str, dict[str, float]] = {}
        if _PRUNER_AVAILABLE:
            logger.info("AdaptivePruner: Rust backend available -- RL weight learning active")
        else:
            logger.debug("AdaptivePruner 未启用：%s", _PRUNER_IMPORT_ERROR or "未安装 native 可选组件")

    @property
    def available(self) -> bool:
        return _PRUNER_AVAILABLE and self._pruner is not None

    def record_fragment_features(
        self,
        fragment_id: str,
        recency: float,
        relevance: float,
        complexity: float,
        was_selected: bool,
    ) -> None:
        """
        Record the scoring features for a fragment at selection time.
        Called from optimize_context for each selected fragment.
        These are stored until feedback arrives.
        """
        self._fragment_features[fragment_id] = {
            "recency": recency,
            "relevance": relevance,
            "complexity": complexity,
            "was_selected": was_selected,
        }

    def apply_feedback(self, fragment_id: str, feedback: float) -> bool:
        """
        Apply user feedback to update RL weights for this fragment's features.

        Args:
            fragment_id: The fragment that received feedback.
            feedback:    +1.0 = helpful, -1.0 = not helpful, 0.0 = neutral.

        Returns:
            True if weights were updated, False if no feature record found.
        """
        if not self.available:
            return False

        features = self._fragment_features.get(fragment_id)
        if not features:
            return False

        # historical_success: 1.0 if this fragment was previously selected, else 0.5
        historical_success = 1.0 if features.get("was_selected") else 0.5

        self._pruner.update_policy(
            feedback=feedback,
            recency=features["recency"],
            relevance=features["relevance"],
            historical_success=historical_success,
            complexity=features["complexity"],
        )
        return True

    def score_fragment(
        self,
        recency: float,
        relevance: float,
        historical_success: float,
        complexity: float,
    ) -> float | None:
        """
        Score a fragment using current learned RL weights.
        Returns None if pruner unavailable (use entroly's own scoring).
        """
        if not self.available:
            return None
        return self._pruner.score_fragment(recency, relevance, historical_success, complexity)


class FragmentGuard:
    """
    Code quality scanner with optional Rust backend.

    Scans each ingested fragment for:
    - Hardcoded API secrets  (sk-..., API_KEY = "...")
    - unsafe Rust blocks
    - TODO comments
    - Console spam (>5 log statements)

    Returns a list of issues — empty means clean.
    Zero-config: no-op if Rust backend unavailable.
    """

    def __init__(self):
        self._guard = _RustGuard() if _GUARD_AVAILABLE else None
        if _GUARD_AVAILABLE:
            logger.info("FragmentGuard: CodeQualityGuard active -- scanning ingested fragments")

    @property
    def available(self) -> bool:
        return _GUARD_AVAILABLE and self._guard is not None

    def scan(self, content: str, source: str = "") -> list[str]:
        """
        Scan fragment content for code quality issues.

        Returns list of issue strings (empty = clean).
        """
        if not self.available or not content:
            return []
        try:
            return list(self._guard.review_code(content, source))
        except Exception:
            return []
