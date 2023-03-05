from collections import deque

n, k = map(int, input().split())
q = deque([n])
MAX = 10 ** 5
visited = [0] * (MAX + 1)
visited[n] = 1
while q:
    t  = q.popleft()
    if (t == k):
        print(visited[t] - 1)
        break
    for i in (t - 1, t + 1, 2 * t):
        if 0 <= i <= MAX and not visited[i]:
            q.append(i)
            visited[i] = visited[t] + 1