import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ary = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(ary[x][y])
        break

    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == 1:
            ary[nx][ny] = ary[x][y] + 1
            q.append((nx, ny))