"""
MDL-PWR-01 — Standalone power subsystem model (Phase 3.1 partial interface repair;
capacity() signature reconciled per DEC-002)

Changes from original sketch:
- Added missing imports: `Subsystem` (from the authoritative swarm model) and
  `typing.Dict`.
- DEC-002 (docs/decisions/DEC-002-subsystem-capacity-protocol.md), option (a):
  capacity() now takes (swarm_mass, params, global_state) matching the
  authoritative ConstraintSolver's calling convention, instead of a bare
  `cycle: int`. The cycle count is read from global_state['cycle'] (added to
  solve_cycle() in the same change) rather than passed positionally. This
  makes this richer PowerSubsystem (HTS penalty, transmission efficiency,
  degradation curve) usable as a drop-in replacement for ConstraintSolver's
  simpler built-in PowerSubsystem class.
- V0.08: capacity() returns CapacityResult (DEC-002 hard interface), not a bare float.

This module is verified compatible with ConstraintSolver.solve_cycle()
(see tests/test_optimizer_interface.py::test_power_subsystem_wired_into_solver).
"""

from typing import Dict

from astroid_miner.models.contracts import CapacityResult
from astroid_miner.models.zero_g_subsystem_swarm_v3 import Subsystem


class PowerSubsystem(Subsystem):
    def __init__(
        self,
        mass_fraction: float,
        hts_enabled: bool = False,
        dormant_spares_fraction: float = 0.15,
    ):
        super().__init__("Power", mass_fraction)
        self.hts_enabled = hts_enabled
        self.dormant_spares_fraction = dormant_spares_fraction  # From fault-tolerant-power-control.md

    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        cycle = global_state.get("cycle", 0)
        base_specific = params["panel_specific_power_kw_per_kg"]

        # Degradation (radiation, thermal cycling, dust)
        degradation = (1.0 - params.get("power_degradation_per_cycle", 0.025)) ** cycle
        effective_specific = base_specific * degradation

        # HTS mass penalty (encapsulation, shielding)
        if self.hts_enabled:
            effective_specific *= params.get("hts_mass_penalty_factor", 0.78)  # ~22% penalty

        power_mass = swarm_mass * self.mass_fraction * (1 - self.dormant_spares_fraction)
        gross_power = power_mass * effective_specific * (1.0 / params["au_distance"] ** 2)

        # Transmission efficiency
        eta_trans = (
            params.get("hts_transmission_efficiency", 0.98)
            if self.hts_enabled
            else params.get("baseline_transmission_efficiency", 0.85)
        )

        value = gross_power * eta_trans
        limiting = "hts_path" if self.hts_enabled else "baseline_transmission"
        return CapacityResult(
            capacity=value,
            subsystem_id=self.name,
            units="kW",
            limiting_factor=limiting,
            provenance="MDL-PWR-01",
            meta={
                "cycle": cycle,
                "degradation": degradation,
                "hts_enabled": self.hts_enabled,
                "eta_trans": eta_trans,
            },
        )
