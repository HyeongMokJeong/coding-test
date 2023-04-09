import sys, heapq
input = sys.stdin.readline

n, m, r = map(int, input().split())
node = [0] + list(map(int, input().split()))
edge = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    edge[a].append((b, l))
    edge[b].append((a, l))

def dijk(start):
    q = []
    ary = [99999] * (n + 1)
    ary[start] = 0

    heapq.heappush(q, (0, start))
    while q:
        weight, target = heapq.heappop(q)

        for i, wei in edge[target]:
            if weight + wei < ary[i]:
                ary[i] = weight + wei
                heapq.heappush(q, (ary[i], i))
    
    temp = 0
    for i in range(1, n + 1):
        if ary[i] <= m: temp += node[i]
    return temp

result = 0
for i in range(1, n + 1):
    result = max(result, dijk(i))
print(result)