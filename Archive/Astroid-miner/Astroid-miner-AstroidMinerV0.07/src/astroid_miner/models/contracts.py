"""
DEC-002 subsystem capacity contract.

All production subsystems under src/astroid_miner/models/ that participate in
the constraint solver must implement:

    capacity(swarm_mass, params, global_state) -> CapacityResult

Returning a bare float is no longer the production contract. ConstraintSolver
and the optimizer consume CapacityResult.capacity; limiting_factor and units
exist so callers can reason about bottlenecks without scraping ad-hoc dicts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Mapping, Optional, Protocol, runtime_checkable


@dataclass(frozen=True)
class CapacityResult:
    """Structured result of a subsystem capacity() call (DEC-002)."""

    capacity: float
    subsystem_id: str
    units: str
    limiting_factor: Optional[str] = None
    provenance: Optional[str] = None
    meta: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.capacity, (int, float)):
            raise TypeError(
                f"CapacityResult.capacity must be numeric, got {type(self.capacity)!r}"
            )
        if not self.subsystem_id:
            raise ValueError("CapacityResult.subsystem_id must be non-empty")
        if not self.units:
            raise ValueError("CapacityResult.units must be non-empty")

    def __float__(self) -> float:
        return float(self.capacity)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, CapacityResult):
            return self.capacity < other.capacity
        if isinstance(other, (int, float)):
            return self.capacity < float(other)
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, CapacityResult):
            return self.capacity <= other.capacity
        if isinstance(other, (int, float)):
            return self.capacity <= float(other)
        return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, CapacityResult):
            return self.capacity > other.capacity
        if isinstance(other, (int, float)):
            return self.capacity > float(other)
        return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, CapacityResult):
            return self.capacity >= other.capacity
        if isinstance(other, (int, float)):
            return self.capacity >= float(other)
        return NotImplemented


def coerce_capacity(value: Any) -> float:
    """Extract a numeric capacity from CapacityResult or bare float."""
    if isinstance(value, CapacityResult):
        return float(value.capacity)
    if isinstance(value, (int, float)):
        return float(value)
    raise TypeError(
        f"Expected CapacityResult or numeric capacity, got {type(value)!r}"
    )


@runtime_checkable
class SubsystemProtocol(Protocol):
    """Structural contract for production subsystems (DEC-002)."""

    name: str
    mass_fraction: float

    def capacity(
        self,
        swarm_mass: float,
        params: Dict[str, Any],
        global_state: Dict[str, Any],
    ) -> CapacityResult:
        ...
