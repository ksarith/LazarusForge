"""
Astroid-miner models — public API.

Primary swarm / constraint stack (MDL-SWR-03):
  Asteroid, Subsystem, ConstraintSolver, subsystem classes, load_params

Standalone power (MDL-PWR-01, DEC-002 capacity signature):
  PowerSubsystem  (richer drop-in; distinct from the simple class inside swarm v3)

Older parallel models (still authoritative, import-safe):
  SubsystemSwarm, run_monte_carlo  (MDL-REP-01)
  ZeroGSubsystemSwarm              (MDL-SIM-01)
"""

from astroid_miner.models.contracts import CapacityResult, SubsystemProtocol, coerce_capacity
from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
    Asteroid,
    Subsystem,
    AnchorSubsystem,
    MiningSubsystem,
    RefiningSubsystem,
    FabricationSubsystem,
    ConstraintSolver,
    DEFAULT_PARAMS,
    load_params,
)
from astroid_miner.models.zero_g_subsystem_swarm_v3 import (
    PowerSubsystem as SwarmPowerSubsystem,
)
from astroid_miner.models.power_subsystem import PowerSubsystem
from astroid_miner.models.replication_model import SubsystemSwarm, run_monte_carlo
from astroid_miner.models.zero_g_simulator import ZeroGSubsystemSwarm

# Re-export simulator's Asteroid under a distinct name if needed by callers
from astroid_miner.models.zero_g_simulator import Asteroid as SimulatorAsteroid
from astroid_miner.models.replication_model import Asteroid as ReplicationAsteroid

__all__ = [
    # DEC-002 contract
    "CapacityResult",
    "SubsystemProtocol",
    "coerce_capacity",
    # Primary swarm stack (MDL-SWR-03)
    "Asteroid",
    "Subsystem",
    "SwarmPowerSubsystem",
    "AnchorSubsystem",
    "MiningSubsystem",
    "RefiningSubsystem",
    "FabricationSubsystem",
    "ConstraintSolver",
    "DEFAULT_PARAMS",
    "load_params",
    # Standalone power (MDL-PWR-01)
    "PowerSubsystem",
    # Parallel models
    "SubsystemSwarm",
    "run_monte_carlo",
    "ReplicationAsteroid",
    "ZeroGSubsystemSwarm",
    "SimulatorAsteroid",
]
