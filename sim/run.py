id="ix_sim_run_v1"
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

from models.contracts import RunResult
from sim.io import (
    ConfigError,
    ensure_output_dir,
    load_json,
    parse_run_config,
    stable_config_hash,
    write_config_echo,
    write_result_json,
)

OUTPUT_BASE = Path("sim_output")


def _utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _jsonl_append(path: Path, event: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, sort_keys=True) + "\n")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python -m sim.run <config.json>", file=sys.stderr)
        return 2

    cfg_path = Path(argv[1]).expanduser().resolve()
    if not cfg_path.exists():
        print(f"Config not found: {cfg_path}", file=sys.stderr)
        return 2

    try:
        cfg_dict = load_json(cfg_path)
        cfg = parse_run_config(cfg_dict)
        cfg_hash = stable_config_hash(cfg)
    except ConfigError as e:
        print(f"ConfigError: {e}", file=sys.stderr)
        return 2

    run_id = f"{_utc_stamp()}_{cfg_hash}"
    out_dir = ensure_output_dir(OUTPUT_BASE, run_id)
    telemetry_path = out_dir / "telemetry.jsonl"

    # Echo config for reproducibility
    write_config_echo(out_dir, cfg)

    # Telemetry start event
    _jsonl_append(
        telemetry_path,
        {
            "t": _utc_stamp(),
            "event": "run_start",
            "run_id": run_id,
            "config_hash": cfg_hash,
            "mission": cfg.mission,
            "body": cfg.body,
            "models": {
                "atmosphere": cfg.atmosphere_model_id,
                "aero": cfg.aero_model_id,
                "thermal": cfg.thermal_model_id,
                "gnc": cfg.gnc_model_id,
                "prebrake": cfg.prebrake_model_id,
            },
        },
    )

    # NOTE: Actual model execution is intentionally not wired yet.
    # When models are implemented, we will:
    # - call atmosphere/aero/thermal/gnc modules
    # - iterate over trajectory states
    # - log time-series telemetry
    # - compute metrics and verify constraints

    _jsonl_append(
        telemetry_path,
        {
            "t": _utc_stamp(),
            "event": "run_note",
            "run_id": run_id,
            "note": "Scaffold run only (no physics models executed).",
        },
    )

    # Produce placeholder RunResult
    result = RunResult(
        config_hash=cfg_hash,
        model_versions={
            "atmosphere": cfg.atmosphere_model_id,
            "aero": cfg.aero_model_id,
            "thermal": cfg.thermal_model_id,
            "gnc": cfg.gnc_model_id,
            "prebrake": cfg.prebrake_model_id,
        },
        telemetry_path=str(telemetry_path.as_posix()),
        notes="Scaffold only. Models not implemented.",
    )

    # Telemetry end event
    _jsonl_append(
        telemetry_path,
        {
            "t": _utc_stamp(),
            "event": "run_end",
            "run_id": run_id,
            "config_hash": cfg_hash,
            "result_path": str((out_dir / "result.json").as_posix()),
        },
    )

    write_result_json(out_dir, result.to_json_dict())
    print(f"Run complete: {run_id}")
    print(f"Output dir : {out_dir.as_posix()}")
    print(f"Telemetry  : {telemetry_path.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
