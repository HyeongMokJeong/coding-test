import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(N)]
ice = []
for i in range(N):
    for j in range(M):
        if ary[i][j]: ice.append((i, j))

def dfs(x, y):
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and ary[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny)

def melt(x, y):
    count = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < N and 0 <= ny < M and not ary[nx][ny] and not visited[nx][ny]: count += 1
    ary[x][y] = max(ary[x][y] - count, 0)

result = 0
while ice:
    visited = [[0] * M for _ in range(N)]
    remove = []
    result += 1
    for x, y in ice:
        visited[x][y] = 1
        melt(x, y)
        if ary[x][y] == 0: remove.append((x, y))
    ice = sorted(list(set(ice) - set(remove)))

    visited = [[0] * M for _ in range(N)]
    count = 0
    for i, j in ice:
        if not visited[i][j]:
            visited[i][j] = 1
            count += 1
            dfs(i, j)
    if count >= 2:
        print(result)
        break
else: print(0)