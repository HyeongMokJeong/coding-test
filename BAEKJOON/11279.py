import sys, heapq

n = int(sys.stdin.readline().rstrip())
q = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(q) == 0: print(0)
        else: print(-1 * heapq.heappop(q))
    heapq.heappush(q, -1 * x)