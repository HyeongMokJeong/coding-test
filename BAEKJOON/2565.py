import sys; input = sys.stdin.readline

n = int(input().rstrip())
ary, dp = [], [1] * n
for _ in range(n):
    a, b = map(int, input().split())
    ary.append((a, b))
ary.sort()

for i in range(1, n):
    for j in range(i):
        if ary[j][1] < ary[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))