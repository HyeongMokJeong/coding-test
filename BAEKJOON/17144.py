import sys
from collections import deque
input = sys.stdin.readline

R, C, T = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(R)]
cleaner = []
for i in range(2, R):
    if ary[i][0] == -1:
        cleaner.append(i)
        cleaner.append(i + 1)
        break
    
def can(x, y):
    count = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < R and 0 <= ny < C and ary[nx][ny] != -1:
            count += 1
    return count

def bfs(): # bfs 1사이클(1초)
    q = deque()
    for i in range(R):
        for j in range(C):
            if ary[i][j] > 0: q.append((i, j, ary[i][j]))
    
    while q:
        x, y, value = q.popleft()
        target = value // 5
        ary[x][y] -= target * can(x, y)
        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= nx < R and 0 <= ny < C and ary[nx][ny] != -1:
                ary[nx][ny] += target

def cleanUp():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner[0], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner[0] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        ary[x][y], before = before, ary[x][y]
        x = nx
        y = ny

def cleanDown():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner[1], 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner[1] and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        ary[x][y], before = before, ary[x][y]
        x = nx
        y = ny

for _ in range(T):
    bfs()
    cleanUp()
    cleanDown()
result = 0
for i in range(R):
    for j in range(C):
        if ary[i][j] > 0:
            result += ary[i][j]
print(result)