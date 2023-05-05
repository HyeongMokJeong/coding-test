import sys; input = sys.stdin.readline

n, d = map(int, input().split())
root = [list(map(int, input().split())) for _ in range(n)]
dp = [i for i in range(d + 1)]

for i in range(d + 1):
    if i > 0: dp[i] = min(dp[i], dp[i - 1] + 1)
    for s, e, w in root:
        if s == i and e <= d and dp[i] + w < dp[e]:
            dp[e] = dp[i] + w
print(dp[d])