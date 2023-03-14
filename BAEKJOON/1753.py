import sys, heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline().strip())
edge = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    edge[a].append((b, c))

weight = [float('inf')] * (v + 1)
weight[k] = 0

q = [(0, k)]
while q:
    w, t = heapq.heappop(q)

    if weight[t] < w: continue

    for tar, wei in edge[t]:
        cost = wei + weight[t]
        if weight[tar] > cost:
            weight[tar] = cost
            heapq.heappush(q, (cost, tar))

for i in weight[1:]: print(i if i != float('inf') else "INF")