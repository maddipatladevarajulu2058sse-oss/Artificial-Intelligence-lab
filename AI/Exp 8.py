# Function to perform Depth First Search (DFS)
def dfs(graph, node, visited):
    if node not in visited:
        print node,
        visited.add(node)

        # Visit all adjacent nodes
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Set to store visited nodes
visited = set()

print "DFS Traversal:"
dfs(graph, 'A', visited)
