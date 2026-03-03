id="ix_model_overview_v1"
# Models (Scaffold Only)

Status: **Interfaces + contracts only** (no locked equations yet)

Purpose:
- Provide a stable place to implement:
  - atmospheric models
  - aero / aerocapture approximations
  - heating proxies (TPS sizing proxy)
  - GNC safety gating logic
  - optional pre-brake coupler proxies (research lane)

Rules:
- Any numeric model must declare:
  - variables + units
  - assumptions
  - evidence tag (E1–E5) per `CLAIMS_POLICY.md`

Code structure (current):
- `contracts.py` — dataclasses and type contracts
- `atmosphere.py` — atmosphere profile interface (stub)
- `aero.py` — aerodynamics / decel proxy interface (stub)
- `thermal.py` — heating proxy interface (stub)
- `gnc.py` — safety gate interface (stub)
- `prebrake.py` — optional pre-brake coupler interface (stub)

Nothing in this folder should claim "better than baseline" until:
- `docs/requirements/CONSTRAINTS.md` thresholds are set, and
- we have at least E2 models + E3 cross-check on golden cases.
