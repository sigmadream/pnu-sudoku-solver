
import platform
import os

CLS = "cls" if platform.system() == "Windows" else "clear"

def make_board(problem):
    sudoku = []
    row = []
    for i in range(len(problem)):
        row.append(int(problem[i]))
        if (i+1) % 9 == 0:
            sudoku.append(row)
            row = []
    return sudoku
    
def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------+-------+-------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")


def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3
    for i in range(boardx_y*3, boardx_y*3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True

def solve(board):
    find = is_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            os.system(CLS)
            print(f"\nSolution {row, col}: \n")
            print_sudoku(board)
            if solve(board):
                return True
            board[row][col] = 0
    return False


if __name__ == "__main__":
    problem = f"800134902041096080005070010008605000406310009023040860500709000010080040000401006"
    solution = f"867134952241596783395872614978625431456318279123947865534769128619283547782451396"
    board = make_board(problem)
    print("Problem:")
    print_sudoku(board)
    solve(board)
