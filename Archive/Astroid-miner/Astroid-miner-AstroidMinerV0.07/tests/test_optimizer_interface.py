"""
Minimal contract test for MDL-OPT-01 (astroid_miner.optimization.optimizer)

Run with the repo's src/ on PYTHONPATH, e.g.:
    python3 -m pytest tests/test_optimizer_interface.py -q
or simply:
    python3 tests/test_optimizer_interface.py

Phase 3 note: this test was updated to import from the src/astroid_miner
package layout instead of the old flat notebooks/ directory. No test
logic or assertions were changed -- only the import paths.
"""

import sys
import os
import unittest

SRC = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.insert(0, os.path.abspath(SRC))

from astroid_miner.optimization.optimizer import optimize_mass_allocation
from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
    Asteroid,
    ConstraintSolver,
    PowerSubsystem,
    AnchorSubsystem,
    MiningSubsystem,
    RefiningSubsystem,
    FabricationSubsystem,
)


def _make_solver():
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
        "Power": 0.28,
        "Anchor": 0.10,
        "Mining": 0.20,
        "Refining": 0.18,
        "Fabrication": 0.15,
    }
    subsystems = [
        PowerSubsystem("Power", fractions["Power"]),
        AnchorSubsystem("Anchor", fractions["Anchor"]),
        MiningSubsystem("Mining", fractions["Mining"]),
        RefiningSubsystem("Refining", fractions["Refining"]),
        FabricationSubsystem("Fabrication", fractions["Fabrication"]),
    ]
    return ConstraintSolver(subsystems, params)


class TestOptimizerInterface(unittest.TestCase):
    def setUp(self):
        self.solver = _make_solver()
        self.asteroid = Asteroid(
            "C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70}
        )
        self.mass = 8000.0

    def test_returns_dict_of_floats(self):
        grads = optimize_mass_allocation(self.solver, self.mass, self.asteroid)
        self.assertIsInstance(grads, dict)
        self.assertTrue(len(grads) > 0)
        for name, value in grads.items():
            self.assertIsInstance(name, str)
            self.assertIsInstance(value, float)

    def test_keys_match_subsystems(self):
        grads = optimize_mass_allocation(self.solver, self.mass, self.asteroid)
        self.assertEqual(set(grads.keys()), set(self.solver.subsystems.keys()))

    def test_fractions_restored_after_call(self):
        original = {n: s.mass_fraction for n, s in self.solver.subsystems.items()}
        _ = optimize_mass_allocation(self.solver, self.mass, self.asteroid)
        restored = {n: s.mass_fraction for n, s in self.solver.subsystems.items()}
        self.assertEqual(original, restored)

    def test_growth_key_missing_raises(self):
        with self.assertRaises(KeyError):
            optimize_mass_allocation(
                self.solver,
                self.mass,
                self.asteroid,
                growth_key="net_growth_that_does_not_exist",
            )

    def test_default_growth_key_is_fabricated(self):
        grads = optimize_mass_allocation(self.solver, self.mass, self.asteroid)
        self.assertIn("Power", grads)


