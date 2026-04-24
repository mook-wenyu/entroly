from __future__ import annotations

import json
import sys
from collections.abc import Callable
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


@pytest.fixture
def anyio_backend():
    return "asyncio"


def _contract_pipeline(
    user_message: str, body: dict[str, object], path: str
) -> dict[str, object]:
    assert user_message
    assert path
    assert body
    return {
        "context": "ENTROLY_CONTEXT",
        "elapsed_ms": 1.0,
        "selected_fragments": [
            {
                "id": "frag-contract",
                "entropy_score": 0.9,
                "token_count": 12,
            }
        ],
    }


async def _send_through_proxy(
    *,
    path: str,
    body: dict[str, object],
    headers: dict[str, str],
) -> tuple[httpx.Response, dict[str, object]]:
    captured: dict[str, object] = {}

    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        captured["path"] = request.url.path
        captured["body"] = json.loads(request.content.decode("utf-8"))
        return httpx.Response(
            200,
            headers={"content-type": "application/json"},
            json={"id": "resp_mock", "choices": []},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(
            openai_base_url="https://api.openrouter.ai",
            anthropic_base_url="https://api.anthropic.com",
            gemini_base_url="https://generativelanguage.googleapis.com",
            enable_temperature_calibration=False,
            enable_conversation_compression=False,
        ),
    )
    proxy._enable_passive_feedback = False
    proxy._run_pipeline = _contract_pipeline  # type: ignore[method-assign]
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    app = Starlette(routes=[Route("/{path:path}", proxy.handle_proxy, methods=["POST"])])
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(path, json=body, headers=headers)

    await proxy._client.aclose()
    return response, captured


@pytest.mark.anyio
@pytest.mark.parametrize(
    ("path", "headers", "body", "assert_context"),
    [
        (
            "/responses",
            {"authorization": "Bearer sk-test"},
            {"model": "gpt-5.4", "input": "review this file", "stream": False},
            lambda sent: (
                sent["instructions"] == "ENTROLY_CONTEXT"
                and sent["input"] == "review this file"
            ),
        ),
        (
            "/v1/chat/completions",
            {"authorization": "Bearer sk-or-test"},
            {
                "model": "anthropic/claude-sonnet-4.6",
                "messages": [{"role": "user", "content": "review this file"}],
                "stream": False,
            },
            lambda sent: (
                sent["messages"][0]["role"] == "system"
                and sent["messages"][0]["content"] == "ENTROLY_CONTEXT"
            ),
        ),
        (
            "/v1/messages",
            {"x-api-key": "sk-ant-test", "anthropic-version": "2023-06-01"},
            {
                "model": "claude-sonnet-4-5-20250929",
                "system": "Existing system",
                "messages": [{"role": "user", "content": "review this file"}],
                "max_tokens": 1024,
            },
            lambda sent: sent["system"].startswith("ENTROLY_CONTEXT\n\nExisting system"),
        ),
        (
            "/v1beta/models/gemini-2.5-flash:generateContent",
            {"x-goog-api-key": "AIza-test"},
            {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": "review this file"}],
                    }
                ]
            },
            lambda sent: (
                sent["systemInstruction"]["parts"][0]["text"] == "ENTROLY_CONTEXT"
            ),
        ),
    ],
)
async def test_provider_contract_injects_context_before_forwarding(
    path: str,
    headers: dict[str, str],
    body: dict[str, object],
    assert_context: Callable[[dict[str, Any]], bool],
):
    response, captured = await _send_through_proxy(
        path=path,
        body=body,
        headers=headers,
    )

    assert response.status_code == 200
    assert response.headers["x-entroly-optimized"] == "true"
    assert assert_context(captured["body"]) is True
