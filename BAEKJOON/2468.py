import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
ary = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

c = 0
result = list()

def dfs(x, y, w, visited):
    if (x < 0 or x >= n or y < 0 or y >= n): return

    if (ary[x][y] > w and visited[x][y] == 0):
        visited[x][y] = 1
        for i in range(4):
            dfs(x + dx[i], y + dy[i], w, visited)
        return

start = 0
while start < max(sum(ary, [])):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if ary[i][j] > start and visited[i][j] == 0:
                c += 1
                for d in range(4):
                    dfs(i + dx[d], j + dy[d], start, visited)
    result.append(c)
    c = 0
    start += 1

print(max(result))