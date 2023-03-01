import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
tomato = [list(list(map(int, sys.stdin.readline().split())) for _ in range(n)) for _ in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
q = deque()
for x, i in enumerate(tomato):
    for y, j in enumerate(i):
        for z, l in enumerate(j):
            if l == 1: q.append((x, y, z))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and tomato[nx][ny][nz] == 0:
            tomato[nx][ny][nz] = tomato[x][y][z] + 1
            q.append((nx, ny, nz))

result = 0
for i in tomato:
    for j in i:
        for l in j:
            if l == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))
print(result - 1)