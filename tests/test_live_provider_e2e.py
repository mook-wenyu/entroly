from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import httpx
import pytest
from starlette.applications import Starlette
from starlette.routing import Route

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

from entroly.proxy import PromptCompilerProxy  # noqa: E402
from entroly.proxy_config import ProxyConfig  # noqa: E402


SENTINEL = "ENTROLY_LIVE_PROVIDER_E2E_OK_7F3B"


@pytest.fixture
def anyio_backend():
    return "asyncio"


def _required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        pytest.skip(f"{name} 是真实 provider E2E 测试的必需环境变量")
    return value


def _extract_text(response_json: dict[str, Any]) -> str:
    parts: list[str] = []

    output_text = response_json.get("output_text")
    if isinstance(output_text, str):
        parts.append(output_text)

    for item in response_json.get("output", []):
        if not isinstance(item, dict):
            continue
        for block in item.get("content", []):
            if isinstance(block, dict) and isinstance(block.get("text"), str):
                parts.append(block["text"])

    for choice in response_json.get("choices", []):
        if not isinstance(choice, dict):
            continue
        message = choice.get("message", {})
        if isinstance(message, dict) and isinstance(message.get("content"), str):
            parts.append(message["content"])

    for block in response_json.get("content", []):
        if isinstance(block, dict) and isinstance(block.get("text"), str):
            parts.append(block["text"])

    for candidate in response_json.get("candidates", []):
        if not isinstance(candidate, dict):
            continue
        content = candidate.get("content", {})
        if not isinstance(content, dict):
            continue
        for part in content.get("parts", []):
            if isinstance(part, dict) and isinstance(part.get("text"), str):
                parts.append(part["text"])

    if not parts:
        raise AssertionError(
            "真实 provider 响应没有可识别的文本字段；"
            f"顶层字段={sorted(response_json.keys())}"
        )
    return "\n".join(parts)


def _redacted_preview(response: httpx.Response) -> str:
    text = response.text[:1000]
    api_key = os.environ.get("ENTROLY_LIVE_RESPONSES_API_KEY")
    if api_key:
        text = text.replace(api_key, "<redacted>")
    return text


@pytest.mark.anyio
@pytest.mark.live_provider
async def test_live_responses_provider_receives_entroly_context(monkeypatch):
    base_url = _required_env("ENTROLY_LIVE_RESPONSES_BASE_URL")
    model = _required_env("ENTROLY_LIVE_RESPONSES_MODEL")
    api_key = _required_env("ENTROLY_LIVE_RESPONSES_API_KEY")

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(
            openai_base_url=base_url,
            strict_optimization=True,
            enable_conversation_compression=False,
            enable_temperature_calibration=False,
        ),
    )
    proxy._enable_passive_feedback = False
    proxy._client = httpx.AsyncClient(timeout=60.0, trust_env=False)

    def pipeline(user_message: str, body: dict[str, object], path: str) -> dict[str, object]:
        assert user_message
        assert path.endswith("/responses")
        assert body["model"] == model
        return {
            "context": (
                "Live provider E2E instruction: when the user asks for the provider check, "
                f"reply exactly {SENTINEL} and no other text."
            ),
            "elapsed_ms": 1.0,
            "selected_fragments": [
                {
                    "id": "live-provider-e2e",
                    "entropy_score": 1.0,
                    "token_count": 24,
                }
            ],
        }

    monkeypatch.setattr(proxy, "_run_pipeline", pipeline)

    app = Starlette(routes=[Route("/responses", proxy.handle_proxy, methods=["POST"])])
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
        timeout=90.0,
    ) as client:
        response = await client.post(
            "/responses",
            json={
                "model": model,
                "input": "Provider check: return the required sentinel.",
                "max_output_tokens": 128,
                "stream": False,
            },
            headers={"authorization": f"Bearer {api_key}"},
        )

    await proxy._client.aclose()

    assert response.headers["x-entroly-optimized"] == "true"
    if response.status_code >= 400:
        pytest.fail(
            f"真实 provider 返回 {response.status_code}: {_redacted_preview(response)}"
        )

    response_json = response.json()
    text = _extract_text(response_json)
    assert SENTINEL in text
