import sys; input = sys.stdin.readline

n = int(input().rstrip())
ary = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')

for i in range(3):
    dp = [[float('inf'), float('inf'), float('inf')] for _ in range(n)]
    dp[0][i] = ary[0][i]

    for j in range(1, n):
        dp[j][0] = ary[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = ary[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = ary[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for h in range(3):
        if h != i:
            result = min(result, dp[-1][h])
print(result)