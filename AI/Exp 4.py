from itertools import permutations

# Letters in the puzzle
letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

# Try all possible digit assignments
for perm in permutations(range(10), len(letters)):
    S, E, N, D, M, O, R, Y = perm

    # Leading letters cannot be zero
    if S == 0 or M == 0:
        continue

    # Form the numbers
    SEND = 1000 * S + 100 * E + 10 * N + D
    MORE = 1000 * M + 100 * O + 10 * R + E
    MONEY = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

    # Check the equation
    if SEND + MORE == MONEY:
        print("Solution Found!")
        print("SEND  =", SEND)
        print("MORE  =", MORE)
        print("MONEY =", MONEY)
        break
