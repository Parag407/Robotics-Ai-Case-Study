# Practical 1: Depth First Search (DFS) Algorithm
# Domain Specific: Education - Learning Path Traversal

def dfs_learning_path(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    
    if start == goal:
        return path
        
    for next_course in graph.get(start, []):
        if next_course not in visited:
            result = dfs_learning_path(graph, next_course, goal, visited, path)
            if result:
                return result
    path.pop()
    return None

# Curriculum Prerequisite Graph
edu_curriculum = {
    'Intro to Python': ['Data Structures', 'Web Basics'],
    'Data Structures': ['Algorithms', 'Database Systems'],
    'Algorithms': ['Machine Learning', 'Artificial Intelligence'],
    'Machine Learning': ['Deep Learning'],
    'Artificial Intelligence': ['Robotics & AI Lab'],
    'Web Basics': ['Frontend Dev']
}

path = dfs_learning_path(edu_curriculum, 'Intro to Python', 'Robotics & AI Lab')

print("=== PRACTICAL 1: DFS LEARNING PATH ===")
if path:
    print("Course Prerequisite DFS Path:")
    print(" -> ".join(path))
else:
    print("No valid prerequisite path found.")
