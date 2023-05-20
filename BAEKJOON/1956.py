import sys, heapq; input = sys.stdin.readline

V, E = map(int, input().split())
road = [[] for _ in range(V + 1)]
temp = [[float('inf')] * (V + 1) for _ in range(V + 1)]
q = []

for _ in range(E):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    temp[a][b] = c
    heapq.heappush(q, (c, a, b))

while q:
    c, a, b = heapq.heappop(q)
    if a == b:
        print(c)
        break

    if temp[a][b] < c: continue
    for tar, wei in road[b]:
        if c + wei < temp[a][tar]:
            temp[a][tar] = c + wei
            heapq.heappush(q, (c + wei, a, tar))
else: print(-1)