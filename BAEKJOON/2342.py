import sys; sys.setrecursionlimit(10 ** 9)

ary = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(100000)]

def move(a, b):
    if a == b: return 1
    elif a == 0: return 2
    elif abs(a - b) % 2 == 1: return 3
    else: return 4

def solve(n, l, r):
    global dp
    if n >= len(ary) - 1: return 0
    if dp[n][l][r] != -1: return dp[n][l][r]

    dp[n][l][r] = min(solve(n + 1, ary[n], r) + move(l, ary[n]), solve(n + 1, l, ary[n]) + move(r, ary[n]))
    return dp[n][l][r]

print(solve(0, 0, 0))