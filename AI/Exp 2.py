def is_safe(board, row, col, n):
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower-left diagonal
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col, n):
    # If all queens are placed
    if col == n:
        return True

    # Try placing the queen in each row
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, col + 1, n):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Main Program
n = int(input("Enter the number of queens: "))

board = [[0] * n for _ in range(n)]

if solve(board, 0, n):
    print("\nSolution:")
    for row in board:
        print(row)
else:
    print("No solution exists.")
