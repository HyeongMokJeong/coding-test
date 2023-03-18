import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ary = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 0은 파괴 가능한 루트, 1은 파괴 불가능한 루트
visited[0][0][0] = 1
q = deque([(0, 0, 0)])

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    b, x, y = q.popleft()
    if x == n - 1 and y == m - 1: 
        print(visited[x][y][b])
        break

    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if ary[nx][ny] == 1 and not b: # 벽이고 파괴 가능하면
                visited[nx][ny][1] = visited[x][y][0] + 1 # 파괴 불가능한 루트로 이동해서 횟수 추가 
                q.append((1, nx, ny))
            elif ary[nx][ny] == 0 and visited[nx][ny][b] == 0: # 길이고 본인 루트에서 아직 방문하지 않았다면
                visited[nx][ny][b] = visited[x][y][b] + 1
                q.append((b, nx, ny))
else: print(-1)