# Scope (Working) — IX-AeroCapture-EDL-Architecture

Status: **Active development / README intentionally frozen**

## Core scope (what this repo will do)
1) Provide a **numbers-first** architecture for extreme deceleration using real momentum sinks:
   - Atmosphere (aerocapture / aerobraking / EDL)
   - Propulsion for terminal trim (minimal, precision-oriented)
   - Optional research lane: field-coupled pre-brake (solar wind / magnetosphere)

2) Provide a **verification-grade** workflow:
   - Configurable simulation inputs (YAML/JSON)
   - Reproducible outputs (JSONL logs)
   - Golden cases + regression checks
   - Clear pass/fail criteria tied to constraints (g, heating proxy, q, mass, power)

3) Provide a **telemetry + proof layer**:
   - What to measure
   - What constitutes "worked" vs "failed"
   - How to replay runs and compare against baselines

## Non-goals (explicit)
- Designing or claiming buildable "warp drive" systems.
- Any requirement on exotic matter / negative energy.
- Any claim of inertial cancellation.
- Any reactionless propulsion.

## Definitions (so we don’t talk past each other)
- **Braking / Deceleration**: reduction of vehicle kinetic energy relative to target frame,
  achieved by momentum exchange with an external sink.
- **Aerocapture**: atmospheric pass used to capture into orbit without full propulsive insertion.
- **EDL**: entry, descent, and landing sequence in atmosphere.
- **Terminal trim**: final controlled adjustments to meet orbit/landing targets.

## Open scope questions (to be decided)
- Primary mission focus:
  - (A) aerocapture-to-orbit, (B) landing EDL, or (C) both
- Vehicle mass classes supported:
  - 1t / 10t / 100t bands (or different)
- Preferred decelerator family:
  - rigid aeroshell vs HIAD vs ballute vs hybrid
- Validation targets:
  - which published mission envelopes we will match first

These will be locked via the Decision Log once you finalize direction.
