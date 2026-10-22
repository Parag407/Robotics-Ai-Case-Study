# Practical 5: Travelling Salesman Problem (TSP) using A* Search
# Informed Search Strategy

import heapq

def solve_tsp_a_star(dist):
    n = len(dist)
    pq = [(0, 0, 0, 1, [0])]
    
    while pq:
        f, g, u, mask, path = heapq.heappop(pq)
        
        if mask == (1 << n) - 1:
            return path + [0], g + dist[u][0]
            
        for v in range(n):
            if not (mask & (1 << v)):
                next_mask = mask | (1 << v)
                next_g = g + dist[u][v]
                h = min([dist[v][k] for k in range(n) if not (next_mask & (1 << k))] or [dist[v][0]])
                f_score = next_g + h
                heapq.heappush(pq, (f_score, next_g, v, next_mask, path + [v]))

cities = ["Campus Alpha", "Hub Beta", "Lab Gamma", "Tech Center Delta", "Main Office"]
matrix = [
    [0, 20, 30, 10, 15],
    [20, 0, 15, 25, 35],
    [30, 15, 0, 30, 20],
    [10, 25, 30, 0, 12],
    [15, 35, 20, 12, 0]
]

print("=== PRACTICAL 5: TRAVELLING SALESMAN PROBLEM (A* SEARCH) ===")
path, cost = solve_tsp_a_star(matrix)
print("Optimal TSP Route:")
print(" -> ".join([cities[i] for i in path]))
print(f"Total Optimal Cost / Distance: {cost} units")
