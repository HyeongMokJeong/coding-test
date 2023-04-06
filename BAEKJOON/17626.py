n = int(input())

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    t, min_v = 1, 4
    while (t ** 2) <= i:
        a = dp[i - (t ** 2)]
        min_v = min(min_v, a)
        t += 1
    dp[i] = min_v + 1
print(dp[n])