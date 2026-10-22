# Practical 8: Min-Max Algorithm
# Adversarial Search / Game Playing

import math

def min_max(depth, node_idx, is_maximizing_player, scores, tree_height):
    if depth == tree_height:
        return scores[node_idx]
        
    if is_maximizing_player:
        return max(
            min_max(depth + 1, node_idx * 2, False, scores, tree_height),
            min_max(depth + 1, node_idx * 2 + 1, False, scores, tree_height)
        )
    else:
        return min(
            min_max(depth + 1, node_idx * 2, True, scores, tree_height),
            min_max(depth + 1, node_idx * 2 + 1, True, scores, tree_height)
        )

leaf_scores = [3, 5, 2, 9, 12, 5, 23, 23]
height = int(math.log2(len(leaf_scores)))

print("=== PRACTICAL 8: MIN-MAX ALGORITHM ===")
print(f"Game Tree Leaf Scores: {leaf_scores}")
optimal_value = min_max(0, 0, True, leaf_scores, height)
print(f"Optimal Decision Score for MAX Player: {optimal_value}")
