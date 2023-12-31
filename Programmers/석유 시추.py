from collections import deque

def solution(land):
    mx, my = len(land[0]), len(land)
    visited = [[0] * mx for _ in range(my)]
    dp = [0] * mx
    
    def find(a, b):
        x_set = set([a])
        q = deque([(a, b)])
        count = 1
        
        while q:
            x, y = q.popleft()
            
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < mx and 0 <= ny < my and not visited[ny][nx] and land[ny][nx] == 1:
                    count += 1
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                    x_set.add(nx)
        for i in x_set: dp[i] += count
    
    for i in range(mx):
        for j in range(my):
            if not visited[j][i] and land[j][i] == 1:
                visited[j][i] = 1
                find(i, j)
    return max(dp)