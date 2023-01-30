n = int(input())
ary = [list(map(int, input())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
count = 0
c = 0

def dfs(x, y):
    global c
    if x < 0 or x >= n or y < 0 or y >= n: return
    if ary[x][y] == 1:
        c += 1
        ary[x][y] = 0
        for i in range(4): dfs(x + dx[i], y + dy[i])

for i in range(n):
    for j in range(n):
        if ary[i][j] == 1:
            dfs(i, j)
            result.append(c)
            c = 0
            count += 1

print(count)
for i in sorted(result): print(i)

