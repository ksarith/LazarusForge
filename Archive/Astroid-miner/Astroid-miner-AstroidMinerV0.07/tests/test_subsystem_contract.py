"""
Repository contract tests for DEC-002 subsystem capacity protocol.

These tests ask: "Is every production subsystem allowed to claim it
implements the capacity contract?" — not "does the physics look right?"
"""

from __future__ import annotations

import inspect
import os
import sys
import unittest
from typing import get_type_hints

SRC = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.insert(0, os.path.abspath(SRC))

from astroid_miner.models.contracts import (  # noqa: E402
    CapacityResult,
    SubsystemProtocol,
    coerce_capacity,
)
from astroid_miner.models.power_subsystem import PowerSubsystem as StandalonePower  # noqa: E402
from astroid_miner.models.zero_g_subsystem_swarm_v3 import (  # noqa: E402
    AnchorSubsystem,
    Asteroid,
    ConstraintSolver,
    FabricationSubsystem,
    MiningSubsystem,
    PowerSubsystem as SwarmPower,
    RefiningSubsystem,
    Subsystem,
    DEFAULT_PARAMS,
)


PRODUCTION_SUBSYSTEM_CLASSES = [
    SwarmPower,
    StandalonePower,
    AnchorSubsystem,
    MiningSubsystem,
    RefiningSubsystem,
    FabricationSubsystem,
]


def _params():
    return dict(DEFAULT_PARAMS)


def _global_state(**extra):
    state = {"cycle": 0, "power_available": 100.0, "anchor_capacity": 1e6, "cohesion_force": 750.0}
    state.update(extra)
    return state


class TestCapacityResult(unittest.TestCase):
    def test_basic_fields(self):
        r = CapacityResult(
            capacity=12.5,
            subsystem_id="Power",
            units="kW",
            limiting_factor="panel_mass",
            provenance="test",
        )
        self.assertEqual(float(r), 12.5)
        self.assertEqual(r.subsystem_id, "Power")
        self.assertEqual(r.units, "kW")

    def test_rejects_empty_subsystem_id(self):
        with self.assertRaises(ValueError):
            CapacityResult(capacity=1.0, subsystem_id="", units="kW")

    def test_rejects_empty_units(self):
        with self.assertRaises(ValueError):
            CapacityResult(capacity=1.0, subsystem_id="X", units="")

    def test_coerce_capacity(self):
        r = CapacityResult(capacity=3.0, subsystem_id="A", units="kg")
        self.assertEqual(coerce_capacity(r), 3.0)
        self.assertEqual(coerce_capacity(7.0), 7.0)
        with self.assertRaises(TypeError):
            coerce_capacity("nope")

    def test_ordering(self):
        a = CapacityResult(capacity=1.0, subsystem_id="A", units="x")
        b = CapacityResult(capacity=2.0, subsystem_id="B", units="x")
        self.assertTrue(a < b)
        self.assertTrue(b > 1.5)


class TestSubsystemContract(unittest.TestCase):
    def test_all_production_subsystems_return_capacity_result(self):
        params = _params()
        state = _global_state()
        swarm_mass = 8000.0

        for cls in PRODUCTION_SUBSYSTEM_CLASSES:
            with self.subTest(cls=cls.__name__):
                if cls is StandalonePower:
                    inst = cls(mass_fraction=0.28, hts_enabled=False)
                else:
                    inst = cls(cls.__name__.replace("Subsystem", "") or "X", 0.2)
                    # Swarm power uses name as first arg
                    if cls is SwarmPower:
                        inst = cls("Power", 0.28)
                    elif cls is AnchorSubsystem:
                        inst = cls("Anchor", 0.10)
                    elif cls is MiningSubsystem:
                        inst = cls("Mining", 0.20)
                    elif cls is RefiningSubsystem:
                        inst = cls("Refining", 0.18)
                    elif cls is FabricationSubsystem:
                        inst = cls("Fabrication", 0.15)

                result = inst.capacity(swarm_mass, params, state)
                self.assertIsInstance(
                    result,
                    CapacityResult,
                    f"{cls.__name__}.capacity() must return CapacityResult, got {type(result)}",
                )
                self.assertIsInstance(result.capacity, (int, float))
                self.assertTrue(result.subsystem_id)
                self.assertTrue(result.units)
                self.assertGreaterEqual(result.capacity, 0.0)

    def test_protocol_runtime_check(self):
        inst = SwarmPower("Power", 0.28)
        self.assertIsInstance(inst, SubsystemProtocol)

    def test_base_subsystem_not_implemented(self):
        base = Subsystem("X", 0.1)
        with self.assertRaises(NotImplementedError):
            base.capacity(1000.0, _params(), _global_state())


class TestConstraintSolverUsesContract(unittest.TestCase):
    def test_solve_cycle_exposes_capacity_results(self):
        params = _params()
        fractions = {
            "Power": 0.28,
            "Anchor": 0.10,
            "Mining": 0.20,
            "Refining": 0.18,
            "Fabrication": 0.15,
        }
        subsystems = [
            SwarmPower("Power", fractions["Power"]),
            AnchorSubsystem("Anchor", fractions["Anchor"]),
            MiningSubsystem("Mining", fractions["Mining"]),
            RefiningSubsystem("Refining", fractions["Refining"]),
            FabricationSubsystem("Fabrication", fractions["Fabrication"]),
        ]
        solver = ConstraintSolver(subsystems, params)
        asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})
        result = solver.solve_cycle(8000.0, asteroid)

        self.assertIn("capacity_results", result)
        self.assertIn("fabricated", result)
        for name, cap in result["capacity_results"].items():
            self.assertIsInstance(cap, CapacityResult, name)
            self.assertEqual(cap.subsystem_id, name)

        self.assertIn(result["bottleneck"], result["capacity_results"])

    def test_standalone_power_drop_in(self):
        params = _params()
        params.setdefault("power_degradation_per_cycle", 0.025)
        params.setdefault("baseline_transmission_efficiency", 0.85)
        fractions = {
            "Power": 0.28,
            "Anchor": 0.10,
            "Mining": 0.20,
            "Refining": 0.18,
            "Fabrication": 0.15,
        }
        subsystems = [
            StandalonePower(fractions["Power"], hts_enabled=True),
            AnchorSubsystem("Anchor", fractions["Anchor"]),
            MiningSubsystem("Mining", fractions["Mining"]),
            RefiningSubsystem("Refining", fractions["Refining"]),
            FabricationSubsystem("Fabrication", fractions["Fabrication"]),
        ]
        solver = ConstraintSolver(subsystems, params)
        asteroid = Asteroid("C-type", {"water": 0.12, "metal": 0.18, "silicates": 0.70})
        result = solver.solve_cycle(8000.0, asteroid, cycle=3)
        self.assertIn("fabricated", result)
        self.assertIsInstance(result["capacity_results"]["Power"], CapacityResult)
        self.assertEqual(result["capacity_results"]["Power"].provenance, "MDL-PWR-01")


if __name__ == "__main__":
    unittest.main(verbosity=2)