class TestModelImportSmoke(unittest.TestCase):
    """
    Phase 3.1 addition: actually import/instantiate every model under
    src/astroid_miner/models/ rather than trusting REGISTRY.md's prior
    claims. This is what caught MDL-PWR-01 and MDL-GRA-04 in the first
    place -- they had never been executed standalone before.
    """

    def test_power_subsystem_standalone(self):
        from astroid_miner.models.power_subsystem import PowerSubsystem
        p = PowerSubsystem(mass_fraction=0.28, hts_enabled=True)
        params = {
            "panel_specific_power_kw_per_kg": 0.08,
            "au_distance": 1.3,
        }
        # DEC-002: capacity() takes global_state and returns CapacityResult.
        from astroid_miner.models.contracts import CapacityResult
        result = p.capacity(8000.0, params, {"cycle": 1})
        self.assertIsInstance(result, CapacityResult)
        self.assertIsInstance(result.capacity, float)
        self.assertGreater(result.capacity, 0.0)

    def test_power_subsystem_wired_into_solver(self):
        """
        DEC-002 resolution (option a): the richer standalone PowerSubsystem
        (HTS penalty, transmission efficiency, degradation curve) can now be
        used as a drop-in replacement for ConstraintSolver's simpler built-in
        PowerSubsystem class, because both implement
        capacity(swarm_mass, params, global_state).
        """
        from astroid_miner.models.power_subsystem import PowerSubsystem
        from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
            Asteroid, ConstraintSolver, AnchorSubsystem, MiningSubsystem,
            RefiningSubsystem, FabricationSubsystem, load_params,
        )
        params = load_params()
        fractions = {"Power": 0.28, "Anchor": 0.10, "Mining": 0.20,
                     "Refining": 0.18, "Fabrication": 0.15}
        subsystems = [
            PowerSubsystem(fractions["Power"], hts_enabled=True),
            AnchorSubsystem("Anchor", fractions["Anchor"]),
            MiningSubsystem("Mining", fractions["Mining"]),
            RefiningSubsystem("Refining", fractions["Refining"]),
            FabricationSubsystem("Fabrication", fractions["Fabrication"]),
        ]
        solver = ConstraintSolver(subsystems, params)
        asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})

        result_cycle0 = solver.solve_cycle(8000.0, asteroid, cycle=0)
        result_cycle5 = solver.solve_cycle(8000.0, asteroid, cycle=5)

        self.assertIn("power_available", result_cycle0)
        # Degradation curve must actually reduce power over cycles, not just
        # type-check -- confirms this is a real integration, not a stub.
        self.assertLess(result_cycle5["power_available"], result_cycle0["power_available"])

    def test_replication_model_imports(self):
        # Known to print demo output on import (side effect, not fixed here).
        import astroid_miner.models.replication_model  # noqa: F401

    def test_zero_g_simulator_imports(self):
        import astroid_miner.models.zero_g_simulator  # noqa: F401

    def test_swarm_v3_solve_cycle_runs(self):
        from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
            Asteroid, ConstraintSolver, PowerSubsystem, AnchorSubsystem,
            MiningSubsystem, RefiningSubsystem, FabricationSubsystem, load_params,
        )
        params = load_params()
        fractions = {"Power": 0.28, "Anchor": 0.10, "Mining": 0.20,
                     "Refining": 0.18, "Fabrication": 0.15}
        subsystems = [
            PowerSubsystem("Power", fractions["Power"]),
            AnchorSubsystem("Anchor", fractions["Anchor"]),
            MiningSubsystem("Mining", fractions["Mining"]),
            RefiningSubsystem("Refining", fractions["Refining"]),
            FabricationSubsystem("Fabrication", fractions["Fabrication"]),
        ]
        solver = ConstraintSolver(subsystems, params)
        asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})
        result = solver.solve_cycle(8000.0, asteroid)
        self.assertIn("fabricated", result)

    def test_replication_constraint_graph_v4_silicate_is_known_broken(self):
        """
        Documents, rather than hides, the MDL-GRA-04 defect: the module
        (now under experiments/deprecated/) can still be loaded, but
        solve_cycle() fails on undefined names (processed_raw_kg,
        raw_metals, fab_capacity are never assigned). This test asserts the
        failure mode explicitly so a future repair is required to change
        this test, not silently break something that looked passing.
        """
        import importlib.util
        mod_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "experiments",
            "deprecated",
            "replication_constraint_graph_v4_silicate.py",
        )
        spec = importlib.util.spec_from_file_location(
            "replication_constraint_graph_v4_silicate",
            os.path.abspath(mod_path),
        )
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        solver = mod.ConstraintSolver({"base_fab_yield": 0.65})
        asteroid = mod.Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})
        with self.assertRaises(NameError):
            solver.solve_cycle(8000.0, asteroid)


if __name__ == "__main__":
    unittest.main(verbosity=2)
