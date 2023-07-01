D, K = map(int, input().split())

dp = [0] * D
dp[0], dp[1] = 1, 1

while True:
    for i in range(2, D): dp[i] = dp[i - 2] + dp[i - 1]

    if dp[D - 1] < K: dp[1] += 1
    elif dp[D - 1] > K: 
        dp[0] += 1
        dp[1] = dp[0]
    else:
        print(dp[0], dp[1], sep="\n")
        break