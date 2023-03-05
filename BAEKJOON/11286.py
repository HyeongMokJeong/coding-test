import sys, heapq

n = int(input())
ary = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(ary, (abs(x), x))
    else:
        if len(ary) != 0:
            print(heapq.heappop(ary)[1])
        else:
            print(0)