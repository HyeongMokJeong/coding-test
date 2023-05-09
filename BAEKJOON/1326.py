import sys; input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
ary = [0] + list(map(int, input().split()))
a, b = map(int, input().split())

q = deque([a])
visited = [-1] * (n + 1)
visited[a] = 0
while q:
    t = q.popleft()
    if t == b:
        break

    for i in range(t, n + 1, ary[t]):
        if visited[i] == -1:
            visited[i] = visited[t] + 1
            q.append(i)
    for i in range(t, 0, -ary[t]):
        if visited[i] == -1:
            visited[i] = visited[t] + 1
            q.append(i)
print(visited[b])