from __future__ import annotations

import os
import platform
import subprocess
import sys
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, Optional


def utc_now_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _safe_run_git(args: list[str]) -> Optional[str]:
    """
    Best-effort git info without failing if git is unavailable or repo isn't initialized.
    """
    try:
        out = subprocess.check_output(["git", *args], stderr=subprocess.DEVNULL)
        s = out.decode("utf-8", errors="replace").strip()
        return s or None
    except Exception:
        return None


@dataclass(frozen=True)
class EnvInfo:
    captured_utc: str
    python_version: str
    platform: str
    machine: str
    processor: str
    system: str
    release: str
    git_commit: Optional[str] = None
    git_dirty: Optional[bool] = None

    def to_json_dict(self) -> Dict[str, object]:
        return asdict(self)


def capture_env_info() -> EnvInfo:
    commit = _safe_run_git(["rev-parse", "HEAD"])
    dirty = None
    status = _safe_run_git(["status", "--porcelain"])
    if status is not None:
        dirty = (status.strip() != "")

    return EnvInfo(
        captured_utc=utc_now_stamp(),
        python_version=sys.version.replace("\n", " "),
        platform=platform.platform(),
        machine=platform.machine(),
        processor=platform.processor(),
        system=platform.system(),
        release=platform.release(),
        git_commit=commit,
        git_dirty=dirty,
    )
