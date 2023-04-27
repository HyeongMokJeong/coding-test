import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

b, w = 0, 0

def bfs(x, y):
    global b, w
    count = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and ary[nx][ny] == ary[x][y]:
                visited[nx][ny] = 1
                q.append((nx, ny))
                count += 1
    if ary[x][y] == 'B': b += count ** 2
    else: w += count ** 2

for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            bfs(i, j)
print(w, b)