import numpy as np

class Asteroid:
    def __init__(self, name, water=0.10, metal=0.15, silicates=0.75, cohesion_kpa=15.0):
        self.name = name
        self.composition = {'water': water, 'metal': metal, 'silicates': silicates}
        self.cohesion_kpa = cohesion_kpa  # Hardness of the asteroid surface

class ZeroGSubsystemSwarm:
    def __init__(self, initial_mass_kg, fractions, params):
        self.total_mass = initial_mass_kg
        self.fractions = fractions  # Allocation map (must sum to 1.0)
        self.params = params
        
        self.salvage_pool_kg = 0.0
        self.tailings_discarded_kg = 0.0
        self.failures_recorded = 0
        
    @property
    def masses(self):
        """Mass breakdown of the current swarm's subsystems."""
        return {k: self.total_mass * v for k, v in self.fractions.items()}

    def calculate_wear_and_attrition(self, collection_method):
        """Calculates attrition penalty based on dust exposure of the collection method."""
        dust_multiplier = 1.0
        if collection_method == "touch_and_go":
            dust_multiplier = 2.2
        elif collection_method == "mechanical_open":
            dust_multiplier = 1.8
        elif collection_method == "enclosed_bag":
            dust_multiplier = 1.1
            
        return self.params['base_failure_rate_per_cycle'] * dust_multiplier

    def simulate_cycle(self, asteroid, au_distance, collection_method="enclosed_bag"):
        mass_map = self.masses
        
        # 1. Power generation & refinery spin tax
        solar_scale = 1.0 / (au_distance ** 2)
        total_solar_power = mass_map['power'] * self.params['panel_specific_power_kW_per_kg'] * solar_scale
        
        # Power consumed to maintain centrifugal separation (artificial gravity)
        centrifugal_refining_power = mass_map['refine'] * self.params['spin_power_tax_kW_per_kg']
        available_process_power = max(0.0, total_solar_power - centrifugal_refining_power)
        
        # 2. Mining throughput (Throttled by anchoring force vs surface cohesion)
        # Max force tool can exert is limited by the anchor's grip
        tool_force_limit_n = mass_map['mine'] * self.params['anchoring_force_newtons_per_kg']
        cohesion_force_n = asteroid.cohesion_kpa * self.params['tool_area_m2'] * 1000.0
        
        anchoring_throttle = 1.0
        if cohesion_force_n > tool_force_limit_n:
            # Anchor slip occurs; tool speed must reduce to prevent losing grip
            anchoring_throttle = tool_force_limit_n / cohesion_force_n
            
        nominal_dig_limit = mass_map['mine'] * self.params['dig_rate_kg_per_kg_cycle']
        actual_mined_raw = nominal_dig_limit * anchoring_throttle
        
        # 3. Refining pipeline (Capped by process power, sizing, and compositions)
        refining_capacity_raw = mass_map['refine'] * self.params['refining_throughput_kg_per_kg_cycle']
        power_refining_limit_raw = available_process_power * self.params['kg_refined_per_kWh']
        
        processed_raw = min(actual_mined_raw, refining_capacity_raw, power_refining_limit_raw)
        
        # Yields based on composition
        refined_metal = processed_raw * asteroid.composition['metal']
        refined_water = processed_raw * asteroid.composition['water']
        
        # Tailings tracking
        cycle_tailings = actual_mined_raw - (refined_metal + refined_water)
        self.tailings_discarded_kg += cycle_tailings
        
        # 4. Fabrication pipeline (Uses processed metal + salvage pool)
        # Salvage feedstock bypasses refining completely, cutting processing power requirements
        usable_salvage = self.salvage_pool_kg * self.params['salvage_efficiency']
        self.salvage_pool_kg -= usable_salvage # Consume the recycled components
        
        total_feedstock = refined_metal + usable_salvage
        fab_capacity = mass_map['fab'] * self.params['fab_throughput_kg_per_kg_cycle']
        
        # Microgravity printing advantage: zero sedimentation in slurries increases print yield
        adjusted_fab_yield = self.params['base_fab_yield']
        if self.params.get('microgravity_slurry_optimization', False):
            adjusted_fab_yield *= 1.15  # 15% efficiency boost based on 2026 CosmicMaker flights
            
        fabricated_mass = min(fab_capacity, total_feedstock) * adjusted_fab_yield
        
        # 5. Dynamic Attrition & Closed Salvage Loop
        cycle_failure_rate = self.calculate_wear_and_attrition(collection_method)
        failed_mass = self.total_mass * cycle_failure_rate
        self.failures_recorded += int(failed_mass // self.params['min_replication_mass_kg'])
        
        # Reallocate survived + newly printed mass back to swarm
        self.total_mass = (self.total_mass - failed_mass) + fabricated_mass
        
        # Dead units go to the salvage pool to be melted down next cycle
        self.salvage_pool_kg += failed_mass * self.params['salvage_recovery_fraction']
        
        return {
            'final_mass': self.total_mass,
            'fabricated_mass': fabricated_mass,
            'failed_mass': failed_mass,
            'tailings': cycle_tailings,
            'anchoring_throttle': anchoring_throttle,
            'power_margin': available_process_power / (total_solar_power + 1e-6)
        }
