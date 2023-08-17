from collections import deque
F, S, G, U, D = map(int, input().split())

q = deque([(S, 0)])
visited = [0] * (F + 1)
visited[S] = 1

while q:
    t, count = q.popleft()

    if t == G:
        print(count)
        break
    
    for i in [(t + U), (t - D)]:
        if 0 < i <= F and not visited[i]:
            visited[i] = 1
            q.append((i, count + 1))
else: print("use the stairs")