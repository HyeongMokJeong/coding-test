import sys; input=sys.stdin.readline
sys.setrecursionlimit(10**9)

N, M, K = map(int, input().split())

trash, stage = [], [[0] * (M + 1) for _ in range(N + 1)]
for _ in range(K):
    r, c = map(int, input().split())
    trash.append((r, c))
    stage[r][c] = 1

result, temp = 0, 1
def dfs(x, y):
    global temp
    if not stage[x][y]: return

    stage[x][y] = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx <= N and 0 <= ny <= M and stage[nx][ny]:
            temp += 1
            dfs(nx, ny)

for x, y in trash:
    dfs(x, y)
    result = max(result, temp)
    temp = 1
print(result)