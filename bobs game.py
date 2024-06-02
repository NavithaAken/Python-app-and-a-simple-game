from collections import defaultdict

def get_ordering(N, constraints):
    adj_list = defaultdict(list)
    visited = {}
    for i in range(N):
        X, _, Y = constraints[i].split()
        adj_list[X].append(Y)
        adj_list[Y].append(X)
        visited[X] = False
        visited[Y] = False
    
    ordering = []
    start = min(adj_list.keys())
    stack = [start]
    
    while stack:
        node = stack.pop()
        if not visited[node]:
            ordering.append(node)
            visited[node] = True
            for neighbor in sorted(adj_list[node]):
                stack.append(neighbor)
    
    return ordering

# Sample Input
N = 3
constraints = [
    "Buttercup must be killed beside Bella",
    "Blue must be killed beside Bella",
    "Sue must be killed beside Beatrice"
]

# Get ordering
ordering = get_ordering(N, constraints)

# Output the ordering
for monster in ordering:
    print(monster)
