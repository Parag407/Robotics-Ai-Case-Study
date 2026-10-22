# Practical 9: Alpha-Beta Search Algorithm
# Optimized Adversarial Search

import math

def alpha_beta(depth, node_idx, is_max, scores, alpha, beta, height, stats):
    if depth == height:
        return scores[node_idx]
        
    if is_max:
        best = -float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_idx * 2 + i, False, scores, alpha, beta, height, stats)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                stats['pruned_count'] += 1
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta(depth + 1, node_idx * 2 + i, True, scores, alpha, beta, height, stats)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                stats['pruned_count'] += 1
                break
        return best

leaf_scores = [3, 5, 6, 9, 1, 2, 0, -1]
height = int(math.log2(len(leaf_scores)))
stats = {'pruned_count': 0}

print("=== PRACTICAL 9: ALPHA-BETA SEARCH ALGORITHM ===")
print(f"Game Tree Leaf Values: {leaf_scores}")
optimal_score = alpha_beta(0, 0, True, leaf_scores, -float('inf'), float('inf'), height, stats)
print(f"Optimal Score with Alpha-Beta Pruning: {optimal_score}")
print(f"Number of Pruned Branches: {stats['pruned_count']}")
