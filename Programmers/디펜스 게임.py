from heapq import heappush, heappushpop

def solution(n, k, enemy):
    answer = hap = 0
    heap = []

    for i in enemy:
        hap += i
        if hap <= n: 
            heappush(heap, -i)
            answer += 1
        elif k > 0:
            k -= 1
            answer += 1
            hap += heappushpop(heap, -i)
        else: break
    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
print(solution(2, 4, [3, 3, 3, 3]))