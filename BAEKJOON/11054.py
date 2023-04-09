import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
reverse_ary = ary[::-1]

inc_dp = [1] * n; dec_dp = [1] * n

for i in range(n):
    for j in range(i):
        if ary[i] > ary[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)
        if reverse_ary[i] > reverse_ary[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

result = 0
for i in range(n):
    result = max(result, inc_dp[i] + dec_dp[n - i - 1] - 1)
print(result)