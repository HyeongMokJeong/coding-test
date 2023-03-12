import sys

n, m = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

ary = []
def dfs(idx):
    if len(ary) == m:
        print(*ary)
        return
    temp = 0
    for i in range(idx, n):
        if temp != num[i]:
            temp = num[i]
            ary.append(num[i])
            dfs(i)
            ary.pop()
dfs(0)