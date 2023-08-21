import sys; input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
q = deque()
ary = []
for i in range(R):
    m = list(input().rstrip())
    ary.append(m)
    for j in range(C):
        if m[j] == 'X': q.append((i, j))
remove = []
while q:
    x, y = q.popleft()
    c = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 > nx or nx >= R or 0 > ny or ny >= C: c += 1
        elif 0 <= nx < R and 0 <= ny < C and ary[nx][ny] == '.': c += 1
        if c >= 3: break
    if c >= 3: remove.append((x, y))
for x, y in remove: ary[x][y] = '.'

startR, endR = 0, 0
start, end = 0, 0
for i in range(R):
    if 'X' in ary[i]: 
        startR = i
        break
for i in range(R - 1, -1, -1):
    if 'X' in ary[i]: 
        endR = i
        break

for i in range(C):
    for j in range(R):
        if ary[j][i] == 'X': 
            start = i
            break
    if start: break
for i in range(C - 1, -1, -1):
    for j in range(R - 1, -1, -1):
        if ary[j][i] == 'X': 
            end = i
            break
    if end: break

for i in range(startR, endR + 1):
    for j in ary[i][start:end + 1]:
        print(j, end="")
    print()