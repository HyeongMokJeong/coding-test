import sys; input = sys.stdin.readline

n = int(input().rstrip())
ary = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n - i):
        if i == 1:
            dp[j][j + i] = ary[j][0] * ary[j][1] * ary[j + i][1]
            continue
        dp[j][j + i] = 2 ** 32
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i], dp[j][k] + dp[k + 1][j + i] + ary[j][0] * ary[k][1] * ary[j + i][1])
print(dp[0][-1])