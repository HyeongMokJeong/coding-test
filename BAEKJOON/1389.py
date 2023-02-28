import sys
from collections import defaultdict, deque
n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(set)
result = [float('inf')]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)

def run(target):
    visited = [0] * (n + 1)
    visited[target] = 0
    q = deque()
    q.append(target)

    while q:
        t = q.popleft()
        for i in dic[t]:
            if not visited[i] and i != target:
                visited[i] = visited[t] + 1
                q.append(i)
    result.append(sum(visited))

for i in range(1, n + 1):
    run(i)

print(result.index(min(result)))