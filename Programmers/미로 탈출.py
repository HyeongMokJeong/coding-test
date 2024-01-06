from collections import deque
def solution(maps):
    mx, my = len(maps), len(maps[0])

    def bfs(start, end):
        visited = [[0] * my for _ in range(mx)]
        visited[start[0]][start[1]] = 1

        q = deque([start])
        while q:
            x, y, count = q.popleft()

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx < mx and 0 <= ny < my and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    if (nx, ny) == (end[0], end[1]): return count + 1
                    visited[nx][ny] = 1
                    q.append((nx, ny, count + 1))
        return -1

    for idx, i in enumerate(maps):
        for idy, j in enumerate(i):
            if j == 'S': start = (idx, idy, 0)
            if j == 'L': lever = (idx, idy, 0)
            if j == 'E': end = (idx, idy, 0)

    s_l, l_e = bfs(start, lever), bfs(lever, end)
    if s_l == -1 or l_e == -1: return -1

    return s_l + l_e