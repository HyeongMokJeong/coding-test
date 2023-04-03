import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def bfs(target):
    q = deque([target])
    visited = [0] * n

    while q:
        t = q.popleft()
        for idx, i in enumerate(graph[t]):
            if i == 1 and not visited[idx]:
                visited[idx] = 1
                result[target][idx] = 1
                q.append(idx)

for i in range(n): bfs(i)
for i in result: print(*i)