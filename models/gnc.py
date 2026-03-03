id="ix_models_gnc_v1"
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

from .contracts import Constraints, RunConfig, TrajectoryState


@dataclass(frozen=True)
class SafetyGateDecision:
    """
    Output of SafetyGate.
    """
    allowed: bool
    reason: str
    degraded_mode: Optional[str] = None
    tags: Dict[str, str] = None  # type: ignore[assignment]


def safety_gate(
    cfg: RunConfig,
    constraints: Constraints,
    state: TrajectoryState,
    q_Pa: Optional[float] = None,
    heating_W_m2: Optional[float] = None,
    g_load: Optional[float] = None,
) -> SafetyGateDecision:
    """
    Enforce hard constraints. v1 is a stub.

    Later behavior:
      - If a constraint value is UNSET (None), report it (do not assume).
      - If violated, mark not allowed and propose a conservative degraded_mode.

    Raises:
      NotImplementedError until implemented.
    """
    raise NotImplementedError("SafetyGate not implemented yet.")
