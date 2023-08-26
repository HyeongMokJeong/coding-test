import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != 'F': flag = visited[x][y]
        else: flag = "F"

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < h and 0 <= ny < w:
                if not visited[nx][ny] and ary[nx][ny] == ".":
                    if flag == "F": visited[nx][ny] = "F"
                    else: visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "F": return flag
    return "IMPOSSIBLE"

for _ in range(int(input())):
    w, h = map(int, input().split())
    q = deque()
    ary = []
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        ary.append(list(input().rstrip()))
        for j in range(w):
            if ary[i][j] == "@": 
                visited[i][j] = 1
                start = (i, j)
            elif ary[i][j] == "*": 
                visited[i][j] = "F"
                q.append((i, j))
    q.append(start)
    print(bfs())