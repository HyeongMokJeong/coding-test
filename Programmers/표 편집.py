from heapq import heappop, heappush
from collections import deque

def solution(n, k, cmd):
    answer = ['O'] * n

    q1, q2, del_s = [], [], deque()
    for i in range(k): heappush(q1, -i)
    for i in range(k, n): heappush(q2, i)

    for i in cmd:
        if len(i) == 1:
            if i == "C":
                target = heappop(q2)
                del_s.appendleft(target)
                if not q2: heappush(q2, -heappop(q1))
            else:
                target = del_s.popleft()
                if target > q2[0]: heappush(q2, target)
                else: heappush(q1, -target)
        else:
            cm, co = i.split()
            co = int(co)
            if cm == "D":
                for i in range(co):
                    heappush(q1, -heappop(q2))
            else:
                for i in range(co):
                    heappush(q2, -heappop(q1))
    
    for i in del_s: answer[i] = 'X'
    return ''.join(answer)