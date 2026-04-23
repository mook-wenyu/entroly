from __future__ import annotations

import ast
import os
from dataclasses import dataclass
from pathlib import Path

from .proxy_http import split_origin_and_path_prefix

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 fallback
    try:
        import tomli as tomllib  # type: ignore[no-redef]
    except ModuleNotFoundError:  # pragma: no cover - optional dependency
        tomllib = None  # type: ignore[assignment]


_DEFAULT_OPENAI_BASE_URL = "https://api.openai.com/v1"


@dataclass(frozen=True)
class CodexCliSelection:
    profile: str | None = None
    provider_override: str | None = None


@dataclass(frozen=True)
class CodexProviderConfig:
    provider_id: str
    base_url: str
    wire_api: str
    name: str
    config_path: Path | None
    profile: str | None = None


@dataclass(frozen=True)
class CodexWrapPlan:
    provider: CodexProviderConfig
    proxy_base_url: str
    upstream_origin: str
    override_args: list[str]
    env_updates: dict[str, str]


@dataclass(frozen=True)
class OpenAIProxyRoute:
    upstream_base_url: str
    upstream_origin: str
    path_prefix: str
    proxy_base_url: str
    provider_id: str | None
    wire_api: str | None
    source: str


def prepare_codex_wrap(
    agent_args: list[str],
    *,
    port: int,
    env: dict[str, str] | None = None,
    provider_id: str | None = None,
    base_url: str | None = None,
) -> CodexWrapPlan:
    """为 `entroly wrap codex` 生成当前会话的临时重定向计划。"""
    effective_env = env or os.environ
    selection = parse_codex_cli_selection(agent_args)

    if provider_id or base_url:
        if not provider_id or not base_url:
            raise ValueError("`--codex-provider-id` 和 `--codex-base-url` 必须同时提供。")
        provider = CodexProviderConfig(
            provider_id=provider_id,
            base_url=base_url,
            wire_api="responses",
            name=provider_id,
            config_path=None,
            profile=selection.profile,
        )
    else:
        provider = load_active_codex_provider(effective_env, selection)

    if provider.wire_api != "responses":
        raise ValueError(
            f"当前 Codex provider `{provider.provider_id}` 的 wire_api={provider.wire_api!r}，"
            "Entroly 目前只支持 Responses API。"
        )

    route = _build_openai_proxy_route(
        provider.base_url,
        port,
        provider_id=provider.provider_id,
        wire_api=provider.wire_api,
        source="codex-provider",
    )
    override_args = build_codex_override_args(provider, route.proxy_base_url)

    return CodexWrapPlan(
        provider=provider,
        proxy_base_url=route.proxy_base_url,
        upstream_origin=route.upstream_origin,
        override_args=override_args,
        env_updates={"ENTROLY_OPENAI_BASE": route.upstream_origin},
    )


def resolve_openai_proxy_route(
    *,
    port: int,
    env: dict[str, str] | None = None,
    selection: CodexCliSelection | None = None,
) -> OpenAIProxyRoute:
    """解析 OpenAI 兼容上游及其对应的本地代理入口。"""
    effective_env = env or os.environ
    explicit_base = effective_env.get("ENTROLY_OPENAI_BASE")
    if explicit_base:
        return _build_openai_proxy_route(explicit_base, port, source="env")

    provider = load_active_codex_provider(
        effective_env, selection or CodexCliSelection()
    )
    source = "codex-provider"
    if (
        provider.provider_id == "openai"
        and provider.base_url == _DEFAULT_OPENAI_BASE_URL
        and provider.config_path is None
        and provider.profile is None
    ):
        source = "default-openai"

    return _build_openai_proxy_route(
        provider.base_url,
        port,
        provider_id=provider.provider_id,
        wire_api=provider.wire_api,
        source=source,
    )


def parse_codex_cli_selection(agent_args: list[str]) -> CodexCliSelection:
    """解析 Codex 命令行里会影响 provider 选择的参数。"""
    profile: str | None = None
    provider_override: str | None = None

    index = 0
    while index < len(agent_args):
        arg = agent_args[index]

        if arg in {"--profile", "-p"}:
            if index + 1 >= len(agent_args):
                raise ValueError("`codex --profile` 缺少值。")
            profile = agent_args[index + 1]
            index += 2
            continue

        if arg.startswith("--profile="):
            profile = arg.split("=", 1)[1]
            index += 1
            continue

        if arg in {"--config", "-c"}:
            if index + 1 >= len(agent_args):
                raise ValueError("`codex --config` 缺少 `key=value`。")
            key, value = _parse_config_entry(agent_args[index + 1])
            provider_override = _apply_config_override(key, value, provider_override)
            index += 2
            continue

        if arg.startswith("--config="):
            key, value = _parse_config_entry(arg.split("=", 1)[1])
            provider_override = _apply_config_override(key, value, provider_override)
            index += 1
            continue

        index += 1

    return CodexCliSelection(profile=profile, provider_override=provider_override)


def resolve_codex_config_path(env: dict[str, str] | None = None) -> Path:
    """解析当前会话实际使用的 Codex 配置路径。"""
    effective_env = env or os.environ
    codex_home = effective_env.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "config.toml"
    return Path.home() / ".codex" / "config.toml"


