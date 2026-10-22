# Practical 6: Tower of Hanoi Problem
# Recursive Problem Solving

def solve_tower_of_hanoi(n, source, destination, auxiliary, moves):
    if n == 1:
        moves.append((1, source, destination))
        return
    solve_tower_of_hanoi(n - 1, source, auxiliary, destination, moves)
    moves.append((n, source, destination))
    solve_tower_of_hanoi(n - 1, auxiliary, destination, source, moves)

moves_list = []
solve_tower_of_hanoi(3, 'Peg A (Source)', 'Peg C (Destination)', 'Peg B (Auxiliary)', moves_list)

print("=== PRACTICAL 6: TOWER OF HANOI (3 DISKS) ===")
print(f"Total Moves Required: {len(moves_list)}")
for idx, (disk, src, tgt) in enumerate(moves_list, 1):
    print(f"  Step {idx}: Move disk {disk} from {src} to {tgt}")
