goal = [['1','2','3'],
        ['4','5','6'],
        ['7','8','0']]

print("Enter the initial state:")
puzzle = []

for i in range(3):
    puzzle.append(input().split())

# Check if already solved
if puzzle == goal:
    print("Puzzle is already solved.")
else:
    # Find blank space
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] == '0':
                x, y = i, j

    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    solved = False

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            temp = [row[:] for row in puzzle]
            temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]

            if temp == goal:
                solved = True
                break

    if solved:
        print("Puzzle can be solved in one move.")
    else:
        print("Puzzle is not solved in one move.")
