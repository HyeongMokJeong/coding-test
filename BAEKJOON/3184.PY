import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

R, C = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
r_sheep, r_wolf = 0, 0

def dfs(x, y):
    global t_sheep, t_wolf
    if ary[x][y] == 'v': t_wolf += 1
    elif ary[x][y] == 'o': t_sheep += 1
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and ary[nx][ny] != '#':
            visited[nx][ny] = 1
            dfs(nx, ny) 

for i in range(R):
    for j in range(C):
        t_sheep, t_wolf = 0, 0
        if not visited[i][j] and ary[i][j] != '#':
            visited[i][j] = 1
            dfs(i, j)
        if t_sheep or t_wolf:
            if t_sheep > t_wolf: r_sheep += t_sheep
            else: r_wolf += t_wolf
print(r_sheep, r_wolf)