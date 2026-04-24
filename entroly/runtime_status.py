"""
运行时身份与能力状态工具。

这些函数只读取进程环境和 vault 文件，不创建目录，也不修改运行时状态。
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


@dataclass(frozen=True)
class RuntimePaths:
    project_dir: Path
    checkpoint_dir: Path | None
    vault_path: Path
    vault_source: str
    cwd: Path


def resolve_runtime_paths(
    engine: Any | None = None,
    *,
    env: Mapping[str, str] | None = None,
    cwd: str | Path | None = None,
) -> RuntimePaths:
    """解析当前进程实际服务的项目、索引和认知 vault 路径。"""

    env_map = os.environ if env is None else env
    cwd_path = Path(cwd if cwd is not None else os.getcwd()).resolve()
    project_dir = Path(env_map.get("ENTROLY_SOURCE") or cwd_path).resolve()

    checkpoint_value = env_map.get("ENTROLY_DIR")
    if checkpoint_value is None and engine is not None:
        config = getattr(engine, "config", None)
        checkpoint_value = getattr(config, "checkpoint_dir", None)
    checkpoint_dir = Path(checkpoint_value).resolve() if checkpoint_value else None

    if env_map.get("ENTROLY_VAULT"):
        vault_path = Path(env_map["ENTROLY_VAULT"]).resolve()
        vault_source = "ENTROLY_VAULT"
    elif env_map.get("ENTROLY_DIR"):
        vault_path = (Path(env_map["ENTROLY_DIR"]) / "vault").resolve()
        vault_source = "ENTROLY_DIR"
    else:
        vault_path = (project_dir / ".entroly" / "vault").resolve()
        vault_source = "project_dir"

    return RuntimePaths(
        project_dir=project_dir,
        checkpoint_dir=checkpoint_dir,
        vault_path=vault_path,
        vault_source=vault_source,
        cwd=cwd_path,
    )


def snapshot_belief_vault(vault_path: str | Path) -> dict[str, Any]:
    """读取 vault/beliefs 的摘要，用于 dashboard 和健康诊断。"""

    vault = Path(vault_path).resolve()
    beliefs_dir = vault / "beliefs"
    total_beliefs = 0
    verified = 0
    stale = 0
    doc_beliefs = 0
    confidence_total = 0.0
    entities: list[str] = []
    errors: list[str] = []

    if beliefs_dir.exists():
        for md in sorted(beliefs_dir.rglob("*.md")):
            try:
                frontmatter = _read_frontmatter(md)
                if frontmatter is None:
                    continue
                total_beliefs += 1
                entity = str(frontmatter.get("entity", ""))
                status = str(frontmatter.get("status", "inferred"))
                confidence_total += _parse_confidence(frontmatter.get("confidence"))
                if status == "verified":
                    verified += 1
                elif status == "stale":
                    stale += 1
                if entity.startswith("doc/"):
                    doc_beliefs += 1
                entities.append(entity)
            except OSError as exc:
                errors.append(f"{md.name}: {exc}")

    avg_confidence = confidence_total / total_beliefs if total_beliefs else 0.0
    status = "ready" if total_beliefs else "unseeded"
    if errors:
        status = "degraded"

    return {
        "status": status,
        "vault_path": str(vault),
        "vault_exists": vault.exists(),
        "beliefs_dir_exists": beliefs_dir.exists(),
        "total_beliefs": total_beliefs,
        "verified": verified,
        "stale": stale,
        "doc_beliefs": doc_beliefs,
        "avg_confidence": avg_confidence,
        "freshness_pct": round((1 - stale / max(total_beliefs, 1)) * 100, 1),
        "entity_count": len({entity for entity in entities if entity}),
        "read_errors": errors[:5],
        "read_error_count": len(errors),
    }


def _read_frontmatter(path: Path) -> dict[str, str] | None:
    content = path.read_text(encoding="utf-8", errors="replace")
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    frontmatter: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip()
    return frontmatter


def _parse_confidence(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.5
