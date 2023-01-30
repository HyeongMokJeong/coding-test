import sys

result = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def daik(ary, visited):
    q = [(0, 0, ary[0][0])]

    while q:
        x, y, t = q.pop(0)
        if visited[x][y] < t: continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(ary) and 0 <= ny < len(ary):
                if t + ary[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = t + ary[nx][ny]
                    q.append((nx, ny, visited[nx][ny]))
    return visited[-1][-1]


while True:
    n = int(input())
    if n == 0: break
    ary = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited = [([9999] * n) for _ in range(n)]
    answer = daik(ary, visited)
    result.append(answer)
    
for idx, i in enumerate(result): print(f"Problem {idx + 1}: {i}")