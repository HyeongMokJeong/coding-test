import sys
from collections import deque

board, visited = [0] * 101, [0] * 101
n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    board[x] = y
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    board[u] = v

q = deque([(1, 0)])

while q:
    t, count = q.popleft()
    if t == 100:
        print(count)
        break

    for i in range(6, 0, -1):
        nt = t + i
        if nt <= 100 and not visited[nt]:
            if board[nt] != 0:
                visited[board[nt]] = 1
                q.append((board[nt], count + 1))
            else:
                visited[nt] = 1
                q.append((nt, count + 1))
