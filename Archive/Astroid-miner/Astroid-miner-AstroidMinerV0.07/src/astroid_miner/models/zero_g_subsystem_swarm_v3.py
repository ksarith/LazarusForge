import numpy as np
from dataclasses import dataclass
from typing import Dict, List, Any

from astroid_miner.models.contracts import CapacityResult, coerce_capacity

# =============================================
# Constraint Graph for Astroid-miner Zero-G Replication
# Modular subsystems with explicit dependencies
# =============================================

@dataclass
class Asteroid:
    name: str
    composition: Dict[str, float]
    cohesion_kpa: float = 15.0

class Subsystem:
    def __init__(self, name: str, mass_fraction: float):
        self.name = name
        self.mass_fraction = mass_fraction
        self.state = {}  # e.g. dust, temperature

    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        """Maximum output this subsystem can provide this cycle (DEC-002)."""
        raise NotImplementedError

    def demand(self, flow: float, params: Dict) -> float:
        """Resources (power, mass, etc.) demanded to achieve target flow."""
        return 0.0

class PowerSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        mass = swarm_mass * self.mass_fraction
        solar = mass * params['panel_specific_power_kw_per_kg'] * (1.0 / params['au_distance']**2)
        return CapacityResult(
            capacity=solar,
            subsystem_id=self.name,
            units="kW",
            limiting_factor="panel_mass_and_au_distance",
            provenance="MDL-SWR-03",
        )

class AnchorSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        # Max force before slip
        mass = swarm_mass * self.mass_fraction
        force = mass * params['anchoring_force_n_per_kg']
        return CapacityResult(
            capacity=force,
            subsystem_id=self.name,
            units="N",
            limiting_factor="anchor_mass",
            provenance="MDL-SWR-03",
        )

class MiningSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        anchor_limit = coerce_capacity(global_state.get('anchor_capacity', 1e6))
        throttle = min(1.0, anchor_limit / max(global_state.get('cohesion_force', 1), 1e-6))
        mass = swarm_mass * self.mass_fraction
        dig = mass * params['dig_rate_kg_per_kg'] * throttle
        limiting = "anchor_throttle" if throttle < 1.0 else "mining_mass"
        return CapacityResult(
            capacity=dig,
            subsystem_id=self.name,
            units="kg/cycle",
            limiting_factor=limiting,
            provenance="MDL-SWR-03",
            meta={"throttle": throttle},
        )

class RefiningSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        mass = swarm_mass * self.mass_fraction
        spin_tax = mass * params.get('spin_power_tax_kw_per_kg', 0.005)
        available_power = max(0.0, coerce_capacity(global_state.get('power_available', 0)) - spin_tax)
        mass_limited = mass * params['refining_rate']
        power_limited = available_power * params['kg_per_kwh']
        value = min(mass_limited, power_limited)
        limiting = "refining_mass" if mass_limited <= power_limited else "available_power"
        return CapacityResult(
            capacity=value,
            subsystem_id=self.name,
            units="kg/cycle",
            limiting_factor=limiting,
            provenance="MDL-SWR-03",
        )

class FabricationSubsystem(Subsystem):
    def capacity(self, swarm_mass: float, params: Dict, global_state: Dict) -> CapacityResult:
        mass = swarm_mass * self.mass_fraction
        base = mass * params['fab_rate']
        yield_bonus = 1.15 if params.get('micro_g_slurry', True) else 1.0
        value = base * params['base_fab_yield'] * yield_bonus
        return CapacityResult(
            capacity=value,
            subsystem_id=self.name,
            units="kg/cycle",
            limiting_factor="fab_mass_and_yield",
            provenance="MDL-SWR-03",
            meta={"yield_bonus": yield_bonus},
        )

