import heapq
def solution(stones, k):
    answer = float('inf')
    q = []
    for i in range(k - 1): heapq.heappush(q, (-stones[i], i))

    for i in range(k - 1, len(stones)):
        heapq.heappush(q, (-stones[i], i))
        while q[0][1] < i - k + 1: heapq.heappop(q)
        answer = min(answer, -q[0][0])
    return answer