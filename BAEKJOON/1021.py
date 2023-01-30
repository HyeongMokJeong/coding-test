from collections import deque

n, m = map(int, input().split())
num = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

move = 0
for i in num:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q)/2:
                q.append(q.popleft())
                move += 1
            else:
                q.appendleft(q.pop())
                move += 1
print(move)