import sys
from collections import deque

n = int(input())
ary = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

size, eat = 2, 0
x, y = 0, 0

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(n):
        if ary[i][j] == 9: x, y = i, j

def bfs(a, b):
    visited = [[0] * n for _ in range(n)]
    q = deque([(a, b)])
    can = []

    visited[a][b] = 1

    while q:
        ox, oy = q.popleft()

        for i in range(4):
            nx, ny = ox + move[i][0], oy + move[i][1]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if ary[a][b] > ary[nx][ny] and ary[nx][ny] != 0: # ary[a][b]인 상어크기보다 작고, 0이 아니라면
                    visited[nx][ny] = visited[ox][oy] + 1 # 방문처리(이전 거리보다 1 더해서)
                    can.append((visited[nx][ny] - 1, nx, ny)) # 먹을 수 있으므로 can에 추가
                elif ary[a][b] == ary[nx][ny] or ary[nx][ny] == 0: # 무게가 똑같거나 / 빈칸이여서 그냥 가면 된다면
                    visited[nx][ny] = visited[ox][oy] + 1 # 방문처리만
                    q.append((nx, ny))

    return sorted(can, key=lambda x:(x[0], x[1], x[2])) # 방문 우선순위인 가장 가깝고 - 가장 위고 - 가장 왼쪽인 순으로 정렬해서 리턴

result = 0
while 1:
    ary[x][y] = size
    can = deque(bfs(x, y))

    if not can: break

    weight, nx, ny = can.popleft()
    result += weight
    eat += 1

    if size == eat:
        size += 1
        eat = 0
    
    ary[x][y] = 0
    x, y = nx, ny
print(result)