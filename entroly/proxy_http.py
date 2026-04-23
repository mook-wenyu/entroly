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
    seen_lower: set[str] = set()

    for key, value in original.items():
        lower_key = key.lower()
        if lower_key in _HOP_BY_HOP_HEADERS:
            continue
        if lower_key in seen_lower:
            continue
        seen_lower.add(lower_key)
        forward[key] = value

    if "content-type" not in seen_lower:
        forward["Content-Type"] = "application/json"
    return forward


def build_downstream_headers(original: dict[str, str]) -> dict[str, str]:
    """过滤逐跳头，保留可安全返回给调用方的上游响应头。"""
    downstream: dict[str, str] = {}

    for key, value in original.items():
        if key.lower() in _HOP_BY_HOP_HEADERS:
            continue
        downstream[key] = value

    return downstream


def merge_path_and_query(path: str, query: str) -> str:
    """把请求路径和查询串还原成完整上游路径。"""
    if not query:
        return path
    return f"{path}?{query}"


def join_target_url(base_url: str, path_with_query: str) -> str:
    """把上游 origin 与当前请求路径安全拼接。"""
    if not base_url:
        raise ValueError("upstream base_url 不能为空")

    origin, path_prefix = split_origin_and_path_prefix(base_url)
    parsed_origin = urlsplit(origin)
    request = urlsplit(path_with_query)
    request_path = request.path or "/"
    if not request_path.startswith("/"):
        request_path = f"/{request_path}"

    # 当本地 proxy URL 已经带上 provider 前缀时，避免把同一前缀重复拼回上游。
    suffix_path = request_path
    if path_prefix:
        if request_path == path_prefix:
            suffix_path = "/"
        elif request_path.startswith(f"{path_prefix}/"):
            suffix_path = request_path[len(path_prefix):]

    full_path = f"{path_prefix}{suffix_path}" if path_prefix else suffix_path
    return urlunsplit(
        (parsed_origin.scheme, parsed_origin.netloc, full_path, request.query, "")
    )


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
