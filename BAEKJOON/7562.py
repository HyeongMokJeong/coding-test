import sys; input = sys.stdin.readline
from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]
for _ in range(int(input())):
    l = int(input())
    a, b = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    visited[a][b] = 1

    q = deque([(a, b, 0)])
    while q:
        x, y, c= q.popleft()
        if x == goal_x and y == goal_y:
            print(c)
            break

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append((nx, ny, c + 1))
                visited[nx][ny] = 1