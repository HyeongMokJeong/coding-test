import sys, heapq
from collections import defaultdict

v, e = map(int, input().split())
dic = defaultdict(list)
for _ in range(e):
    a, b, weight = map(int, sys.stdin.readline().rstrip().split())
    dic[a].append([b, weight])
    dic[b].append([a, weight])

def prim(start):
    visited, edge = [0] * (v + 1), [(0, start)]
    count = 0
    result = 0

    while (count < v):
        w, a = heapq.heappop(edge)
        if visited[a] == 1: continue
        visited[a] = 1
        count += 1
        result += w
        for a, w in dic[a]:
            heapq.heappush(edge, (w, a))
    return result

print(prim(1))