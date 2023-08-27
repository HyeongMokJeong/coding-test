n = int(input())
ary = list(map(int, input().split()))
dp=[[0 for _ in range(21)] for _ in range(n)]
dp[0][ary[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= ary[i] + j <= 20: dp[i][ary[i] + j] += dp[i - 1][j]
            if 0 <= j - ary[i] <= 20: dp[i][j - ary[i]] += dp[i - 1][j]
print(dp[-2][ary[-1]])