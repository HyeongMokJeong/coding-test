import sys; input = sys.stdin.readline

while True:
    N = int(input())
    if not N: break

    ary = [int(input()) for _ in range(N)]
    dp = [0] * N
    dp[0] = ary[0]

    for i in range(1, N):
        dp[i] = max(ary[i], dp[i - 1] + ary[i])
    print(max(dp))