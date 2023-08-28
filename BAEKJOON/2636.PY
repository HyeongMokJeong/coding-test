import sys; input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(a)]

def check():
    for i in ary:
        if 1 in i: return False
    return True

def bfs():
    global result_a, result_b
    q = deque([(0, 0)])
    melt = []
    visited = [[0] * b for _ in range(a)]
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < a and 0 <= ny < b and not visited[nx][ny]:
                visited[nx][ny] = 1
                if not ary[nx][ny]: q.append((nx, ny))
                else: melt.append((nx, ny))
    for x, y in melt: ary[x][y] = 0
    result_a += 1
    result_b = len(melt)

result_a, result_b = 0, 0
while not check(): bfs()
print(result_a)
print(result_b)