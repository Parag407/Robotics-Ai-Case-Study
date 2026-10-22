# Practical 3: Water Jug Problem
# Uninformed Search State Space Problem

import collections

def solve_water_jug():
    queue = collections.deque([((0, 0), [])])
    visited = set([(0, 0)])
    
    while queue:
        (x, y), path = queue.popleft()
        curr = path + [(x, y)]
        
        if x == 2:
            return curr
        
        states = [
            (4, y),  # Fill 4-gal jug
            (x, 3),  # Fill 3-gal jug
            (0, y),  # Empty 4-gal jug
            (x, 0),  # Empty 3-gal jug
            (x - min(x, 3 - y), y + min(x, 3 - y)),  # Pour 4-gal into 3-gal
            (x + min(y, 4 - x), y - min(y, 4 - x))   # Pour 3-gal into 4-gal
        ]
        
        for st in states:
            if st not in visited:
                visited.add(st)
                queue.append((st, curr))

print("=== PRACTICAL 3: WATER JUG PROBLEM SOLUTION ===")
solution = solve_water_jug()
for step, (j1, j2) in enumerate(solution):
    print(f"  Step {step}: 4-Gal Jug = {j1} gal | 3-Gal Jug = {j2} gal")
