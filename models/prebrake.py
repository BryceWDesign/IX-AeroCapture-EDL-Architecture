id="ix_models_prebrake_v1"
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .contracts import RunConfig


@dataclass(frozen=True)
class PreBrakeForceEstimate:
    """
    Order-of-magnitude estimate for optional pre-brake couplers.

    Units:
      force_N: newtons
      torque_Nm: newton-meters (optional)
      notes: plain language assumptions
    """
    force_N: float
    torque_Nm: Optional[float] = None
    notes: str = ""


def estimate_prebrake_force(cfg: RunConfig) -> PreBrakeForceEstimate:
    """
    STUB: Estimate force from a pre-brake concept (magsail / e-sail / plasma-magnet).

    This must remain a research-track model (E1/E2) until validated.
    No claims of flight readiness.

    Raises:
      NotImplementedError until implemented.
    """
    raise NotImplementedError("Pre-brake force estimation not implemented yet.")
