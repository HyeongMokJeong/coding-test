import sys; input = sys.stdin.readline
from collections import deque

N = int(input().rstrip())
K = int(input().rstrip())
ary = [[0] * N for _ in range(N)]
ary[0][0] = 1
for _ in range(K):
    a, b = map(int, input().split())
    ary[a - 1][b - 1] = 'A'

dic = dict()
L = int(input().rstrip())
for _ in range(L):
    x, c = input().split()
    dic[int(x)] = c

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0
def turn(alpha):
    global direction
    if alpha == 'L': direction = (direction - 1) % 4
    else: direction = (direction + 1) % 4

x, y = 0, 0
result = 0
q = deque([(0, 0)])
while q:
    result += 1
    x += dx[direction]
    y += dy[direction]

    if 0 > x or x >= N or 0 > y or y >= N or ary[x][y] == 1: break
    
    if ary[x][y] == 'A':
        ary[x][y] = 1
        q.append((x, y))
    
    elif ary[x][y] == 0:
        ary[x][y] = 1
        q.append((x, y))
        tx, ty = q.popleft()
        ary[tx][ty] = 0

    if result in dic: turn(dic[result])
print(result)