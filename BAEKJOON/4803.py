import sys; input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque([start])
    result = False

    while q:
        t = q.popleft()
        if visited[t]: result = True
        visited[t] = 1
        for i in graph[t]:
            if not visited[i]: q.append(i)
    return result

case = 1
while True:
    n, m = map(int, input().split())
    if not n and not m: break

    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    result = 0
    for i in range(1, n + 1):
        if not visited[i] and not bfs(i): result += 1

    if result == 0: print(f'Case {case}: No trees.')
    elif result == 1: print(f'Case {case}: There is one tree.')
    else: print(f'Case {case}: A forest of {result} trees.')
    case += 1