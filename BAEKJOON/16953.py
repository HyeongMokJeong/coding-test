from collections import deque

a, b = map(int, input().split())
MAX = 10 ** 9
q = deque([(a, 1)])

while q:
    t, cnt, type = q.popleft()
    if t == b:
        print(cnt)
        break
    elif t > MAX: continue
    q.append((t * 2, cnt + 1))
    q.append((t * 10 + 1, cnt + 1))
else:
    print(-1)