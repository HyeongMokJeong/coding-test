from collections import deque

n = int(input())
dp = deque([0, 1])
if n == 0: print(0)
elif n == 1: print(1)
else:  
    c, target = 2, 0
    while c <= n:
        target = sum(dp)
        dp.popleft()
        dp.append(target)
        c += 1
    print(target % 1000000007)