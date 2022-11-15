count = 0
c = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
ary = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n: return
    global c

    if (ary[x][y] == 1):
        c += 1
        ary[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return

result = list()
for i in range(n):
    for j in range(n):
        if (ary[i][j] == 1):
            dfs(i, j)
            count += 1
            result.append(c)
            c = 0

result.sort()
print(count)
for i in result: print(i)