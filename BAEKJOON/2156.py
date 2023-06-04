import sys; input = sys.stdin.readline
n = int(input().rstrip())
ary = [0] + [int(input().rstrip()) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = ary[1]
if n > 1: dp[2] = ary[1] + ary[2]
for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + ary[i], dp[i - 3] + ary[i - 1] + ary[i])
print(dp[n])