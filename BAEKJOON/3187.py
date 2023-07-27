import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

R, C = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

def dfs(x, y):
    global wolf, sheep
    if ary[x][y] == 'v': wolf += 1
    elif ary[x][y] == 'k': sheep += 1
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and ary[nx][ny] != '#':
            visited[nx][ny] = 1
            dfs(nx, ny)

r_wolf, r_sheep = 0, 0
for i in range(R):
    for j in range(C):
        if visited[i][j] or ary[i][j] == '#': continue
        wolf, sheep = 0, 0
        visited[i][j] = 1
        dfs(i, j)
        if wolf < sheep: r_sheep += sheep
        else: r_wolf += wolf
print(r_sheep, r_wolf)