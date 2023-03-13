import sys, heapq
from collections import defaultdict

n, m = int(sys.stdin.readline().strip()), int(sys.stdin.readline().strip())
dic = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    dic[a].append((b, c))
start, end = map(int, sys.stdin.readline().split())

weight = [float('inf')] * (n + 1)
weight[start] = 0
q = [(0, start)]

while q:
    wei, t = heapq.heappop(q)
    if weight[t] < wei: continue

    for next, w in dic[t]:
        cost = weight[t] + w
        if cost < weight[next]:
            weight[next] = cost
            heapq.heappush(q, (cost, next))

print(weight[end])