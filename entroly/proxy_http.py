from __future__ import annotations

from urllib.parse import urlsplit, urlunsplit


_HOP_BY_HOP_HEADERS = {
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailer",
    "transfer-encoding",
    "upgrade",
    "host",
    "content-length",
}


def build_forward_headers(original: dict[str, str]) -> dict[str, str]:
    """保留上游 provider 所需请求头，同时剔除逐跳头。"""
    forward: dict[str, str] = {}

    for key, value in original.items():
        if key.lower() in _HOP_BY_HOP_HEADERS:
            continue
        forward[key] = value

    forward.setdefault("Content-Type", "application/json")
    return forward


def merge_path_and_query(path: str, query: str) -> str:
    """把请求路径和查询串还原成完整上游路径。"""
    if not query:
        return path
    return f"{path}?{query}"


def join_target_url(base_url: str, path_with_query: str) -> str:
    """把上游 origin 与当前请求路径安全拼接。"""
    if not base_url:
        raise ValueError("upstream base_url 不能为空")

    base = base_url.rstrip("/")
    path = path_with_query if path_with_query.startswith("/") else f"/{path_with_query}"
    return f"{base}{path}"


def split_origin_and_path_prefix(base_url: str) -> tuple[str, str]:
    """把 provider base_url 拆成 origin 与路径前缀。"""
    parsed = urlsplit(base_url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"无效的 provider base_url: {base_url}")
    if parsed.query or parsed.fragment:
        raise ValueError(f"provider base_url 不能包含 query 或 fragment: {base_url}")

    origin = urlunsplit((parsed.scheme, parsed.netloc, "", "", ""))
    path_prefix = parsed.path.rstrip("/")
    return origin, path_prefix
