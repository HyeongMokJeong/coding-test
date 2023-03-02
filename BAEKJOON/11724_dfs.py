import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)
q = deque([1])
dic = defaultdict(set)

result = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    dic[u].add(v)
    dic[v].add(u)

def dfs(target):
    for i in dic[target]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)