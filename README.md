# IX-AeroCapture-EDL-Architecture

**Proof-first aerocapture + Entry/Descent/Landing (EDL) deceleration architecture** for reproducible trade studies.

This repository is built around one idea: **if you can’t rerun it from a single config and audit what happened, it doesn’t count.**  
So instead of starting with marketing claims or “magic braking,” this repo starts with **constraints, baselines, telemetry, and verification** — then layers models only after scope is locked.

**Maintainer:** Bryce Lovell  
**License:** Apache-2.0  
**Status:** Active development (README intentionally lean; details live in `/docs`)

---

## Why this exists (why a NASA/SpaceX engineer would care)

Braking/capture problems die in review for predictable reasons:
- unclear assumptions,
- hidden constants,
- no baselines,
- no reproducibility,
- “trust me” outputs with no proof trail.

This repo targets the opposite:
- **Corridor / heating / q / g constraints** are first-class
- results are **replayable**
- verification is **range-based early** (no fake precision)
- every run produces **audit-grade artifacts** (config echo + JSONL telemetry + result bundle)

This is intended to be useful to:
- Mission design (aerocapture trades, capture energy vs propulsive ΔV)
- EDL/GNC (corridor shaping under constraints)
- TPS/structures (heating proxy + q gates + margin reporting)
- Tooling/verification folks (repeatability + regression harness)

---

## What this repo is (and is not)

### ✅ Is
- An **architecture + workflow** for aerocapture/EDL deceleration studies
- A **simulation harness scaffold** (config → run → telemetry → result)
- A **verification scaffold** (golden cases + range checks)
- A **telemetry/proof scaffold** for reviewable evidence artifacts

### ❌ Is not
- A claim of reactionless braking
- A warp/negative-energy dependency
- A finished physics toolchain (models are intentionally stubbed until scope is locked)

---

## Start here (canonical docs)

1) **Architecture Map:** `docs/architecture/ARCH_MAP.md`  
2) **Decision Log:** `docs/decision-log/DECISION_LOG.md`  
3) **Requirements:** `docs/requirements/`  
   - `METRICS.md` (what we measure)
   - `CONSTRAINTS.md` (hard gates)
   - `BASELINES.md` (what “better” means)

Repo guardrails:
- `CLAIMS_POLICY.md`
- `SCOPE.md`

---

## Repository layout (what’s inside)

- `docs/` — architecture, decisions, requirements (this is where the real content lives right now)
- `models/` — **interfaces/contracts** only (physics implementations come later)
- `sim/` — run harness (config IO + JSONL telemetry + result bundle)
- `verification/` — golden-case scaffolding + range checker
- `telemetry/` — proof bundle tools + schema + basic validators

---

## Quickstart (scaffold runs)

### 1) Run a minimal scaffold config
```bash
python -m sim.run sim/example_configs/minimal_run.json

This creates:

sim_output/<timestamp>_<hash>/config.echo.json

sim_output/<timestamp>_<hash>/telemetry.jsonl

sim_output/<timestamp>_<hash>/result.json

Note: models are not executed yet (by design). This validates the run pipeline and proof trail.

2) Run the minimal verification case

python verification/run_case.py verification/cases/case_000_minimal

3) Validate telemetry format (basic)

python -m telemetry.validate_basic sim_output/<run_id>/telemetry.jsonl

Evidence levels (how this repo stays credible)

This repo uses explicit evidence tags:

E0 concept

E1 toy model

E2 implemented model

E3 cross-checked

E4 measured

E5 flight relevant

If a claim is stronger than E1, it must link to the model producing it and its assumptions.

Roadmap (near-term, realistic)

Lock mission focus (aerocapture-to-orbit vs landing EDL vs both) via Decision Log

Implement a first E1/E2 atmosphere + aero proxy + heating proxy (explicit assumptions)

Add initial golden cases with published-range cross-check targets (E3 path)

Expand verification to include constraint violations and degrade modes

Improve proof bundles (packaging + stronger schema checks)

Contributing

See CONTRIBUTING.md.
Key rule while architecture is evolving: do not churn the README — add substance to /docs, cases, and checks.

Disclaimer

This is an independent engineering repo and is not affiliated with NASA, SpaceX, or any other organization.
