import sys, copy
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]
empty, virus = [], []
for i in range(n):
    for j in range(m):
        if ary[i][j] == 0: empty.append((i, j))
        elif ary[i][j] == 2: virus.append((i, j))
result = 0

def dfs(board, x, y):
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
            board[nx][ny] = 2
            dfs(board, nx, ny)

for combi in combinations(empty, 3):
    board = copy.deepcopy(ary)
    for x, y in combi: board[x][y] = 1
    for v_x, v_y in virus: dfs(board, v_x, v_y)
    temp = 0
    for i in board: temp += i.count(0)
    result = max(result, temp)
print(result)