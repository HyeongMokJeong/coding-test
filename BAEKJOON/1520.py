import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

m, n = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

def run(x, y):
    if x == m - 1 and y == n - 1: return 1
    if dp[x][y] == -1:
        dp[x][y] = 0    
        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] < maps[x][y]:
                dp[x][y] += run(nx, ny)
    return dp[x][y]
print(run(0, 0))