import sys
sys.setrecursionlimit(1000000)

t = int(input())
result = []

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(matrix, x, y):
    matrix[x][y] = 0
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == 1:
            dfs(matrix, nx, ny)

for _ in range(t):
    m, n, k = map(int, input().split())
    matrix = [[0] * m for _ in range(n)]
    count = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        matrix[y][x] = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                dfs(matrix, i, j)
                count += 1
    result.append(count)
for i in result: print(i)