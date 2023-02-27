import sys
from collections import defaultdict, deque

n, m, v = map(int, sys.stdin.readline().split())
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].append(b)
    dic[b].append(a)
for i in dic.keys(): dic[i].sort()

visited = [0] * (n + 1)
result_dfs = [v]
def dfs(target):
    visited[target] = 1
    for i in dic[target]:
        if not visited[i]:
            result_dfs.append(i)
            dfs(i)

q = deque()
result_bfs = []
def bfs(v):
    q.append(v)
    visited = [0] * (n + 1)
    while q:
        target = q.popleft()
        visited[target] = 1
        result_bfs.append(target)
        for i in dic[target]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

dfs(v)
bfs(v)
print(*result_dfs)
print(*result_bfs)