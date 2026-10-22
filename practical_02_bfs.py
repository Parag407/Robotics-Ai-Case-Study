# Practical 2: Breadth First Search (BFS) Algorithm
# Domain Specific: Software Development - Dependency Resolution

import collections

def bfs_module_dependencies(graph, start_module):
    visited = set([start_module])
    queue = collections.deque([(start_module, 0)])
    level_order = []
    
    while queue:
        module, level = queue.popleft()
        level_order.append((module, level))
        for neighbor in graph.get(module, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
    return level_order

code_modules = {
    'AppMain': ['AuthService', 'PaymentGateway', 'UIEngine'],
    'AuthService': ['DatabaseDriver', 'OAuthProvider'],
    'PaymentGateway': ['DatabaseDriver', 'StripeAPI'],
    'UIEngine': ['RenderPipeline']
}

print("=== PRACTICAL 2: BFS SOFTWARE DEPENDENCY RESOLUTION ===")
for mod, lvl in bfs_module_dependencies(code_modules, 'AppMain'):
    print(f"  Level {lvl}: {mod}")
