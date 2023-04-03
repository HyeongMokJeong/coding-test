import sys

n, m = map(int, sys.stdin.readline().split())
num = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0] * (n + 1)
for i in range(1, n + 1): dp[i] = dp[i - 1] + num[i]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(dp[j] - dp[i - 1])