import sys; input = sys.stdin.readline
from collections import deque

while True:
    L, R, C = map(int, input().split())
    if not L and not R and not C: break

    ary = []
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    q = deque()
    for z in range(L):
        temp = []
        for x in range(R):
            temp.append(list(input().rstrip()))
            for y in range(C):
                if temp[x][y] == 'S': 
                    q.append((z, x, y, 0))
                    visited[z][x][y] = 1
        ary.append(temp)
        input()
    
    while q:
        z, x, y, c = q.popleft()

        if ary[z][x][y] == 'E':
            print(f"Escaped in {c} minute(s).")
            break
        for nz, nx, ny in [(z + 1, x, y), (z - 1, x, y), (z, x + 1, y), (z, x - 1, y), (z, x, y + 1), (z, x, y - 1)]:
            if 0 <= nz < L and 0 <= nx < R and 0 <= ny < C and not visited[nz][nx][ny] and ary[nz][nx][ny] != '#':
                q.append((nz, nx, ny, c + 1))
                visited[nz][nx][ny] = 1
    else: print("Trapped!")
