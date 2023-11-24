from collections import deque

def solution(board):
    n = len(board)
    answer = int(1e9)
    d = [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]

    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]

    q = deque([(0, 0, 0, -1)])
    while q:
        x, y, cost, way = q.popleft()
        if x == n - 1 and y == n - 1 and answer > cost: answer = cost
        for dx, dy, dw in d:
            nx, ny = x + dx, y + dy
            add_cost = 100 if way == dw or way == -1 else 600

            if 0 <= nx < n and 0 <= ny < n and not board[nx][ny] and dp[nx][ny] >= cost + add_cost - 400:
                dp[nx][ny] = cost + add_cost
                q.append((nx, ny, cost + add_cost, dw))
    return answer