import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

count, result = 0, 0

def dfs(x, y):
    global temp
    ary[x][y] = 0
    temp += 1
    for nx, ny in [(x + 1, y), (x, y  + 1), (x - 1, y), (x, y - 1)]:
        if 0 <= nx < n and 0 <= ny < m and ary[nx][ny]:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if ary[i][j] == 0: continue
        temp = 0
        count += 1
        dfs(i, j)
        if result < temp: result = temp
print(count)
print(result)