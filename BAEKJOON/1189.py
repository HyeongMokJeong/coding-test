import sys

r, c, k = map(int, input().split())
matrix = [list(sys.stdin.readline()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)]
visited[r - 1][0] = 0
result = 0

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y, count):
    global result
    if x == 0 and y == c - 1:
        if count == k - 1: result += 1
        return
    
    for dx, dy in move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] != "T" and visited[nx][ny] == -1:
            visited[nx][ny] = 0
            dfs(nx, ny, count + 1)
            visited[nx][ny] = -1

dfs(r - 1, 0, 0)
print(result)