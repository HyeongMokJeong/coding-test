import sys, heapq

n, e = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int ,sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(start, end):
    weight = [float('inf')] * (n + 1)
    weight[start] = 0
    q = [(0, start)]

    while q:
        w, t = heapq.heappop(q)

        if weight[t] < w: continue

        for tar, wei in tree[t]:
            cost = weight[t] + wei
            if weight[tar] > cost:
                weight[tar] = cost
                heapq.heappush(q, (cost, tar))
    return weight[end]

case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

print(min(case1, case2) if min(case1, case2) != float('inf') else -1)