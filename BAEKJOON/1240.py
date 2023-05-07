import sys; input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ary = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    ary[a].append((b, c))
    ary[b].append((a, c))

def bfs(start, target):
    q = deque([(start, 0)])
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        t, w = q.popleft()
        if target == t: return w
        for tar, wei in ary[t]:
            if not visited[tar]:
                visited[tar] = 1
                q.append((tar, w + wei))

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))
