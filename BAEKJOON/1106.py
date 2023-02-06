c, n = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
dp = [float("inf") for _ in range(c + 100)]
dp[0] = 0

for cost, people in city:
    for i in range(people, c + 100):
        dp[i] = min(dp[i], dp[i - people] + cost)
print(min(dp[c:]))