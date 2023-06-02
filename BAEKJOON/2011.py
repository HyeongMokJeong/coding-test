ary = [0] + list(map(int, list(input())))
if ary[1] == 0:
    print(0)
    exit(0)
dp = [0] * len(ary)
dp[0] = 1

for i in range(1, len(ary)):
    if ary[i] > 0:
        dp[i] += dp[i - 1]
    if 10 <= ary[i - 1] * 10 + ary[i] <= 26:
        dp[i] += dp[i - 2]
print(dp[-1] % 1000000)