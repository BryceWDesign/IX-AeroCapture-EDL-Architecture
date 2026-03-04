# Case: CASE_XXXX — <Short title>

## Purpose
<Why this case exists. What behavior does it validate?>

## Scenario
- Body: <Mars/Earth/etc>
- Mission: <aerocapture-to-orbit / landing EDL / etc>
- Vehicle: mass/ref area/Cd/Cl
- Constraints: q_max/g_max/heating proxies (if locked)

## Inputs
- `config.json`

## Expected outputs (ranges)
- `expected_ranges.json`

## Evidence tag targets
- M-01 ΔV removed: E1/E2/E3...
- M-03 q_max: E1/E2/E3...
- M-05 heating proxy: E1/E2/E3...

## Pass/Fail definition
- PASS if all required metrics are present AND within defined ranges.
- FAIL otherwise.

## Notes
- Assumptions:
- Known limitations:
- Next tightening step:
