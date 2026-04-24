import json
import urllib.request

from bench import accuracy


def _bfcl_record() -> dict:
    return {
        "question": [[{"role": "user", "content": "Create a calendar event for the release review."}]],
        "ground_truth": ["calendar.create(title='Release review')"],
        "function": json.dumps([
            {
                "name": "calendar.create",
                "description": "Create a calendar event.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            }
        ]),
    }


def test_benchmark_registry_includes_bfcl_consistently():
    loaders = accuracy._benchmark_loaders("gpt-4o-mini", 1)

    assert tuple(loaders) == accuracy.BENCHMARKS
    assert "bfcl" in accuracy.BENCHMARK_CHOICES_HELP


def test_bfcl_loader_uses_cache_and_builds_tool_context(tmp_path):
    cache_path = tmp_path / "bfcl_simple.json"
    cache_path.write_text(json.dumps([_bfcl_record()]), encoding="utf-8")

    items = accuracy._load_bfcl(samples=1, cache_path=cache_path)

    assert len(items) == 1
    item = items[0]
    assert item["expected"] == "calendar.create"
    assert item["metadata"]["full_answer"] == "calendar.create(title='Release review')"
    assert "calendar.create" in item["context"]
    assert "get_weather_forecast" in item["context"]
    assert "Respond with ONLY the function call" in item["question"]


def test_bfcl_download_sets_user_agent(monkeypatch):
    captured = {}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return b'{"id":"sample","question":[]}\n'

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    records = accuracy._download_bfcl_records("https://example.test/bfcl.json")

    assert records == [{"id": "sample", "question": []}]
    assert captured["request"].headers["User-agent"] == accuracy.BFCL_USER_AGENT
    assert captured["timeout"] == 60


def test_bfcl_answer_matching_requires_exact_function_name():
    assert accuracy._check_answer("calendar.create(title='Release review')", "calendar.create", "bfcl")
    assert accuracy._check_answer("calendar.create", "calendar.create", "bfcl")
    assert not accuracy._check_answer("calendar.create_event(title='Release review')", "calendar.create", "bfcl")
    assert not accuracy._check_answer("I would call calendar.create", "calendar.create", "bfcl")
