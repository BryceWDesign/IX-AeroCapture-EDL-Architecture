# Baselines (Working) — IX-AeroCapture-EDL-Architecture

Purpose:
We only claim "better" if we name a baseline and quantify the delta.

Status: **VOLATILE / IN-PROGRESS**

## Baseline families (choose one primary later)
### B-01 Propulsive capture baseline (reference)
- Description: capture by chemical or high-thrust propulsive burn at arrival.
- What it provides: a reference ΔV requirement and mass fraction impact.
- Notes: simplest comparison.

### B-02 Aerobraking baseline (traditional)
- Description: multiple-pass aerobraking using a rigid aeroshell/vehicle body.
- What it provides: operationally realistic corridor management baseline.

### B-03 HIAD/ballute-only baseline
- Description: atmospheric decel using deployable decelerator but without pre-brake coupling.
- What it provides: isolates benefit of upstream pre-brake (if included).

### B-04 Hybrid baseline (aerocapture + propulsive trim)
- Description: aerocapture to reduce energy + modest trim burn.
- What it provides: the baseline most similar to our target architecture.

## Required baseline reporting (per run)
Every run report must include:
- baseline ID used
- baseline assumptions (mass, Cd/Cl, atmosphere model)
- delta vs baseline for:
  - remaining ΔV
  - q_max
  - heating proxy peak
  - g_max
  - mass/volume penalties

## Golden baseline cases (to be added)
When we add `/verification/cases/`, each case must specify:
- a baseline family
- expected outcome ranges (even if broad at first)
