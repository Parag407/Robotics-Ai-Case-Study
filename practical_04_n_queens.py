# Practical 4: N-Queens Problem Simulation
# Constraint Satisfaction & Backtracking

def solve_nqueens(n=8):
    board = [-1] * n
    sols = []
    
    def is_safe(r, c):
        for prev_r in range(r):
            if board[prev_r] == c or abs(board[prev_r] - c) == abs(prev_r - r):
                return False
        return True
        
    def backtrack(r):
        if r == n:
            sols.append(list(board))
            return
        for c in range(n):
            if is_safe(r, c):
                board[r] = c
                backtrack(r + 1)
                board[r] = -1

    backtrack(0)
    return sols

print("=== PRACTICAL 4: N-QUEENS SIMULATION ===")
solutions = solve_nqueens(8)
print(f"Total solutions found for 8-Queens Problem: {len(solutions)}")
print("\nFirst Solution Visualization (Q = Queen, . = Empty):")
first_sol = solutions[0]
for r in range(8):
    row_str = " ".join(["Q" if first_sol[r] == c else "." for c in range(8)])
    print(f"  {row_str}")
