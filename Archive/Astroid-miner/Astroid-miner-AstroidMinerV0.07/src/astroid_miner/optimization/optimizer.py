"""
MDL-OPT-01 — Mass-allocation finite-difference optimizer (Phase 2 repaired interface)

Changes from original sketch (V0.02.1):
- Added missing imports (typing.Dict, Asteroid).
- Aligned growth metric to the actual key returned by ConstraintSolver.solve_cycle().
  Original code expected baseline['net_growth'] which never existed.
  The solver returns 'fabricated' (mass of new structure produced). We treat that
  as the growth signal for gradient estimation. This is an interface alignment,
  not a claim about physics fidelity.
- Function is now importable without NameError / KeyError on the interface.
- No numerical constants or model physics were altered.
"""

from typing import Dict
from astroid_miner.models.zero_g_subsystem_swarm_v3 import Asteroid, ConstraintSolver


def optimize_mass_allocation(
    solver: ConstraintSolver,
    current_mass: float,
    asteroid: Asteroid,
    cycle: int = 0,
    epsilon: float = 0.01,
    growth_key: str = "fabricated",
) -> Dict[str, float]:
    """
    Finite-difference gradient of a growth metric w.r.t. subsystem mass fractions.

    growth_key defaults to "fabricated", the key actually returned by
    ConstraintSolver.solve_cycle() (the original 'net_growth' key never existed).
    """
    baseline = solver.solve_cycle(current_mass, asteroid)
    if growth_key not in baseline:
        raise KeyError(
            f"Solver result does not contain growth_key='{growth_key}'. "
            f"Available keys: {list(baseline.keys())}"
        )
    baseline_growth = float(baseline[growth_key])

    gradients: Dict[str, float] = {}
    original_fractions = {
        name: sub.mass_fraction for name, sub in solver.subsystems.items()
    }

    for target in list(solver.subsystems.keys()):
        perturbed = original_fractions.copy()
        perturbed[target] += epsilon
        total_others = sum(v for k, v in perturbed.items() if k != target)
        scale = (1.0 - perturbed[target]) / (total_others + 1e-9)
        for k in perturbed:
            if k != target:
                perturbed[k] *= scale

        for name, frac in perturbed.items():
            solver.subsystems[name].mass_fraction = frac

        perturbed_result = solver.solve_cycle(current_mass, asteroid)
        gradients[target] = (
            float(perturbed_result[growth_key]) - baseline_growth
        ) / epsilon

    for name, frac in original_fractions.items():
        solver.subsystems[name].mass_fraction = frac

    return gradients


if __name__ == "__main__":
    from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
        PowerSubsystem, AnchorSubsystem, MiningSubsystem,
        RefiningSubsystem, FabricationSubsystem, ConstraintSolver, Asteroid
    )

    params = {
        "au_distance": 1.3,
        "panel_specific_power_kw_per_kg": 0.08,
        "anchoring_force_n_per_kg": 15.0,
        "tool_area_m2": 0.05,
        "dig_rate_kg_per_kg": 15.0,
        "refining_rate": 12.0,
        "kg_per_kwh": 2.5,
        "fab_rate": 8.0,
        "base_fab_yield": 0.65,
        "spin_power_tax_kw_per_kg": 0.005,
        "micro_g_slurry": True,
    }
    fractions = {
        "Power": 0.28, "Anchor": 0.10, "Mining": 0.20,
        "Refining": 0.18, "Fabrication": 0.15,
    }
    subsystems = [
        PowerSubsystem("Power", fractions["Power"]),
        AnchorSubsystem("Anchor", fractions["Anchor"]),
        MiningSubsystem("Mining", fractions["Mining"]),
        RefiningSubsystem("Refining", fractions["Refining"]),
        FabricationSubsystem("Fabrication", fractions["Fabrication"]),
    ]
    solver = ConstraintSolver(subsystems, params)
    asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})

    grads = optimize_mass_allocation(solver, 8000.0, asteroid)
    print("Interface repair self-test OK")
    print("Gradients (fabricated w.r.t. mass_fraction):")
    for k, v in grads.items():
        print(f"  {k}: {v:.6f}")
