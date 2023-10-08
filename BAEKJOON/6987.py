import sys; input = sys.stdin.readline
from itertools import combinations

def dfs(n):
    global cnt

    if n == 15:
        cnt = 1
        for i in res:
            if i.count(0) != 3:
                cnt = 0
                break
        return
    
    g1, g2 = games[n]
    for i, j in ((0, 2), (1, 1), (2, 0)):
        if res[g1][i] > 0 and res[g2][j] > 0:
            res[g1][i] -= 1
            res[g2][j] -= 1
            dfs(n + 1)
            res[g1][i] += 1
            res[g2][j] += 1

result = []
games = list(combinations(range(6), 2))
for _ in range(4):
    tmp = list(map(int, input().split()))
    res = [tmp[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    result.append(cnt)
print(*result)