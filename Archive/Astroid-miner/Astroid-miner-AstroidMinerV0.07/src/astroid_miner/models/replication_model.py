import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import Dict

# =============================================
# Astroid-miner Replication Model v2
# Subsystem-centric, bottlenecked, salvage-aware Monte Carlo
# =============================================

@dataclass
class Asteroid:
    name: str
    composition: Dict[str, float]  # water, metal, silicates (sum ≈ 1.0)
    cohesion_kpa: float = 15.0
    density: float = 2.0

    def __post_init__(self):
        total = sum(self.composition.values())
        if abs(total - 1.0) > 0.05:
            print(f"Warning: Composition sums to {total:.2f}")

class SubsystemSwarm:
    def __init__(self, initial_mass_kg: float, fractions: Dict[str, float], params: Dict):
        self.total_mass = initial_mass_kg
        self.fractions = fractions  # e.g. {'power': 0.28, 'mine': 0.22, ...}
        self.params = params
        self.salvage_pool_kg = 0.0
        self.cycle_history = []
        
    @property
    def masses(self) -> Dict[str, float]:
        return {k: self.total_mass * v for k, v in self.fractions.items()}
    
    def simulate_cycle(self, asteroid: Asteroid, au_distance: float):
        mass_map = self.masses
        cycle_data = {}
        
        # 1. Power (only from power subsystem)
        solar_scale = 1.0 / (au_distance ** 2)
        power_mass = mass_map.get('power', 0)
        available_power_kw = power_mass * self.params['panel_specific_power_kw_per_kg'] * solar_scale
        
        # 2. Bottlenecked pipeline
        phi_power = available_power_kw * self.params['kg_per_kwh']
        phi_mine = mass_map.get('mine', 0) * self.params['mining_multiplier']
        phi_refine = mass_map.get('refine', 0) * self.params['refining_multiplier']
        
        mined_raw = min(phi_power, phi_mine)
        
        # Yield by asteroid composition
        refined_metal = mined_raw * asteroid.composition.get('metal', 0.15)
        refined_water = mined_raw * asteroid.composition.get('water', 0.10)
        tailings = mined_raw - (refined_metal + refined_water)
        
        # 3. Fabrication (uses refined + salvage first)
        usable = refined_metal + (self.salvage_pool_kg * self.params['salvage_efficiency'])
        self.salvage_pool_kg *= (1 - self.params['salvage_efficiency'])
        
        phi_fab = mass_map.get('fab', 0) * self.params['fab_multiplier']
        fabricated = min(phi_fab, usable * self.params['fab_yield'])
        
        # 4. Attrition + Salvage
        failure_rate = self.params['base_failure_rate']
        failed = self.total_mass * failure_rate
        surviving = self.total_mass - failed
        
        self.salvage_pool_kg += failed * self.params['salvage_recovery']
        
        # Update
        self.total_mass = surviving + fabricated
        
        cycle_data = {
            'power_kw': available_power_kw,
            'mined_raw': mined_raw,
            'fabricated': fabricated,
            'tailings': tailings,
            'salvage': self.salvage_pool_kg,
            'bottleneck': 'power' if phi_power <= phi_mine else 'mine'
        }
        self.cycle_history.append(cycle_data)
        return fabricated

# Monte Carlo
def run_monte_carlo(base_params: Dict, num_runs: int = 800, num_cycles: int = 15):
    results = []
    for r in range(num_runs):
        params = base_params.copy()
        # Sample uncertainty
        params['fab_yield'] = np.random.triangular(0.35, base_params['fab_yield'], 0.72)
        params['failure_rate'] = np.random.triangular(0.03, base_params['base_failure_rate'], 0.18)
        
        swarm = SubsystemSwarm(
            initial_mass_kg=base_params['seed_mass_kg'],
            fractions=base_params['fractions'],
            params=params
        )
        
        asteroid = Asteroid("C-type NEA", {"water": 0.12, "metal": 0.18, "silicates": 0.70})
        
        mass_history = [base_params['seed_mass_kg']]
        for _ in range(num_cycles):
            swarm.simulate_cycle(asteroid, base_params['au_distance'])
            mass_history.append(swarm.total_mass)
        
        results.append({
            'run': r,
            'final_mass': mass_history[-1],
            'mass_history': mass_history,
            'success': mass_history[-1] > base_params['seed_mass_kg'] * 8
        })
    
    mass_matrix = np.array([r['mass_history'] for r in results])
    return results, mass_matrix

# Default parameters (tune these!)
default_params = {
    'seed_mass_kg': 8000.0,
    'au_distance': 1.3,
    'panel_specific_power_kw_per_kg': 0.08,
    'kg_per_kwh': 4500,
    'mining_multiplier': 1200,
    'refining_multiplier': 800,
    'fab_multiplier': 600,
    'fab_yield': 0.58,
    'base_failure_rate': 0.07,
    'salvage_efficiency': 0.65,
    'salvage_recovery': 0.75,
    'fractions': {
        'power': 0.28,
        'mine': 0.22,
        'refine': 0.18,
        'fab': 0.15,
        'struct': 0.12,
        'prop': 0.05
    }
}


if __name__ == "__main__":

    # Run it
    mc_results, mass_matrix = run_monte_carlo(default_params)

    # Plot
    cycles = len(mc_results[0]['mass_history'])
    p5 = np.percentile(mass_matrix, 5, axis=0)
    p50 = np.percentile(mass_matrix, 50, axis=0)
    p95 = np.percentile(mass_matrix, 95, axis=0)

    plt.figure(figsize=(10, 6))
    plt.plot(range(cycles), p50/1000, 'b-', lw=2.5, label='Median Mass')
    plt.fill_between(range(cycles), p5/1000, p95/1000, color='blue', alpha=0.25, label='90% CI')
    plt.yscale('log')
    plt.xlabel('Cycle')
    plt.ylabel('Total Mass (tonnes)')
    plt.title('Astroid-miner Swarm Growth (800 Monte Carlo runs)')
    plt.legend()
    plt.grid(True, ls='--', alpha=0.6)
    plt.show()

    success_rate = sum(1 for r in mc_results if r['success']) / len(mc_results)
    print(f"Success rate (>8x seed mass): {success_rate:.1%}")
