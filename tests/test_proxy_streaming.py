from __future__ import annotations

import sys
from pathlib import Path
from types import SimpleNamespace

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


def test_proxy_config_disables_env_proxy_by_default(monkeypatch):
    monkeypatch.delenv("ENTROLY_TRUST_ENV_PROXY", raising=False)
    assert ProxyConfig.from_env().trust_env_proxy is False


def test_new_http_client_uses_trust_env_proxy_flag(monkeypatch):
    created: list[dict] = []

    class DummyClient:
        is_closed = False

    def fake_async_client(*args, **kwargs):
        created.append(kwargs)
        return DummyClient()

    monkeypatch.setattr("entroly.proxy.httpx.AsyncClient", fake_async_client)

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(trust_env_proxy=False),
    )
    proxy._new_http_client()

    assert created[0]["trust_env"] is False


@pytest.mark.anyio
async def test_streaming_error_preserves_upstream_status_and_body():
    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        assert request.url.path == "/responses"
        return httpx.Response(
            401,
            headers={
                "content-type": "application/json",
                "x-request-id": "req_test_123",
            },
            json={"code": "INVALID_API_KEY", "message": "Invalid API key"},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(openai_base_url="https://api.mookbot.com"),
    )
    proxy._bypass = True
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    app = Starlette(routes=[Route("/responses", proxy.handle_proxy, methods=["POST"])])

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(
            "/responses",
            json={"model": "gpt-5.4", "input": "hello", "stream": True},
            headers={"authorization": "Bearer test"},
        )

    assert response.status_code == 401
    assert response.headers["content-type"].startswith("application/json")
    assert response.headers["x-request-id"] == "req_test_123"
    assert response.headers["x-entroly-source"] == "upstream"
    assert response.json() == {
        "code": "INVALID_API_KEY",
        "message": "Invalid API key",
    }
    assert proxy._breaker.state == "closed"

    await proxy._client.aclose()


@pytest.mark.anyio
async def test_bypass_forwards_chat_request_body_without_mutation():
    captured: dict[str, str] = {}

    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        captured["path"] = request.url.path
        captured["body"] = request.content.decode("utf-8")
        return httpx.Response(
            200,
            headers={"content-type": "application/json"},
            json={"id": "resp_mock", "choices": []},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(openai_base_url="https://api.mookbot.com"),
    )
    proxy._bypass = True
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    app = Starlette(routes=[Route("/v1/chat/completions", proxy.handle_proxy, methods=["POST"])])
    raw_body = '{"model":"gpt-5.4","messages":[{"role":"user","content":"hello"}],"stream":false}'

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(
            "/v1/chat/completions",
            content=raw_body.encode("utf-8"),
            headers={"authorization": "Bearer test", "content-type": "application/json"},
        )

    assert response.status_code == 200
    assert captured["path"] == "/v1/chat/completions"
    assert captured["body"] == raw_body

    await proxy._client.aclose()
