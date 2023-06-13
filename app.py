import sudoku_solver as ss

if __name__ == "__main__":
    p = "405001068073628500009003070240790030006102005950000021507064213080217050612300007"
    b = ss.make_board(p)
    ss.print_sudoku(b)
    ss.solve(b)