def load_active_codex_provider(
    env: dict[str, str] | None,
    selection: CodexCliSelection,
) -> CodexProviderConfig:
    """读取当前生效的 Codex provider。"""
    config_path = resolve_codex_config_path(env)
    config = _load_codex_config(config_path)

    profile = selection.profile
    profile_cfg = _load_profile(config, profile)

    provider_id = selection.provider_override
    if provider_id is None:
        provider_id = _pick_first(profile_cfg, config, key="model_provider") or "openai"

    if provider_id == "openai":
        base_url = _pick_first(profile_cfg, config, key="openai_base_url") or _DEFAULT_OPENAI_BASE_URL
        return CodexProviderConfig(
            provider_id="openai",
            base_url=base_url,
            wire_api="responses",
            name="OpenAI",
            config_path=config_path if config_path.exists() else None,
            profile=profile,
        )

    provider_cfg = config.get("model_providers", {}).get(provider_id)
    if not isinstance(provider_cfg, dict):
        location = str(config_path) if config_path.exists() else "默认配置"
        raise ValueError(f"未在 {location} 中找到 Codex provider `{provider_id}`。")

    base_url = provider_cfg.get("base_url")
    if not isinstance(base_url, str) or not base_url:
        raise ValueError(f"Codex provider `{provider_id}` 缺少 `base_url`。")

    wire_api = provider_cfg.get("wire_api", "responses")
    if not isinstance(wire_api, str) or not wire_api:
        wire_api = "responses"

    name = provider_cfg.get("name", provider_id)
    if not isinstance(name, str) or not name:
        name = provider_id

    return CodexProviderConfig(
        provider_id=provider_id,
        base_url=base_url,
        wire_api=wire_api,
        name=name,
        config_path=config_path if config_path.exists() else None,
        profile=profile,
    )


def build_codex_override_args(provider: CodexProviderConfig, proxy_base_url: str) -> list[str]:
    """构造只影响当前会话的 Codex 配置覆盖参数。"""
    override_value = _toml_string(proxy_base_url)

    if provider.provider_id == "openai":
        entry = f"openai_base_url={override_value}"
    else:
        entry = f"model_providers.{provider.provider_id}.base_url={override_value}"

    return ["--config", entry]


def _load_codex_config(config_path: Path) -> dict:
    if not config_path.exists():
        return {}
    if tomllib is None:
        raise ValueError(
            "当前 Python 环境缺少 TOML 解析能力，无法读取 Codex 配置。"
            "请使用 Python 3.11+，或显式传入 `--codex-provider-id` 与 `--codex-base-url`。"
        )

    with config_path.open("rb") as fh:
        data = tomllib.load(fh)

    if not isinstance(data, dict):
        raise ValueError(f"Codex 配置格式非法: {config_path}")
    return data


def _load_profile(config: dict, profile: str | None) -> dict:
    if not profile:
        return {}

    profiles = config.get("profiles", {})
    if not isinstance(profiles, dict):
        raise ValueError("Codex 配置中的 `[profiles]` 不是合法对象。")

    profile_cfg = profiles.get(profile)
    if not isinstance(profile_cfg, dict):
        raise ValueError(f"未找到 Codex profile `{profile}`。")

    return profile_cfg


def _pick_first(*sources: dict, key: str) -> str | None:
    for source in sources:
        if not isinstance(source, dict):
            continue
        value = source.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _parse_config_entry(entry: str) -> tuple[str, str]:
    if "=" not in entry:
        raise ValueError(f"Codex `--config` 不是合法的 `key=value`：{entry}")
    key, value = entry.split("=", 1)
    return key.strip(), value.strip()


def _apply_config_override(
    key: str,
    value: str,
    provider_override: str | None,
) -> str | None:
    if key == "model_provider":
        return _parse_toml_string(value)

    if key == "openai_base_url" or (
        key.startswith("model_providers.") and key.endswith(".base_url")
    ):
        raise ValueError(
            "检测到你在 `codex` 参数里手动覆盖 provider base_url。"
            "这会与 `entroly wrap codex` 的会话重定向冲突，请删除该覆盖后再运行。"
        )

    return provider_override


def _parse_toml_string(value: str) -> str:
    stripped = value.strip()
    if stripped and stripped[0] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(stripped)
        except (SyntaxError, ValueError):
            parsed = stripped.strip("\"'")
        if not isinstance(parsed, str):
            raise ValueError(f"`model_provider` 必须是字符串，收到：{value}")
        return parsed
    return stripped


def _toml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _build_openai_proxy_route(
    base_url: str,
    port: int,
    *,
    provider_id: str | None = None,
    wire_api: str | None = None,
    source: str,
) -> OpenAIProxyRoute:
    upstream_origin, path_prefix = split_origin_and_path_prefix(base_url)
    proxy_base_url = f"http://127.0.0.1:{port}{path_prefix}"
    return OpenAIProxyRoute(
        upstream_base_url=base_url,
        upstream_origin=upstream_origin,
        path_prefix=path_prefix,
        proxy_base_url=proxy_base_url,
        provider_id=provider_id,
        wire_api=wire_api,
        source=source,
    )
