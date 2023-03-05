import sys
from collections import deque
n = int(input())
tree = [[] for _ in range(n + 1)]
result = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = deque([1])
visited = [0] * (n + 1)
visited[1] = 1
while q:
    t = q.popleft()
    for i in tree[t]:
        if not visited[i]:
            visited[i] = 1
            result[i] = t
            q.append(i)
for i in result[2:]: print(i)