# Code is taken from https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
# Backtracking algorithm is implemented.

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


def convert(string):
    arr = []
    for i in range(9):
        arr.append(int(string[i]))
    return arr


total = 0
count = 0
with open("Problem 96 - Su Doku.txt") as f:
    i = 0
    f.readline()
    puzzle = []
    for line in f:
        i += 1
        puzzle.append(convert(str(line)))
        if (i == 9):
            count += 1
            print(count)
            for line in puzzle:
                print(line)
            print("solved")
            solve(puzzle)
            for line in puzzle:
                print(line)
            print()
            total += puzzle[0][0] * 100 + puzzle[0][1] * 10 + puzzle[0][2]
            f.readline()
            i = 0
            puzzle = []

print(total)

# Answer: 24702