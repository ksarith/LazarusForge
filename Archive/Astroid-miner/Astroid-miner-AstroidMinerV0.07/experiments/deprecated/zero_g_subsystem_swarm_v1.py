import numpy as np
from dataclasses import dataclass
from typing import Dict

@dataclass
class Asteroid:
    name: str
    composition: Dict[str, float]  # water, metal, silicates, ...
    cohesion_kpa: float = 15.0

class ZeroGSubsystemSwarm:
    def __init__(self, initial_mass_kg: float, fractions: Dict[str, float], params: Dict):
        self.total_mass = initial_mass_kg
        self.fractions = fractions
        self.params = params
        self.salvage_pool_kg = 0.0
        self.tailings = {'silicates': 0.0, 'other': 0.0}  # Split for usability
        self.dust_inventory = 0.0  # Emerging environmental state

    @property
    def masses(self):
        return {k: self.total_mass * v for k, v in self.fractions.items()}

    def simulate_cycle(self, asteroid, au_distance: float, collection_method="enclosed_bag"):
        mass_map = self.masses
        
        # Power with spin tax
        solar_scale = 1.0 / (au_distance ** 2)
        total_power = mass_map.get('power', 0) * self.params['panel_specific_power_kw_per_kg'] * solar_scale
        spin_tax = mass_map.get('refine', 0) * self.params.get('spin_power_tax_kw_per_kg', 0.005)
        available_power = max(0, total_power - spin_tax)
        
        # Anchoring-limited mining
        tool_force_limit = mass_map.get('mine', 0) * self.params['anchoring_force_n_per_kg']
        cohesion_force = asteroid.cohesion_kpa * self.params['tool_area_m2'] * 1000
        throttle = min(1.0, tool_force_limit / max(cohesion_force, 1e-6))
        
        nominal_mine = mass_map.get('mine', 0) * self.params['dig_rate_kg_per_kg']
        mined_raw = nominal_mine * throttle
        
        # Refining & yields
        refine_cap = min(mass_map.get('refine', 0) * self.params['refining_rate'], available_power * self.params['kg_per_kwh'])
        processed = min(mined_raw, refine_cap)
        
        refined = {
            'metal': processed * asteroid.composition.get('metal', 0.15),
            'water': processed * asteroid.composition.get('water', 0.10),
            'silicates': processed * asteroid.composition.get('silicates', 0.70)
        }
        
        # Tailings split
        self.tailings['silicates'] += refined['silicates'] * 0.3  # Some usable
        self.tailings['other'] += processed - sum(refined.values())
        
        # Fabrication (salvage + refined metal + silicate bonus)
        usable = refined['metal'] + (self.salvage_pool_kg * self.params['salvage_eff'])
        fab_cap = mass_map.get('fab', 0) * self.params['fab_rate']
        fab_yield = self.params['base_fab_yield'] * (1.15 if self.params.get('micro_g_slurry', True) else 1.0)
        fabricated = min(fab_cap, usable) * fab_yield
        
        # Dust & attrition
        dust_add = mined_raw * self.params['dust_factor'].get(collection_method, 1.0)
        self.dust_inventory += dust_add
        failure_rate = self.params['base_failure'] * (1 + 0.3 * self.dust_inventory)
        failed = self.total_mass * min(failure_rate, 0.25)
        
        self.salvage_pool_kg += failed * self.params['salvage_recovery']
        self.total_mass = (self.total_mass - failed) + fabricated
        
        return {
            'fabricated': fabricated,
            'anchoring_throttle': throttle,
            'power_margin': available_power / (total_power + 1e-6),
            'dust': self.dust_inventory
        }
