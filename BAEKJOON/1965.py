import sys; input = sys.stdin.readline

n = int(input().rstrip())
ary = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    big = 0
    for j in range(i):
        if ary[i] > ary[j]: big = max(big, dp[j] + 1)
    dp[i] = big
print(max(dp))