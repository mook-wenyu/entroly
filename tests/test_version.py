from __future__ import annotations

from pathlib import Path

import entroly


def _read_pyproject_version() -> str:
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"
    in_project = False
    for raw_line in pyproject_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "[project]":
            in_project = True
            continue
        if in_project and line.startswith("["):
            break
        if not in_project or "=" not in line:
            continue

        key, _, value = line.partition("=")
        if key.strip() == "version":
            return value.strip().strip('"').strip("'")
    raise AssertionError("pyproject.toml 缺少 [project].version")


def test_package_version_matches_pyproject():
    assert entroly.__version__ == _read_pyproject_version()
