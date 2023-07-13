import sys; input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
ary, q = [], deque([])
distance = [[0] * C for _ in range(R)]

for i in range(R):
    ary.append(list(input().rstrip()))
    for j in range(C):
        if ary[i][j] == 'D': d = (i, j)
        elif ary[i][j] == 'S': q.append((i, j))

for i in range(R):
    for j in range(C):
        if ary[i][j] == '*': q.append((i, j))

def bfs(x, y):
    while q:
        tx, ty = q.popleft()
        if ary[x][y] == 'S':
            return distance[x][y]
        for nx, ny in [(tx + 1, ty), (tx - 1, ty), (tx, ty + 1), (tx, ty - 1)]:
            if 0 <= nx < R and 0 <= ny < C:
                if (ary[nx][ny] == '.' or ary[nx][ny] == 'D') and ary[tx][ty] == 'S':
                    q.append((nx, ny))
                    distance[nx][ny] = distance[tx][ty] + 1
                    ary[nx][ny] = 'S'
                elif (ary[nx][ny] == '.' or ary[nx][ny] == 'S') and ary[tx][ty] == '*':
                    ary[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"
print(bfs(d[0], d[1]))