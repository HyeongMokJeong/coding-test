import sys; input = sys.stdin.readline

def row(x, n):
    for i in range(9):
        if n == ary[x][i]: return False
    return True

def col(y, n):
    for i in range(9):
        if n == ary[i][y]: return False
    return True

def rect(x, y, n):
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(3):
        for j in range(3):
            if n == ary[nx + i][ny + j]: return False
    return True

def run(n):
    if n == len(blank):
        for i in ary:
            print(*i)
        exit()
    
    x, y = blank[n][0], blank[n][1]
    for i in range(1, 10):
        if row(x, i) and col(y, i) and rect(x, y, i):
            ary[x][y] = i
            run(n + 1)
            ary[x][y] = 0

ary = []
blank = []
for i in range(9):
    ary.append(list(map(int, input().split())))
    for j in range(9):
        if not ary[i][j]: blank.append((i, j))
run(0)