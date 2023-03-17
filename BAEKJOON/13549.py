from collections import deque

n, k = map(int, input().split())
ary = [float('inf')] * 100001
ary[n] = 0

q = deque([n])
while q:
    t = q.popleft()
    if t == k:
        print(ary[t])
        break
    
    for i in (-1, 1):
        temp = t + i
        if 0 <= temp < len(ary):
            if ary[t] + 1 <= ary[temp]:
                ary[temp] = ary[t] + 1
                q.append(temp)
    temp = t * 2
    if 0 <= temp < len(ary):
        if ary[t] <= ary[temp]:
            ary[temp] = ary[t]
            q.append(temp)