import sys; input = sys.stdin.readline

n, m = map(int, input().split())
ary = [list(map(int, list(input().rstrip()))) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0: dp[i][j] = ary[i][j]
        elif ary[i][j] == 1: dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        if dp[i][j] > result: result = dp[i][j]
print(result ** 2)