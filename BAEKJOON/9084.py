import sys; input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ary = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1
    for i in ary:
        for j in range(1, m + 1):
            if j >= i: dp[j] += dp[j - i]
    print(dp[m])