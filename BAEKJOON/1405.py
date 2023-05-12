N, A, B, C, D = map(int, input().split())
percent = [A, B, C, D]
visited = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]

result = 0
def dfs(x, y, per, count):
    global result
    if count == N:
        result += per
        return
    
    visited[x][y] = 1
    for idx, nxy in enumerate(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))):
        nx, ny = nxy[0], nxy[1]
        if 0 <= nx < N * 2 + 1 and 0 <= ny < N * 2 + 1:
            if visited[nx][ny]: continue
            dfs(nx, ny, per * (percent[idx] / 100),count + 1)
            visited[nx][ny] = 0

dfs(N, N, 1, 0)
print(result)