"""Astroid Miner — salvage-first zero-g mining and replication models."""

__version__ = "0.7.0"

# Convenience re-exports of the primary public surface
from astroid_miner.models import (
    CapacityResult,
    Asteroid,
    ConstraintSolver,
    PowerSubsystem,
    SwarmPowerSubsystem,
    load_params,
    DEFAULT_PARAMS,
)
from astroid_miner.optimization import optimize_mass_allocation

__all__ = [
    "__version__",
    "CapacityResult",
    "Asteroid",
    "ConstraintSolver",
    "PowerSubsystem",
    "SwarmPowerSubsystem",
    "load_params",
    "DEFAULT_PARAMS",
    "optimize_mass_allocation",
]
