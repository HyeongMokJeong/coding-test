import sys; input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
dp = [[0] * n for _ in range(n)]

for start in range(n):
    for end in range(start + 1):
        if start == end: dp[start][end] = 1
        elif num[start] == num[end]: 
            if start - end == 1: dp[start][end] = 1
            elif dp[start - 1][end + 1] == 1:
                dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[e - 1][s - 1])