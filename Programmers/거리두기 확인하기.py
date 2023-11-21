from collections import deque
def solution(places):
    SIZE = 5    
    answer = []

    def bfs(i, j, cls):
        q = deque([(i, j, 0)])
        visited = [[0] * SIZE for _ in range(SIZE)] 

        while q:
            x, y, count = q.popleft()
            visited[x][y] = 1

            if count == 0:
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < SIZE and 0 <= ny < SIZE and cls[nx][ny] != 'X' and not visited[nx][ny]:
                        if cls[nx][ny] == 'P': return 0
                        q.append((nx, ny, 1))
            else:
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < SIZE and 0 <= ny < SIZE and cls[nx][ny] == 'P' and not visited[nx][ny]: return 0
        return 1

    def run(cls):
        for i in range(SIZE):
            for j in range(SIZE):
                if cls[i][j] == 'P':
                    if not bfs(i, j , cls): return 0
        return 1
    
    for i in places: answer.append(run(i))
    return answer