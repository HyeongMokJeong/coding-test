import sys; input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
ary = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0

q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            if ary[nx][ny] == 0: 
                dist[nx][ny] = dist[x][y]
                q.appendleft((nx, ny))
            else: 
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
print(dist[N - 1][M - 1])