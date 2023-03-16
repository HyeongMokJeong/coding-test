import sys, heapq

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    min_q, max_q = [], []
    result = []
    visited = [0] * k
    for i in range(k):
        case = sys.stdin.readline().rstrip().split()
        o, num = case[0], int(case[1])
        if o == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-1 * num, i))
            result.append(num)
        else:
            if num == 1:
                while max_q and visited[max_q[0][1]]: heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = 1
                    heapq.heappop(max_q)
            else:
                while min_q and visited[min_q[0][1]]: heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = 1
                    heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]]: heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]]: heapq.heappop(min_q)
    print(f"{-1 * max_q[0][0]} {min_q[0][0]}" if max_q and min_q else 'EMPTY')