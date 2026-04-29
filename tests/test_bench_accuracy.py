import json
import urllib.request
from types import SimpleNamespace

import pytest

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


def test_responses_payload_maps_system_to_instructions_and_user_to_input():
    instructions, input_text = accuracy._messages_to_responses_payload([
        {"role": "system", "content": "Answer with one letter."},
        {"role": "user", "content": "Question A"},
        {"role": "user", "content": "Question B"},
    ])

    assert instructions == "Answer with one letter."
    assert input_text == "Question A\n\nQuestion B"


def test_responses_payload_rejects_non_string_content_and_empty_input():
    with pytest.raises(ValueError, match="string content"):
        accuracy._messages_to_responses_payload([{"role": "user", "content": ["not", "text"]}])

    with pytest.raises(ValueError, match="cannot be empty"):
        accuracy._messages_to_responses_payload([{"role": "system", "content": "No user input"}])


def test_extract_responses_text_reads_output_text_and_structured_output():
    assert accuracy._extract_responses_text(SimpleNamespace(output_text="direct text")) == "direct text"

    response = SimpleNamespace(
        output=[
            SimpleNamespace(content=[SimpleNamespace(text="part 1"), SimpleNamespace(text="part 2")]),
        ]
    )

    assert accuracy._extract_responses_text(response) == "part 1\npart 2"


def test_extract_responses_text_reads_json_dict_output():
    response = {
        "output": [
            {"content": [{"type": "output_text", "text": "dict text"}]},
        ],
        "usage": {"total_tokens": 11},
    }

    assert accuracy._extract_responses_text(response) == "dict text"
    assert accuracy._responses_token_count(response) == 11


def test_call_responses_http_posts_explicit_payload(monkeypatch):
    captured = {}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return json.dumps({
                "output": [{"content": [{"text": "B"}]}],
                "usage": {"total_tokens": 7},
            }).encode("utf-8")

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        captured["payload"] = json.loads(request.data.decode("utf-8"))
        return FakeResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    text, tokens = accuracy._call_responses_http(
        [{"role": "system", "content": "Answer briefly."}, {"role": "user", "content": "Question"}],
        model="gpt-5.5",
        max_tokens=12,
        base_url="https://api.example.test/v1/",
        api_key="secret-key",
    )

    assert text == "B"
    assert tokens == 7
    assert captured["request"].full_url == "https://api.example.test/v1/responses"
    assert captured["request"].headers["Authorization"] == "Bearer secret-key"
    assert captured["request"].headers["Content-type"] == "application/json"
    assert captured["request"].headers["User-agent"] == accuracy.BENCHMARK_USER_AGENT
    assert captured["payload"] == {
        "model": "gpt-5.5",
        "input": "Question",
        "max_output_tokens": 12,
        "instructions": "Answer briefly.",
    }
    assert captured["timeout"] == 120


def test_fetch_hf_rows_sets_user_agent(monkeypatch):
    captured = {}

    class FakeResponse:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self):
            return b'{"rows":[{"row":{"answer":"A"}}]}'

    def fake_urlopen(request, timeout):
        captured["request"] = request
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr(urllib.request, "urlopen", fake_urlopen)

    rows = accuracy._fetch_hf_rows("cais/mmlu", "all", "test", 1)

    assert rows == [{"answer": "A"}]
    assert captured["request"].headers["User-agent"] == accuracy.BENCHMARK_USER_AGENT
    assert captured["timeout"] == 60


def test_run_mode_rejects_failed_samples(monkeypatch):
    def failing_call(*args, **kwargs):
        raise RuntimeError("provider unavailable")

    monkeypatch.setattr(accuracy, "_call_llm", failing_call)

    with pytest.raises(accuracy.BenchmarkExecutionError, match="failed for 1/1 samples"):
        accuracy._run_mode(
            [{"context": "", "question": "What is 2+2?", "expected": "4"}],
            benchmark="gsm8k",
            model="gpt-test",
            mode="baseline",
            budget=None,
        )


def test_benchmark_registry_includes_bfcl_consistently():
    loaders = accuracy._benchmark_loaders("gpt-5.5", 1)

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
