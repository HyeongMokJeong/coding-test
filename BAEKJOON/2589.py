import sys; input = sys.stdin.readline
from collections import deque

L, W = map(int, input().split())
ary, temp = [], []
for i in range(L):
    ary.append(list(input().rstrip()))
    for j in range(W):
        if ary[i][j] == 'L': temp.append((i, j))

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[0] * W for _ in range(L)]
    visited[i][j] = 1

    count = 0
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < L and 0 <= ny < W and not visited[nx][ny] and ary[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                count = max(count, visited[nx][ny])
    return count - 1

result = 0  
for x, y in temp: result = max(result, bfs(x, y))
print(result)