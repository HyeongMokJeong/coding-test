import sys; input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
ary, visited_j, visited_f = [], [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]
q_j, fire = deque(), deque()
for i in range(R):
    maze = list(input().rstrip())
    for j in range(C):
        if maze[j] == 'J': 
            q_j.append((i, j))
            visited_j[i][j] = 1
        elif maze[j] == 'F': 
            fire.append((i, j))
            visited_f[i][j] = 1
    ary.append(maze)

while fire:
    x, y = fire.popleft()
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < R and 0 <= ny < C and not visited_f[nx][ny] and ary[nx][ny] != '#':
            visited_f[nx][ny] = visited_f[x][y] + 1
            fire.append((nx, ny))

while q_j:
    x, y = q_j.popleft()

    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < R and 0 <= ny < C:
            if ary[nx][ny] != '#' and not visited_j[nx][ny]:
                if not visited_f[nx][ny] or visited_f[nx][ny] > visited_j[x][y] + 1:
                    visited_j[nx][ny] = visited_j[x][y] + 1
                    q_j.append((nx, ny))
        else:
            print(visited_j[x][y])
            exit()
print("IMPOSSIBLE")