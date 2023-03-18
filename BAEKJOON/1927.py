import sys, heapq

n = int(sys.stdin.readline().rstrip())
q = []

for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    if t == 0:
        if not q: print(0)
        else: print(heapq.heappop(q))
        continue
    heapq.heappush(q, t)