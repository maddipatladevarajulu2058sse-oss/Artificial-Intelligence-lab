# A* Search Algorithm
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 4)],
    'F': [('G', 2)],
    'G': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}

def astar(start, goal):
    open_list = set([start])
    closed_list = set()

    g = {}
    g[start] = 0

    parents = {}
    parents[start] = start

    while len(open_list) > 0:
        n = None

        # Find node with lowest f = g + h
        for v in open_list:
            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == goal:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)
            path.reverse()

            print "Shortest Path:", path
            print "Total Cost:", g[goal]
            return

        for (m, weight) in graph[n]:
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            elif g[m] > g[n] + weight:
                g[m] = g[n] + weight
                parents[m] = n

                if m in closed_list:
                    closed_list.remove(m)
                    open_list.add(m)

        open_list.remove(n)
        closed_list.add(n)
    print "Path does not exist."

# Driver Code
astar('A', 'G')
