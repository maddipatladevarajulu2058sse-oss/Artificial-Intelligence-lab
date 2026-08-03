# Water Jug Problem

from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        print((x, y))

        if x == target or y == target:
            print("Target reached!")
            return

        queue.extend([
            (jug1, y),                         # Fill Jug 1
            (x, jug2),                         # Fill Jug 2
            (0, y),                            # Empty Jug 1
            (x, 0),                            # Empty Jug 2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug 1 -> Jug 2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug 2 -> Jug 1
        ])