class ConstraintSolver:
    def __init__(self, subsystems: List[Subsystem], params: Dict):
        self.subsystems = {s.name: s for s in subsystems}
        self.params = params

    def solve_cycle(self, swarm_mass: float, asteroid: Asteroid, collection_method: str = "enclosed", cycle: int = 0):
        """
        cycle: elapsed-cycle counter, threaded through global_state per DEC-002
        (docs/decisions/DEC-002-subsystem-capacity-protocol.md). Added so subsystems
        that need cycle-dependent behavior (e.g. degradation curves) can read
        it from global_state rather than needing a separate calling convention.
        Non-breaking: existing callers that omit cycle get 0, identical to
        prior behavior for all subsystems that don't use it.
        """
        global_state = {'cycle': cycle}

        # Power
        power_result = self.subsystems['Power'].capacity(swarm_mass, self.params, global_state)
        global_state['power_available'] = coerce_capacity(power_result)
        global_state['power_result'] = power_result

        # Anchor
        anchor_result = self.subsystems['Anchor'].capacity(swarm_mass, self.params, global_state)
        global_state['anchor_capacity'] = coerce_capacity(anchor_result)
        global_state['anchor_result'] = anchor_result
        global_state['cohesion_force'] = asteroid.cohesion_kpa * self.params['tool_area_m2'] * 1000

        # Mining
        mining_result = self.subsystems['Mining'].capacity(swarm_mass, self.params, global_state)
        mined = coerce_capacity(mining_result)

        # Refining
        refining_result = self.subsystems['Refining'].capacity(swarm_mass, self.params, global_state)
        refined_raw = coerce_capacity(refining_result)
        processed = min(mined, refined_raw)

        refined_metal = processed * asteroid.composition.get('metal', 0.15)

        # Fabrication
        fab_result = self.subsystems['Fabrication'].capacity(swarm_mass, self.params, global_state)
        fab = coerce_capacity(fab_result)

        # Simple salvage placeholder (expand later)
        fabricated = min(fab, refined_metal * 1.2)  # rough

        results_by_name = {
            'Power': power_result,
            'Anchor': anchor_result,
            'Mining': mining_result,
            'Refining': refining_result,
            'Fabrication': fab_result,
        }
        bottleneck = min(
            results_by_name,
            key=lambda n: results_by_name[n].capacity,
        )

        return {
            'mined': mined,
            'processed': processed,
            'fabricated': fabricated,
            'power_available': global_state['power_available'],
            'bottleneck': bottleneck,
            'capacity_results': results_by_name,
        }

# =============================================
# Parameter loading (V0.02.1 Phase 2 addition)
# =============================================
DEFAULT_PARAMS = {
    'au_distance': 1.3,
    'panel_specific_power_kw_per_kg': 0.08,
    'anchoring_force_n_per_kg': 15.0,
    'tool_area_m2': 0.05,
    'dig_rate_kg_per_kg': 15.0,
    'refining_rate': 12.0,
    'kg_per_kwh': 2.5,
    'fab_rate': 8.0,
    'base_fab_yield': 0.65,
    'spin_power_tax_kw_per_kg': 0.005,
    'micro_g_slurry': True,
}


def load_params(yaml_path=None):
    """
    Optionally load parameters from parameters/swarm_v3.yaml (provenance-tracked).
    Falls back silently to DEFAULT_PARAMS if the file or PyYAML is unavailable,
    so this function is safe to call even without a YAML parser installed.

    Does not mutate DEFAULT_PARAMS. No numerical values change vs. the
    original hardcoded dict -- this only adds an optional loading path.
    """
    import os
    if yaml_path is None:
        # This module now lives at src/astroid_miner/models/, three levels
        # below the repo root, so parameters/ requires three ".." hops.
        yaml_path = os.path.join(
            os.path.dirname(__file__), "..", "..", "..", "parameters", "swarm_v3.yaml"
        )

    try:
        import yaml  # PyYAML
        with open(yaml_path, "r") as f:
            records = yaml.safe_load(f)
        params = dict(DEFAULT_PARAMS)
        for rec in records:
            params[rec["symbol"]] = rec["value"]
        return params
    except Exception:
        return dict(DEFAULT_PARAMS)


if __name__ == "__main__":
    # Example usage -- moved under __main__ guard (Phase 2) so importing this
    # module has no side effects. Uses load_params() which defaults to the
    # same hardcoded values unless parameters/swarm_v3.yaml overrides them.
    params = load_params()

    fractions = {
        'Power': 0.28, 'Anchor': 0.10, 'Mining': 0.20,
        'Refining': 0.18, 'Fabrication': 0.15, 'Other': 0.09
    }

    subsystems = [
        PowerSubsystem('Power', fractions['Power']),
        AnchorSubsystem('Anchor', fractions['Anchor']),
        MiningSubsystem('Mining', fractions['Mining']),
        RefiningSubsystem('Refining', fractions['Refining']),
        FabricationSubsystem('Fabrication', fractions['Fabrication'])
    ]

    solver = ConstraintSolver(subsystems, params)
    asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})

    result = solver.solve_cycle(8000.0, asteroid)
    print(result)
