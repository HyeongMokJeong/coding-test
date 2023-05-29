import sys, heapq; input = sys.stdin.readline

N = int(input().rstrip())
q = []
for _ in range(N):
    ary = list(map(int, input().split()))
    for i in ary:
        if len(q) < N:
            heapq.heappush(q, i)
        else:
            if i > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, i)
print(q[0])