
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

def solve():
    return "Hello, Sudoku-Solver!"


if __name__ == "__main__":
    problem = f"800134902041096080005070010008605000406310009023040860500709000010080040000401006"
    solution = f"867134952241596783395872614978625431456318279123947865534769128619283547782451396"
    board = make_board(problem)
    print("Problem:")
    print_sudoku(board)
    print(solve())
