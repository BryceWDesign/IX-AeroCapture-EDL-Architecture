id="ix_models_init_v1"
"""
Models package (scaffolding).

This repo intentionally starts with interfaces/contracts first.
Implementations will be added only after mission focus + constraints are locked.
"""
from .contracts import (
    AtmospherePoint,
    AtmosphereProfile,
    VehicleParams,
    Constraints,
    RunConfig,
    TrajectoryState,
    RunResult,
)
