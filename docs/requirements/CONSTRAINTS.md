# Constraints (Working) — IX-AeroCapture-EDL-Architecture

Status: **VOLATILE / IN-PROGRESS**
Constraints are hard gates. If a candidate trajectory or architecture violates a constraint,
the system must either:
- degrade to a safer mode, or
- declare "not feasible under current assumptions."

## C-01 Structural limits
- Max dynamic pressure (q_max): TBD Pa
- Max normal load factor (g_max): TBD g
- Max bending moment proxy: TBD (define later)
- Deployment stability constraints: TBD (define later)

## C-02 Thermal / TPS limits
- Peak heating proxy (q_dot_max): TBD W/m^2
- Peak surface temperature proxy: TBD K
- Heat load (integrated): TBD J/m^2
- TPS margin requirement: TBD %

## C-03 Guidance / control limits
- Max bank angle / rate: TBD deg / deg/s
- Max AoA / rate: TBD deg / deg/s
- Control authority requirements: TBD
- Abort triggers: TBD

## C-04 Packaging / integration limits
- Max stowed volume: TBD m^3
- Max deployed diameter/area: TBD
- Mass budget cap: TBD kg or %

## C-05 Power / energy limits
- Peak power: TBD W
- Available energy: TBD Wh
- Thermal rejection limit (radiators): TBD W

## C-06 Verification / proof limits
- Required signals by phase: TBD
- Minimum sampling rates: TBD
- Required event markers: TBD

## Notes
- Constraints will be locked via Decision Log entries once mission class and vehicle class are chosen.
- Until locked, all constraint checks should report "UNSET" rather than silently assuming values.
