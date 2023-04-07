import sys
input = sys.stdin.readline

n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
result = 0

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

for i in range(1, n):
    if ary[0][i]: break
    dp[0][0][i] = 1

for i in range(1, n):
    for j in range(1, n):
        if not ary[i][j] and not ary[i - 1][j] and not ary[i][j - 1]:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]
        
        if not ary[i][j]:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
print(sum(dp[i][n - 1][n - 1] for i in range(3)))