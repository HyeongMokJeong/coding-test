import sys

n = int(input())
m = int(input())
ary = [[] for i in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    ary[a] += [b]
    ary[b] += [a]

def dfs(a):
    visited[a] = True
    for i in ary[a]:
        if not visited[i]: dfs(i)

q = [1]
def bfs(a):
    while q:
        target = q.pop(0)
        visited[target] = True
        for i in ary[target]:
            if not visited[i]: q.append(i)

bfs(1)
print(visited.count(True) - 1)