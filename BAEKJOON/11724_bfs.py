import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)
dic = defaultdict(set)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    dic[u].add(v)
    dic[v].add(u)

result = 0

def bfs(target):
    q = deque([target])
    while q:
        t = q.popleft()
        for i in dic[t]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        result += 1
print(result)