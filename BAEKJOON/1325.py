import sys; input = sys.stdin.readline

n, m = map(int, input().split())
ary = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ary[b].append(a)

m = 0
visited = [0] * (n + 1)
def dfs(start):
    global m

    for nt in ary[start]:
        if not visited[nt]:
            m += 1
            visited[nt] = 1
            dfs(nt)
            visited[nt] = 0

ma = 0
result = []
for i in range(1, n + 1):
    visited[i] = 1
    dfs(i)
    if m > ma:
        ma = m
        result.clear()
        result.append(i)
    elif m == ma: result.append(i)
    m = 0
    visited[i] = 0

print(*result)