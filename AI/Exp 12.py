board = [' ' for i in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],   # Rows
        [0,3,6], [1,4,7], [2,5,8],   # Columns
        [0,4,8], [2,4,6]             # Diagonals
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

player = 'X'

for turn in range(9):
    print_board()

    move = int(input("Player " + player + ", Enter position (1-9): "))

    if move < 1 or move > 9:
        print("Invalid position! Enter a number between 1 and 9.")
        continue

    if board[move - 1] == ' ':
        board[move - 1] = player
    else:
        print("Position already occupied!")
        continue

    if check_win(player):
        print_board()
        print("Player", player, "Wins!")
        break

    if player == 'X':
        player = 'O'
    else:
        player = 'X'
else:
    print_board()
    print("Game Draw!")
