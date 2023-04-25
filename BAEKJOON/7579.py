import sys; input = sys.stdin.readline

n, m = map(int, input().split())
usage = [0] + list(map(int, input().split()))
restart = [0] + list(map(int, input().split()))
s = sum(restart)

dp = [[0] * (s + 1) for _ in range(n + 1)]
result = float('inf')

for i in range(1, n + 1):
    target, weight = usage[i], restart[i]

    for j in range(1, s + 1):
        if weight > j: dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(target + dp[i - 1][j - weight], dp[i - 1][j])
        
        if dp[i][j] >= m:
            result = min(result, j)
if m != 0: print(result)
else: print(0)