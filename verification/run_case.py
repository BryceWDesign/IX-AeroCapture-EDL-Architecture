from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import List


def _fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 1


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("Usage: python verification/run_case.py <case_folder>", file=sys.stderr)
        return 2

    case_dir = Path(argv[1]).expanduser().resolve()
    cfg_p = case_dir / "config.json"
    exp_p = case_dir / "expected_ranges.json"

    if not case_dir.exists():
        return _fail(f"Case folder not found: {case_dir}")
    if not cfg_p.exists():
        return _fail(f"Missing config.json in case: {cfg_p}")
    if not exp_p.exists():
        return _fail(f"Missing expected_ranges.json in case: {exp_p}")

    # Run the sim
    print(f"Running sim for case: {case_dir.name}")
    proc = subprocess.run([sys.executable, "-m", "sim.run", str(cfg_p)], check=False)
    if proc.returncode != 0:
        return _fail(f"sim.run failed with code {proc.returncode}")

    # Find latest output dir by mtime (simple and dependency-free)
    out_base = Path("sim_output")
    if not out_base.exists():
        return _fail("sim_output folder not found after sim.run")

    out_dirs = [p for p in out_base.iterdir() if p.is_dir()]
    if not out_dirs:
        return _fail("No output run directories found in sim_output")

    latest = max(out_dirs, key=lambda p: p.stat().st_mtime)
    result_p = latest / "result.json"
    if not result_p.exists():
        return _fail(f"result.json not found in latest run dir: {latest}")

    print(f"Checking result: {result_p}")
    check_proc = subprocess.run(
        [sys.executable, str(Path("verification/checks/check_result_against_ranges.py")), str(result_p), str(exp_p)],
        check=False,
    )
    return check_proc.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
