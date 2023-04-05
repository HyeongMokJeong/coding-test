import sys

n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = 0

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(x, y, count, num):
    global result

    if num == 4:
        if count > result: result = count
        return
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, count + paper[nx][ny], num + 1)
            visited[nx][ny] = 0

def search(x, y):
    global result
    for i in range(4):
        temp = paper[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx = x + move[t][0]
            ny = y + move[t][1]

            if not (0 <= nx < n and 0 <= ny < m):
                temp = 0
                break
            temp += paper[nx][ny]
        if temp > result: result = temp

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, paper[i][j], 1)
        search(i, j)
        visited[i][j] = 0
print(result)