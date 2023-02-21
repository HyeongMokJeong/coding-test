import sys
from collections import deque

n, m = map(int, input().split())
maze = [list(sys.stdin.readline()) for _ in range(n)]
q = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
key = {'a':1,'b':2,'c':4,'d':8,'e':16,'f':32}
door = {'A':1,'B':2,'C':4,'D':8,'E':16,'F':32}
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maze[i][j] == "0":
            q.append([i, j, 0, 0])
            visited[i][j] = 0
            maze[i][j] = "."

while q:
    x, y, keys, count = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if n > nx >= 0 and m > ny >= 0 and maze[nx][ny] != "#":
            if visited[nx][ny] != -1 and visited[nx][ny] | keys == visited[nx][ny]: continue
            visited[nx][ny] = keys
            if maze[nx][ny] == ".": q.append([nx, ny, keys, count + 1])
            if maze[nx][ny] == "1": 
                print(count + 1)
                exit(0)
            if maze[nx][ny] in key.keys(): q.append([nx, ny, keys | key[maze[nx][ny]], count + 1])
            if maze[nx][ny] in door.keys() and door[maze[nx][ny]] | keys == keys: q.append([nx, ny, keys, count + 1])
print(-1)