import sys, heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
ary = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    ary[a].append((c, b))

def daji(start, type):
    graph = [float('inf')] * (n + 1)
    graph[start] = 0
    q = [(0, start)]

    while q:
        weight, target = heapq.heappop(q)

        if weight > graph[target]: continue
        for wei, tar in ary[target]:
            if graph[tar] > wei + weight:
                heapq.heappush(q, (wei + weight, tar))
                graph[tar] = wei + weight
    if not type: return graph[x]
    else: return graph

result = 0
back = daji(x, 1)
for i in range(1, n + 1):
    result = max(result, daji(i, 0) + back[i])
print(result)