from collections import deque
n, k = map(int, input().split())

visited = [0] * 100001
visited[n] = 0

result = 0
q = deque([n])
while q:
    t = q.popleft()
    if t == k:
        result += 1
        continue

    for i in (t - 1, t + 1, t * 2):
        if 0 <= i < len(visited):
            if not visited[i] or visited[i] == visited[t] + 1:
                visited[i] = visited[t] + 1
                q.append(i)
print(visited[k])
print(result)