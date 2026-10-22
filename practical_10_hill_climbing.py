# Practical 10: Hill Climbing Algorithm
# Domain Specific: Model Hyperparameter Optimization

import math

def objective_function(x):
    return -(x - 3)**2 + 10 * math.cos(2 * math.pi * x) + 20

def hill_climbing(start_x, step_size=0.1, max_iterations=100):
    current_x = start_x
    current_score = objective_function(current_x)
    trajectory = [(current_x, current_score)]
    
    for _ in range(max_iterations):
        neighbors = [current_x + step_size, current_x - step_size]
        best_neighbor = max(neighbors, key=objective_function)
        best_neighbor_score = objective_function(best_neighbor)
        
        if best_neighbor_score > current_score:
            current_x = best_neighbor
            current_score = best_neighbor_score
            trajectory.append((current_x, current_score))
        else:
            break
            
    return current_x, current_score, trajectory

print("=== PRACTICAL 10: HILL CLIMBING HYPERPARAMETER TUNING ===")
start_val = 0.5
opt_x, opt_score, history = hill_climbing(start_val)

print(f"Starting Hyperparameter Value: x = {start_val:.2f} | Initial Score = {objective_function(start_val):.4f}")
print(f"Optimal Value Found:           x = {opt_x:.4f} | Optimal Score = {opt_score:.4f}")
print("\nOptimization Trajectory (First 5 Steps):")
for idx, (x_val, score) in enumerate(history[:5]):
    print(f"  Step {idx}: x = {x_val:.4f}, Score = {score:.4f}")
