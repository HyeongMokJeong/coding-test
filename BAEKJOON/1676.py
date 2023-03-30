n = int(input())
dp = [i for i in range(n + 1)]
if n >= 3:
    for i in range(3, n + 1):
        dp[i] *= dp[i - 1]

count = 0
if n != 0:
    for i in str(dp[n])[::-1]:
        if i == '0': count += 1
        else: break
print(count)