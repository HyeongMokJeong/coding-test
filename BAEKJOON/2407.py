n, m = map(int, input().split())
dp = [i for i in range(n + 1)]

for i in range(2, n + 1): dp[i] *= dp[i - 1]
print(dp[n] // (dp[n - m] * dp[m]))