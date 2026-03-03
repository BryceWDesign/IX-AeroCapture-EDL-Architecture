# IX-AeroCapture-EDL-Architecture — Architecture Map (Working Draft)

Status: **VOLATILE / IN-PROGRESS**
- This file is the canonical architecture reference while the README is intentionally frozen.
- Do **not** treat any module list here as final until promoted from "Proposed" → "Locked" in the Decision Log.

## Design principles (the "Tesla lens", reality-locked)
1) **Maximize coupling cross-section** to external momentum sinks (atmosphere, solar wind/magnetosphere, photons).
2) **Use power to shape/steer coupling**, not to claim free momentum.
3) **Measurement-first**: every claim must map to logged telemetry + a validation case.
4) **Fail-safe defaults**: anything uncertain degrades to a conservative mode, not optimism.

---

## Primary objective
Build a verifiable, numbers-first architecture for extreme deceleration during:
- **Aerocapture / Aerobraking** (primary)
- **Entry–Descent–Landing** (primary)
- Optional upstream: **Pre-brake** (secondary / research track)

## Non-objectives
- No claims of reactionless propulsion.
- No exotic physics requirements (negative energy, energy-condition violations) as a dependency for success.

---

## Canonical phases (stack)
### Phase 0 — Upstream pre-brake (Optional)
Goal: reduce arrival V∞ / energy before atmospheric interface.
Examples (research lanes): plasma-magnet / magsail / e-sail / tethers.
Status: **Proposed** (not locked).

### Phase 1 — Aerocapture / initial atmospheric energy dump
Goal: shed the bulk of kinetic energy using the atmosphere while controlling corridor and peak loads.
Status: **Core / Locked as concept** (implementation details TBD).

### Phase 2 — EDL shaping (lift/drag modulation, attitude, stability)
Goal: manage trajectory, loads, heating, dispersions through the mid/late entry.
Status: **Core / Locked as concept**.

### Phase 3 — Terminal trim (propulsive or aerodynamic)
Goal: precision orbit insertion, landing targeting, dispersion cleanup.
Status: **Core / Locked as concept** (method TBD).

### Phase 4 — Proof layer (telemetry + validation + evidence)
Goal: produce machine-checkable or at least reproducible evidence artifacts.
Status: **Core / Locked as concept**.

---

## Module map (proposed until logged)
### M1 — Corridor Planner
Inputs: target orbit/landing, vehicle mass properties, atmospheric model, constraints  
Outputs: entry corridor, guidance targets, abort logic hooks

### M2 — AeroCapture Model (low-fidelity v1 → validated vN)
Inputs: BC, Cd/Cl model, atmosphere profile, bank angle profile  
Outputs: ΔV equivalent removed, peak q, peak heating proxy, peak g

### M3 — HIAD / TPS / Structural Stack Model
Inputs: deployable geometry, material limits, structural margins  
Outputs: allowed q/heating envelopes, deployment constraints, mass/volume penalties

### M4 — Guidance & Control (GNC) SafetyGate
Inputs: M1/M2 outputs, sensor state, constraints  
Outputs: allowable commands + degradations + abort triggers

### M5 — Telemetry Spine
Inputs: sensor suite definition  
Outputs: JSONL logs, event markers, replay bundles, plots (later)

### M6 — Verification Pack
Inputs: canonical test cases  
Outputs: expected ranges + regression checks + pass/fail criteria

### M7 — Optional Pre-Brake Coupler (research)
Inputs: power budget, coil/tether parameters, environment models  
Outputs: force/torque authority estimates + controllability + constraints

---

## Interfaces (placeholders)
- `/sim/inputs/*.yaml` → canonical run configuration
- `/sim/output/*.jsonl` → time-series logs with event tags
- `/verification/cases/*` → golden cases + expected ranges
- `/docs/decision-log/*` → decisions that lock scope

---

## Required “win” metrics (placeholders)
- ΔV (or energy) removed by atmosphere vs baseline
- Peak dynamic pressure (q)
- Peak heating proxy (convective heat flux estimate)
- Peak g-load and jerk proxy
- Corridor width / robustness (Monte Carlo later)
- Mass/volume penalty of decel hardware
- Telemetry completeness (proof coverage)

(Exact thresholds to be added later under `/docs/requirements/`.)

---

## Open questions (not decisions)
- Mission class target(s): orbit capture vs landing vs both
- Vehicle mass classes to support (1t / 10t / 100t)
- Primary decelerator family: rigid aeroshell vs HIAD vs ballute
- Terminal trim strategy: propulsive vs aero-only vs hybrid
- Pre-brake inclusion: scope or separate track
