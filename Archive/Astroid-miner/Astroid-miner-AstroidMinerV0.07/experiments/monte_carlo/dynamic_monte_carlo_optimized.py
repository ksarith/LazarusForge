"""
MDL-MC-02 — Monte Carlo engine, silicate-comparison variant

*** DEPRECATED per DEC-001 (docs/decisions/DEC-001-silicate-pathway.md) ***
*** Resolved: option (b) — formal deprecation, 2026-08-12 ***

NOT functional: imports `Subsystem` and `SilicateSubsystem` from
`replication_constraint_graph_v3`, a module that does not exist anywhere in
this repository. Redirecting the import to the closest surviving relative,
`replication_constraint_graph_v4_silicate.py` (MDL-GRA-04), does not fix
this: that module is itself deprecated/non-functional and defines neither
`Subsystem` nor `SilicateSubsystem`. Real repair requires writing new model
code (a working SilicateSubsystem and a completed solve_cycle), which is
exactly what DEC-001 defers pending a decision to invest in it.

Retained for provenance only. Do not build on this module.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from replication_constraint_graph_v3 import ConstraintSolver, Subsystem, Asteroid, SilicateSubsystem

# 1. Initialize Subsystems with an intentionally poor, unoptimized allocation
initial_fractions = {
    'Power': 0.10,       # Intentionally starved
    'Mining': 0.40,      # Way too many miners, no power to run them
    'Refining': 0.20,
    'Fabrication': 0.20,
    'Silicates': 0.10
}

# 2. Base Engineering Parameters
params = {
    'au_distance': 1.5,
    'panel_specific_power_kw_per_kg': 0.08,
    'power_degradation_per_cycle': 0.025,
    'anchoring_force_n_per_kg': 15.0,
    'tool_area_m2': 0.05,
    'dig_rate_kg_per_kg': 15.0,
    'refining_rate': 12.0,
    'kg_per_kwh': 2.5,
    'fab_rate': 8.0,
    'base_fab_yield': 0.65,
    'spin_power_tax_kw_per_kg': 0.005,
    'silicate_processing_rate': 10.0,
    'base_failure_rate_per_cycle': 0.06,
    'sic_wear_reduction_coefficient': 1.5,
    'max_basalt_substitution_fraction': 0.35,
    'hts_enabled': True,
    'hts_mass_penalty_factor': 0.78,
    'hts_transmission_efficiency': 0.98,
    'baseline_transmission_efficiency': 0.85
}

# 3. Helper to rebuild solver with specific fractions
def build_solver(fractions, params):
    subsystems = [
        PowerSubsystem(fractions['Power'], hts_enabled=params['hts_enabled']),
        Subsystem('Mining', fractions['Mining']),
        Subsystem('Refining', fractions['Refining']),
        Subsystem('Fabrication', fractions['Fabrication']),
        SilicateSubsystem('Silicates', fractions['Silicates'])
    ]
    return ConstraintSolver(subsystems, params)

# Custom PowerSubsystem class containing the HTS/Degradation math
class PowerSubsystem(Subsystem):
    def __init__(self, mass_fraction: float, hts_enabled: bool = False):
        super().__init__('Power', mass_fraction)
        self.hts_enabled = hts_enabled
        
    def capacity(self, swarm_mass: float, params: dict, cycle: int = 0) -> float:
        base_specific = params['panel_specific_power_kw_per_kg']
        degradation = (1.0 - params.get('power_degradation_per_cycle', 0.025)) ** cycle
        effective_specific = base_specific * degradation
        
        if self.hts_enabled:
            effective_specific *= params.get('hts_mass_penalty_factor', 0.78)
            
        power_mass = swarm_mass * self.mass_fraction
        gross_power = power_mass * effective_specific * (1.0 / params['au_distance']**2)
        eta_trans = params['hts_transmission_efficiency'] if self.hts_enabled else params['baseline_transmission_efficiency']
        return gross_power * eta_trans

# 4. Simulation Execution Loop
def run_dynamic_simulation(asteroid, num_cycles=15, adaptation_rate=0.15):
    current_fractions = initial_fractions.copy()
    mass_history = [5000.0]  # 5-tonne seed
    fraction_history = [current_fractions.copy()]
    
    for cycle in range(num_cycles):
        current_mass = mass_history[-1]
        solver = build_solver(current_fractions, params)
        
        # Calculate performance gradients
        gradients = {}
        baseline_result = solver.solve_cycle(current_mass, asteroid, cycle)
        baseline_growth = baseline_result['net_growth']
        
        # Numerical gradient calculation
        epsilon = 0.01
        for name in current_fractions.keys():
            temp_fractions = current_fractions.copy()
            temp_fractions[name] += epsilon
            
            # Renormalize other fractions to preserve sum = 1.0
            sum_others = sum(v for k, v in temp_fractions.items() if k != name)
            scale = (1.0 - temp_fractions[name]) / (sum_others + 1e-9)
            for k in temp_fractions.keys():
                if k != name:
                    temp_fractions[k] *= scale
            
            temp_solver = build_solver(temp_fractions, params)
            temp_result = temp_solver.solve_cycle(current_mass, asteroid, cycle)
            gradients[name] = (temp_result['net_growth'] - baseline_growth) / epsilon
            
        # Update fractions using gradient ascent step
        updated_fractions = {}
        for name in current_fractions.keys():
            updated_fractions[name] = max(0.02, current_fractions[name] + adaptation_rate * gradients[name])
            
        # Final normalization pass
        total_frac = sum(updated_fractions.values())
        current_fractions = {k: v / total_frac for k, v in updated_fractions.items()}
        
        # Progress the actual physical system
        cycle_result = solver.solve_cycle(current_mass, asteroid, cycle)
        mass_history.append(current_mass + cycle_result['net_growth'])
        fraction_history.append(current_fractions.copy())
        
    return mass_history, fraction_history

# Run on C-type (high silicate) asteroid
c_type = Asteroid("C-type", {"metal": 0.15, "silicates": 0.73, "water": 0.12}, cohesion_kpa=10.0)
masses, fractions_over_time = run_dynamic_simulation(c_type)
