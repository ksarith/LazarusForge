def optimize_mass_allocation(solver, current_mass: float, asteroid: Asteroid, cycle: int, 
                             look_ahead=3, discount=0.85) -> Dict[str, float]:
    """Marginal utility with optional look-ahead."""
    gradients = {}
    original = {name: sub.mass_fraction for name, sub in solver.subsystems.items()}
    
    for target in solver.subsystems.keys():
        total_delta = 0.0
        for horizon in range(look_ahead):
            # Perturb and simulate future cycle
            # ... (perturbation logic as before)
            future_growth = ...  # projected net_growth at cycle + horizon
            total_delta += (future_growth * (discount ** horizon))
        
        gradients[target] = total_delta / 0.01  # normalized marginal
    
    # Restore fractions
    for name, frac in original.items():
        solver.subsystems[name].mass_fraction = frac
    return gradients
