import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    q = deque([(a, "")])
    visited = [0] * 10000
    
    while q:
        t, move = q.popleft()
        visited[t] = 1
        if t == b:
            print(move)
            break
        d = (t * 2) % 10000
        if not visited[d]:
            q.append([d, move + 'D'])
            visited[d] = 1

        s = (t - 1) % 10000
        if not visited[s]:
            q.append([s, move + 'S'])
            visited[s] = 1

        l = (t % 1000) * 10 + (t // 1000)
        if not visited[l]:
            q.append([l, move + 'L'])
            visited[l] = 1

        r = (t // 10) + (t % 10) * 1000
        if not visited[r]:
            q.append([r, move + 'R'])
            visited[r] = 1