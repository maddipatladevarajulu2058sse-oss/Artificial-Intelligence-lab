def minimax(depth, isMax):
    if depth == 3:
        return 0

    if isMax:
        best = -1000
        for i in range(2):
            value = minimax(depth + 1, False)
            if value > best:
                best = value
        return best
    else:
        best = 1000
        for i in range(2):
            value = minimax(depth + 1, True)
            if value < best:
                best = value
        return best

print("Best Score:", minimax(0, True))
