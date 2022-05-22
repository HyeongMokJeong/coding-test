import heapq

def solution(scoville, K):
    answer = 0
    lists = []

    scoville = sorted(scoville)
    for i in scoville:
        if i < K: heapq.heappush(lists, i)
        else:  
            heapq.heappush(lists, i)
            break

    while lists[0] <= K:
        if len(lists) == 1: break
        new = heapq.heappop(lists) + heapq.heappop(lists) * 2
        heapq.heappush(lists, new)
        answer += 1
    if lists[0] < K: return -1
    return answer

print(solution([1, 3, 2, 9, 10, 12], 7))