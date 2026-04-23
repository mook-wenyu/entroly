from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path


def resolve_launch_cmd(cmd: list[str]) -> list[str]:
    """解析启动命令，优先把裸命令解析为绝对可执行路径。"""
    if not cmd:
        return cmd

    executable = cmd[0]
    if os.path.isabs(executable) or os.path.dirname(executable):
        return cmd

    resolved = shutil.which(executable)
    if resolved:
        return [resolved, *cmd[1:]]

    return cmd


def resolve_python_cmd(executable: str | None = None) -> str:
    """解析真正的 Python 解释器路径，避免 console launcher 误当成解释器。"""
    candidate = executable or sys.executable
    name = Path(candidate).name.lower()
    if name.startswith("python"):
        return candidate

    executable_path = Path(candidate)
    for sibling_name in ("python.exe", "python", "python3"):
        sibling = executable_path.with_name(sibling_name)
        if sibling.exists():
            return str(sibling)

    return candidate
