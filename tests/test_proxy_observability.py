from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
from starlette.applications import Starlette
from starlette.routing import Route

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

import entroly.dashboard as dashboard  # noqa: E402
from entroly.proxy import PromptCompilerProxy, _health  # noqa: E402
from entroly.proxy_config import ProxyConfig  # noqa: E402


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture(autouse=True)
def clear_dashboard_requests():
    dashboard.clear_request_log()
    yield
    dashboard.clear_request_log()


def test_dashboard_snapshot_reports_proxy_base_url(monkeypatch):
    monkeypatch.setattr(dashboard, "_proxy_base_url", "http://127.0.0.1:9377/openai")
    snapshot = dashboard._get_full_snapshot()
    assert snapshot["proxy_base_url"] == "http://127.0.0.1:9377/openai"


@pytest.mark.anyio
async def test_proxy_health_reports_runtime_identity(monkeypatch, tmp_path):
    monkeypatch.setenv("ENTROLY_SOURCE", str(tmp_path))
    monkeypatch.delenv("ENTROLY_VAULT", raising=False)
    monkeypatch.delenv("ENTROLY_DIR", raising=False)
    engine = SimpleNamespace(
        _use_rust=False,
        _fragments={"one": object(), "two": object()},
        config=SimpleNamespace(checkpoint_dir=tmp_path / ".checkpoint"),
    )
    proxy = PromptCompilerProxy(
        engine=engine,
        config=ProxyConfig(openai_base_url="https://api.mookbot.com"),
    )
    app = Starlette(routes=[Route("/health", _health)])
    app.state.proxy = proxy

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.get("/health")

    payload = response.json()
    assert response.status_code == 200
    assert payload["project_dir"] == str(tmp_path)
    assert payload["vault_path"] == str(tmp_path / ".entroly" / "vault")
    assert payload["openai_base_url"] == "https://api.mookbot.com"
    assert payload["fragments"] == 2
    assert payload["beliefs"]["status"] == "unseeded"


@pytest.mark.anyio
async def test_upstream_502_is_recorded_in_dashboard():
    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            502,
            headers={"content-type": "application/json"},
            json={"error": {"message": "Upstream request failed", "type": "upstream_error"}},
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
            json={"model": "gpt-5.4", "input": "hello", "stream": False},
            headers={"authorization": "Bearer test"},
        )

    assert response.status_code == 502
    assert response.headers["x-entroly-source"] == "upstream"
    assert response.headers["x-entroly-optimized"] == "false"

    recent = dashboard.get_recent_requests()
    assert len(recent) == 1
    entry = recent[0]
    assert entry["status_code"] == 502
    assert entry["source"] == "upstream"
    assert entry["optimized"] is False
    assert entry["path"] == "/responses"
    assert entry["model"] == "gpt-5.4"

    await proxy._client.aclose()


@pytest.mark.anyio
async def test_pipeline_error_stays_pass_through_and_logs_unoptimized(monkeypatch):
    captured: dict[str, object] = {}

    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content.decode("utf-8"))
        return httpx.Response(
            200,
            headers={"content-type": "application/json"},
            json={"id": "resp_mock", "choices": []},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(openai_base_url="https://api.mookbot.com"),
    )
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    def boom(user_message: str, body: dict[str, object], path: str) -> dict[str, object]:
        raise RuntimeError("pipeline exploded")

    monkeypatch.setattr(proxy, "_run_pipeline", boom)

    app = Starlette(routes=[Route("/responses", proxy.handle_proxy, methods=["POST"])])

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(
            "/responses",
            json={"model": "gpt-5.4", "input": "hello", "stream": False},
            headers={"authorization": "Bearer test"},
        )

    assert response.status_code == 200
    assert response.headers["x-entroly-optimized"] == "false"
    assert captured["body"] == {"model": "gpt-5.4", "input": "hello", "stream": False}

    recent = dashboard.get_recent_requests()
    assert len(recent) == 1
    entry = recent[0]
    assert entry["status_code"] == 200
    assert entry["optimized"] is False

    await proxy._client.aclose()


@pytest.mark.anyio
async def test_strict_optimization_error_stops_before_upstream(monkeypatch):
    called = {"count": 0}

    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        called["count"] += 1
        return httpx.Response(
            200,
            headers={"content-type": "application/json"},
            json={"id": "resp_mock", "choices": []},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(
            openai_base_url="https://api.mookbot.com",
            strict_optimization=True,
        ),
    )
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    def boom(user_message: str, body: dict[str, object], path: str) -> dict[str, object]:
        raise RuntimeError("pipeline exploded")

    monkeypatch.setattr(proxy, "_run_pipeline", boom)

    app = Starlette(routes=[Route("/responses", proxy.handle_proxy, methods=["POST"])])

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(
            "/responses",
            json={"model": "gpt-5.4", "input": "hello", "stream": False},
            headers={"authorization": "Bearer test"},
        )

    assert response.status_code == 500
    assert response.headers["x-entroly-source"] == "proxy"
    assert response.headers["x-entroly-optimized"] == "false"
    assert response.json() == {
        "error": "optimization_failed",
        "source": "entroly_proxy",
    }
    assert called["count"] == 0

    recent = dashboard.get_recent_requests()
    assert len(recent) == 1
    entry = recent[0]
    assert entry["status_code"] == 500
    assert entry["source"] == "proxy"
    assert entry["optimized"] is False
    assert entry["error_type"] == "optimization_failed"

    await proxy._client.aclose()


@pytest.mark.anyio
async def test_optimized_responses_request_uses_instructions_and_is_logged(monkeypatch):
    captured: dict[str, object] = {}

    async def upstream_handler(request: httpx.Request) -> httpx.Response:
        captured["body"] = json.loads(request.content.decode("utf-8"))
        return httpx.Response(
            200,
            headers={"content-type": "application/json"},
            json={"id": "resp_mock", "choices": []},
        )

    proxy = PromptCompilerProxy(
        engine=SimpleNamespace(),
        config=ProxyConfig(openai_base_url="https://api.mookbot.com"),
    )
    proxy._client = httpx.AsyncClient(transport=httpx.MockTransport(upstream_handler))

    def fake_pipeline(user_message: str, body: dict[str, object], path: str) -> dict[str, object]:
        return {
            "context": "CONTEXT",
            "elapsed_ms": 1.0,
            "selected_fragments": [{"id": "frag1", "entropy_score": 0.9, "token_count": 12}],
        }

    monkeypatch.setattr(proxy, "_run_pipeline", fake_pipeline)

    app = Starlette(routes=[Route("/responses", proxy.handle_proxy, methods=["POST"])])

    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        response = await client.post(
            "/responses",
            json={"model": "gpt-5.4", "input": "hello", "stream": False},
            headers={"authorization": "Bearer test"},
        )

    assert response.status_code == 200
    assert response.headers["x-entroly-optimized"] == "true"
    instructions = captured["body"]["instructions"]
    assert instructions.startswith("<entroly:retrieved-context>")
    assert "CONTEXT" in instructions
    assert instructions.endswith("</entroly:retrieved-context>")
    assert captured["body"]["input"] == "hello"

    recent = dashboard.get_recent_requests()
    assert len(recent) == 1
    entry = recent[0]
    assert entry["status_code"] == 200
    assert entry["optimized"] is True
    assert entry["tokens_saved"] >= 0

    await proxy._client.aclose()
