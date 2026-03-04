# Telemetry + Proof Layer (Scaffold)

Status: **Scaffold** (but usable immediately)

Goals:
- Make every run auditable:
  - what config was used
  - what code version ran (when available)
  - what telemetry events were emitted
  - what result bundle was produced

Core artifacts (per run):
- `config.echo.json`  (input config, normalized)
- `telemetry.jsonl`   (append-only event log)
- `result.json`       (final result bundle)
- `proof_bundle.json` (packaging metadata referencing the above)

## Telemetry event format (JSON object per line)
Required fields:
- `t` : ISO-like UTC stamp (string)
- `event` : event type (string)
- `run_id` : run identifier (string)
- `config_hash` : stable hash of normalized config (string)

Recommended fields (when known):
- `phase` : phase name (e.g., "aerocapture", "edl", "terminal")
- `severity` : "info" | "warn" | "error"
- `tags` : object of string->string for filtering
- `data` : object for structured payloads (numbers, lists, etc.)

Schemas:
- `telemetry/schema/telemetry_event.schema.json`
- `telemetry/schema/proof_bundle.schema.json`

## Proof bundle philosophy (NASA/SpaceX-clean)
- We do not claim truth; we **prove what happened**:
  - deterministic config hashing
  - config echo
  - event log
  - result bundle
  - environment metadata (python version, platform, timestamp)

This is intentionally dependency-light and can evolve into a stronger attestation system later.
