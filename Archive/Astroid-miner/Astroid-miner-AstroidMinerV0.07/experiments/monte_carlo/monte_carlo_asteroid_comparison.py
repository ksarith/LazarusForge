"""
MDL-MC-03 — Comparative Monte Carlo asteroid model

*** DEPRECATED per DEC-001 (docs/decisions/DEC-001-silicate-pathway.md) ***
*** Resolved: option (b) — formal deprecation, 2026-08-12 ***

NOT functional: imports `Subsystem` from `replication_constraint_graph_v3`,
a module that does not exist anywhere in this repository. See MDL-MC-02's
notice and DEC-001 for the full reasoning — the same disposition applies
here.

Retained for provenance only. Do not build on this module.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from replication_constraint_graph_v3 import ConstraintSolver, Subsystem, Asteroid  # adjust import if needed

# ====================== PARAMETERS ======================
base_params = {
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
    'silicate_processing_rate': 10.0,
    'num_cycles': 15,
}

fractions = {
    'Power': 0.28, 'Anchor': 0.10, 'Mining': 0.20,
    'Refining': 0.18, 'Fabrication': 0.15, 'Silicates': 0.09
}

# ====================== ASTEROID DEFINITIONS ======================
metal_rich = Asteroid("M-type", {"metal": 0.55, "silicates": 0.35, "water": 0.05}, cohesion_kpa=25.0)
silicate_rich = Asteroid("C-type", {"metal": 0.18, "silicates": 0.70, "water": 0.12}, cohesion_kpa=12.0)

# ====================== RUN COMPARISON ======================
def run_comparison(num_runs=600):
    results = {'metal': [], 'silicate': []}
    
    for asteroid_type, asteroid in [('metal', metal_rich), ('silicate', silicate_rich)]:
        for run in range(num_runs):
            # Slight random variation per run
            params = base_params.copy()
            params['base_fab_yield'] = np.random.triangular(0.55, 0.65, 0.75)
            
            solver = ConstraintSolver([  # Rebuild subsystems each run if needed
                Subsystem('Power', fractions['Power']),
                # ... (add all subsystems as before)
            ], params)
            
            mass_history = [8000.0]  # seed mass
            for c in range(params['num_cycles']):
                result = solver.solve_cycle(mass_history[-1], asteroid)
                mass_history.append(mass_history[-1] + result['fabricated'] * 0.8)  # simplified growth
            
            results[asteroid_type].append(mass_history)
    
    return results

# Run and plot
data = run_comparison()

# Plot comparison
cycles = base_params['num_cycles'] + 1
plt.figure(figsize=(12, 7))

for label, color in [('metal', 'red'), ('silicate', 'blue')]:
    matrix = np.array(data[label])
    p5 = np.percentile(matrix, 5, axis=0)
    p50 = np.percentile(matrix, 50, axis=0)
    p95 = np.percentile(matrix, 95, axis=0)
    
    plt.plot(range(cycles), p50/1000, label=f'{label.capitalize()}-rich Median', color=color, lw=2.5)
    plt.fill_between(range(cycles), p5/1000, p95/1000, alpha=0.25, color=color, label=f'{label.capitalize()} 90% CI')

plt.yscale('log')
plt.xlabel('Replication Cycles')
plt.ylabel('Total System Mass (tonnes)')
plt.title('Monte Carlo Growth Comparison: Metal-rich vs Silicate-rich Asteroids')
plt.legend()
plt.grid(True, ls='--', alpha=0.6)
plt.show()

# Summary stats
for label in ['metal', 'silicate']:
    final_masses = [run[-1] for run in data[label]]
    success = sum(1 for m in final_masses if m > 8000*8) / len(final_masses)
    print(f"{label.capitalize()}-rich → Success rate (>8x): {success:.1%} | Median final mass: {np.median(final_masses)/1000:.1f} t")
