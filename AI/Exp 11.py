# Map Coloring using CSP (Backtracking)

# Graph representing adjacent regions
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Dictionary to store assigned colors
color_assignment = {}

# Function to check if a color assignment is valid
def is_safe(region, color):
    for neighbor in graph[region]:
        if neighbor in color_assignment and color_assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def solve(region_list, index):
    if index == len(region_list):
        return True

    region = region_list[index]

    for color in colors:
        if is_safe(region, color):
            color_assignment[region] = color

            if solve(region_list, index + 1):
                return True

            del color_assignment[region]

    return False

# Convert dictionary keys to a list
regions = list(graph.keys())

if solve(regions, 0):
    print("Color Assignment:")
    for region in regions:
        print(region, "->", color_assignment[region])
else:
    print("No solution exists.")
