import sys; input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

result = [float('inf')] * (N + 1)
result[1] = 0
q = [(0, 1)]
while q:
    w, t = heapq.heappop(q)
    if t == N:
        print(result[t])
        break
    if result[t] < w: continue
    for wei, i in graph[t]:
        if w + wei < result[i]:
            result[i] = w + wei
            heapq.heappush(q, (w + wei, i))