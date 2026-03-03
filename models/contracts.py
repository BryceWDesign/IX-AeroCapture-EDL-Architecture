id="ix_model_contracts_v1"
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional


# -----------------------------
# Atmosphere contracts
# -----------------------------

@dataclass(frozen=True)
class AtmospherePoint:
    """
    Single atmosphere sample point.

    Units:
      alt_m: meters
      rho_kg_m3: kg / m^3
      T_K: kelvin
      p_Pa: pascal
      a_m_s: speed of sound, m/s
    """
    alt_m: float
    rho_kg_m3: float
    T_K: float
    p_Pa: float
    a_m_s: float


@dataclass(frozen=True)
class AtmosphereProfile:
    """
    Ordered list of atmosphere points (typically increasing altitude).
    """
    points: List[AtmospherePoint]
    model_id: str
    notes: str = ""


# -----------------------------
# Vehicle + constraints
# -----------------------------

@dataclass(frozen=True)
class VehicleParams:
    """
    Vehicle parameters for low/early fidelity modeling.

    Units:
      mass_kg: kg
      ref_area_m2: m^2  (reference area for aero forces)
      cd: dimensionless (drag coefficient placeholder)
      cl: dimensionless (lift coefficient placeholder)
    """
    mass_kg: float
    ref_area_m2: float
    cd: float
    cl: float = 0.0

    @property
    def ballistic_coefficient_kg_m2(self) -> float:
        """
        Simple ballistic coefficient proxy: beta = m / (Cd * A)
        """
        if self.cd <= 0.0 or self.ref_area_m2 <= 0.0:
            raise ValueError("cd and ref_area_m2 must be > 0 to compute ballistic coefficient.")
        return self.mass_kg / (self.cd * self.ref_area_m2)


@dataclass(frozen=True)
class Constraints:
    """
    Hard gates. Values may be None until locked.

    Units:
      q_max_Pa: Pa (dynamic pressure)
      g_max: g units (dimensionless)
      heating_max_W_m2: W/m^2 (proxy)
    """
    q_max_Pa: Optional[float] = None
    g_max: Optional[float] = None
    heating_max_W_m2: Optional[float] = None

    # Optional: packaging/power placeholders
    mass_penalty_max_kg: Optional[float] = None
    stowed_volume_max_m3: Optional[float] = None
    peak_power_max_W: Optional[float] = None


# -----------------------------
# Trajectory + run config/result
# -----------------------------

@dataclass(frozen=True)
class TrajectoryState:
    """
    Minimal state for v1/v2 proxies.

    Units:
      t_s: seconds
      alt_m: meters
      v_m_s: m/s (speed magnitude)
      gamma_rad: flight-path angle (rad), sign convention documented later
    """
    t_s: float
    alt_m: float
    v_m_s: float
    gamma_rad: float


@dataclass(frozen=True)
class RunConfig:
    """
    Canonical simulation configuration.
    Keep fields JSON-serializable.

    Examples:
      mission: "Mars aerocapture to orbit" / "Mars EDL landing"
      body: "Mars" / "Earth"
    """
    mission: str
    body: str
    vehicle: VehicleParams
    constraints: Constraints

    # Model selectors (strings so we can swap implementations without breaking configs)
    atmosphere_model_id: str = "UNSET"
    aero_model_id: str = "UNSET"
    thermal_model_id: str = "UNSET"
    gnc_model_id: str = "UNSET"
    prebrake_model_id: str = "NONE"

    # Free-form parameters (documented per model)
    params: Dict[str, Any] = None  # type: ignore[assignment]

    def to_json_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["vehicle"] = asdict(self.vehicle)
        d["constraints"] = asdict(self.constraints)
        if d.get("params") is None:
            d["params"] = {}
        return d


@dataclass(frozen=True)
class RunResult:
    """
    Output bundle. Keep JSON-serializable.

    v1 outputs are placeholders until models are implemented.
    """
    config_hash: str
    model_versions: Dict[str, str]

    # Core metrics (may be None until implemented)
    delta_v_removed_m_s: Optional[float] = None
    delta_v_remaining_m_s: Optional[float] = None
    q_max_Pa: Optional[float] = None
    g_max: Optional[float] = None
    heating_proxy_max_W_m2: Optional[float] = None

    # Proof layer
    telemetry_path: Optional[str] = None
    notes: str = ""

    def to_json_dict(self) -> Dict[str, Any]:
        return asdict(self)
