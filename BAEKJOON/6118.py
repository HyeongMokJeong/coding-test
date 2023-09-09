import sys; input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
result = [0] * (N + 1)
result[1] = 1
q = deque([1])

while q:
    t = q.popleft()
    for i in graph[t]:
        if not result[i]:
            result[i] = result[t] + 1
            q.append(i)
m = max(result)
print(result.index(m), m - 1, result.count(m))