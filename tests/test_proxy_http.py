from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

from entroly.proxy_http import (  # noqa: E402
    build_forward_headers,
    join_target_url,
    merge_path_and_query,
    split_origin_and_path_prefix,
)


def test_build_forward_headers_keeps_custom_provider_headers():
    headers = build_forward_headers(
        {
            "authorization": "Bearer test",
            "x-api-key": "abc",
            "x-custom-provider": "mookbot",
            "host": "127.0.0.1:9377",
            "content-length": "123",
        }
    )

    assert headers["authorization"] == "Bearer test"
    assert headers["x-api-key"] == "abc"
    assert headers["x-custom-provider"] == "mookbot"
    assert "host" not in headers
    assert "content-length" not in headers


def test_build_forward_headers_deduplicates_content_type_case_insensitively():
    headers = build_forward_headers(
        {
            "content-type": "application/json",
            "Content-Type": "application/json",
            "authorization": "Bearer test",
        }
    )

    assert list(headers.keys()).count("content-type") == 1
    assert "Content-Type" not in headers
    assert headers["content-type"] == "application/json"


def test_merge_path_and_query_preserves_query_string():
    assert (
        merge_path_and_query("/openai/responses", "api-version=2025-04-01-preview")
        == "/openai/responses?api-version=2025-04-01-preview"
    )


def test_join_target_url_joins_origin_and_request_path():
    assert (
        join_target_url(
            "https://example.openai.azure.com",
            "/openai/responses?api-version=2025-04-01-preview",
        )
        == "https://example.openai.azure.com/openai/responses?api-version=2025-04-01-preview"
    )


def test_split_origin_and_path_prefix_handles_prefixed_base_url():
    origin, path_prefix = split_origin_and_path_prefix(
        "https://example.openai.azure.com/openai"
    )
    assert origin == "https://example.openai.azure.com"
    assert path_prefix == "/openai"
