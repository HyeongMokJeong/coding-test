import sys
import queue

r, c = map(int, sys.stdin.readline().split())

ary = [list(input()) for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0

# def dfs(x, y, visited, cnt):
#     if (x < 0 or x >= r or y < 0 or y >= c): return
#     global count

#     if (ary[x][y] not in visited):
#         visited.append(ary[x][y])
#         count += 1
#         count = max(count, cnt)
#         for i in range(4):
#             dfs(x + dx[i], y + dy[i], visited, cnt + 1)
#         return

def bfs():
    global count
    q = set([(0, 0, ary[0][0])])

    while q:
        x, y, z = q.pop()
        count = max(count, len(z))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (r > nx >=0 and c > ny >= 0 and ary[nx][ny] not in z):
                q.add((nx, ny, z + ary[nx][ny]))
                print(q)


# dfs (0, 0, visited, 1)
bfs()
print(count)