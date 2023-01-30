from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

for idx in range(n):
    for idy in range(m):
        if box[idx][idy] == 1: q.append([idx, idy])

while (q):
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and box[nx][ny] == 0: 
            box[nx][ny] = box[x][y] + 1
            q.append([nx, ny])

m = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        m = max(m, j)
print(m - 1)