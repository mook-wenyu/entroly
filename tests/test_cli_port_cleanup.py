from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO))

from entroly.cli import _is_entroly_process_command, _parse_netstat_listening_pids  # noqa: E402


def test_parse_netstat_listening_pids_matches_only_requested_port():
    output = """
  Proto  Local Address          Foreign Address        State           PID
  TCP    127.0.0.1:9377         0.0.0.0:0              LISTENING       66920
  TCP    127.0.0.1:9378         0.0.0.0:0              LISTENING       66921
  TCP    127.0.0.1:9377         127.0.0.1:50000        ESTABLISHED     66920
  TCP    [::1]:9377             [::]:0                 LISTENING       66922
"""

    assert _parse_netstat_listening_pids(output, 9377) == [66920, 66922]


def test_is_entroly_process_command_requires_runtime_subcommand():
    assert _is_entroly_process_command(r'"C:\Python\python.exe" "C:\Python\Scripts\entroly.exe" go')
    assert _is_entroly_process_command("python -m entroly.cli proxy --port 9377")
    assert not _is_entroly_process_command("python -m entroly.cli compile .")
    assert not _is_entroly_process_command(r'"C:\Other\server.exe" --port 9377')
