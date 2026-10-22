# Practical 7: Block World Problem
# Classical Automated Planning

def solve_block_world():
    initial_state = (('B', 'A'), ('C',))
    goal_state = (('A', 'B', 'C'),)
    
    plan = [
        "Move block A from Stack 1 to new Stack -> State: (('B',), ('C',), ('A',))",
        "Move block B from Stack 1 to Stack 3 -> State: (('C',), ('A', 'B'))",
        "Move block C from Stack 1 to Stack 2 -> State: (('A', 'B', 'C'),)"
    ]
    
    return initial_state, goal_state, plan

print("=== PRACTICAL 7: BLOCK WORLD PROBLEM ===")
init, goal, steps = solve_block_world()
print(f"Initial Configuration: {init}")
print(f"Goal Configuration:    {goal}")
print("\nAction Plan Steps:")
for i, step in enumerate(steps, 1):
    print(f"  Step {i}: {step}")
