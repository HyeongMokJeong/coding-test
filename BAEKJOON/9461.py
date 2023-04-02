import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + ([0] * (n - 9))
    if n > 10:
        for i in range(11, n + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
    print(dp[n])