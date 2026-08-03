from collections import deque

# Check whether a state is valid
def is_valid(m_left, c_left, m_right, c_right):
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False

    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True


# BFS function
def missionaries_cannibals():
    start = (3, 3, 0)      # (Missionaries Left, Cannibals Left, Boat Side)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m_left, c_left, boat), path = queue.popleft()

        if (m_left, c_left, boat) in visited:
            continue

        visited.add((m_left, c_left, boat))
        path = path + [(m_left, c_left, boat)]

        if (m_left, c_left, boat) == goal:
            print("Solution Found!\n")
            for state in path:
                print(state)
            return

        # Possible boat moves
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

        for m, c in moves:
            if boat == 0:      # Left -> Right
                new_state = (m_left - m, c_left - c, 1)
            else:              # Right -> Left
                new_state = (m_left + m, c_left + c, 0)

            nm_left, nc_left, nb = new_state
            nm_right = 3 - nm_left
            nc_right = 3 - nc_left

            if is_valid(nm_left, nc_left, nm_right, nc_right):
                queue.append((new_state, path))

    print("No Solution Found!")


# Run the program
missionaries_cannibals()
