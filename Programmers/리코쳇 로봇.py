from collections import deque

def solution(board):
    for idy, i in enumerate(board):
        for idx, j in enumerate(i):
            if j == 'R': sy, sx = idy, idx

    mx, my = len(board[0]), len(board)
    visited = [[0] * mx for _ in range(my)]
    visited[sy][sx] = 1

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 0123
    q = deque([(sy, sx, 0, 0), (sy, sx, 1, 0), (sy, sx, 2, 0), (sy, sx, 3, 0)])

    while q:
        y, x, d, count = q.popleft()

        # 한 방향으로 끝까지 이동
        while True:
            ny, nx = y + move[d][0], x + move[d][1]
            if 0 > nx or nx >= mx or 0 > ny or ny >= my or board[ny][nx] == 'D': break
            else: y, x = ny, nx
        
        # 이동했을 때 G이면 종료
        if board[y][x] == 'G': return count + 1

        # 도착한 곳이 이미 처리한 곳이면 continue
        if visited[y][x]: continue
        visited[y][x] = 1

        # G가 아니면 모든 방향에 대해 q에 추가
        # 상 - 하, 좌 - 우에 대해서는 제외
        if d == 0 or d == 1: 
            q.append((y, x, 2, count + 1))
            q.append((y, x, 3, count + 1))
        else: 
            q.append((y, x, 0, count + 1))
            q.append((y, x, 1, count + 1))
    return -1