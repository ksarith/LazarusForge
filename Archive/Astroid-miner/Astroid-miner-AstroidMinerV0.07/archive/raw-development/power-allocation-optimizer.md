# Power Allocation Optimizer — Dynamic Mass Reallocation for Replication

**Status**: Conceptual → Working Model (integrated with replication_constraint_graph)

## Purpose

This module implements **adaptive subsystem allocation** during replication. Instead of fixed mass fractions, the swarm dynamically decides where to route newly fabricated mass based on current bottlenecks, asteroid composition, distance, and technology level (e.g. HTS availability).

This directly supports the **emergent roles** doctrine and closes the loop between power backbone realism and overall replication growth.

## Core Mechanism — Marginal Utility Optimizer

For each cycle, the optimizer computes the **marginal growth benefit** of shifting a small amount of mass (ε ≈ 1%) into each subsystem:

```python
gradients = optimize_mass_allocation(solver, current_mass, asteroid, cycle, look_ahead=3)
best_subsystem = max(gradients, key=gradients.get)
