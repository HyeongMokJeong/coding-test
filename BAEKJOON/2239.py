import sys

sudoku = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if not sudoku[i][j]]

def bt(n):
    if n == len(zero):
        for i in sudoku: print(*i, sep="")
        exit(0)
    
    x, y = zero[n]
    can = [i for i in range(1, 10)]

    # 3x3
    s_x, s_y = x // 3 * 3, y // 3 * 3
    for i in range(s_x, s_x + 3):
        for j in range(s_y, s_y + 3):
            if sudoku[i][j] in can:
                can.remove(sudoku[i][j])
    
    # 가로 세로
    for i in range(9):
        if sudoku[i][y] in can:
            can.remove(sudoku[i][y])
        if sudoku[x][i] in can:
            can.remove(sudoku[x][i])
    
    for i in can:
        sudoku[x][y] = i
        bt(n + 1)
    sudoku[x][y] = 0
    
bt(0)