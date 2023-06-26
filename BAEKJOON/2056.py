import sys; input = sys.stdin.readline

N = int(input().rstrip())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    ary = list(map(int, input().split()))
    for j in ary[1:]:
        dp[i] = max(dp[i], dp[j] + ary[0])
print(max(dp))