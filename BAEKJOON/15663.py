import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
visited = [0] * n

ary = []
def dfs():
    if len(ary) == m:
        print(*ary)
        return
    overlab = 0
    for i in range(n):
        if overlab != num[i] and not visited[i]:
            ary.append(num[i])
            visited[i] = 1
            overlab = num[i]
            dfs()
            ary.pop()
            visited[i] = 0
dfs()