import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

ary = []
def dfs(idx):
    if len(ary) == m:
        print(*ary)
        return
    for i in range(idx, n):
        ary.append(num[i])
        dfs(i)
        ary.pop()
dfs(0)