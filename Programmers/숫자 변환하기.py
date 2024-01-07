def solution(x, y, n):
    dp = [-1] * (y + 1)
    dp[x] = 0
    
    for i in range(x, y + 1):
        if dp[i] == -1: continue
        cases = (i + n, i * 2, i * 3)
        for c in cases:
            if c < y + 1:
                if dp[c] == -1: dp[c] = dp[i] + 1
                else: dp[c] = min(dp[c], dp[i] + 1)
    return dp[y]