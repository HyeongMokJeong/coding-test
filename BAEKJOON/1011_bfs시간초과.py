import sys
from collections import deque

move = [-1, 0, 1]
result = []
t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    q = deque()

    q.append([x + 1, 1, 1]) # 현재좌표, 이전 거리, 카운트
    while q:
        target = q.pop()
        if target[0] >= y:
            if target[0] == y and target[1] == 1:
                result.append(target[2])
                break
            continue

        for i in move:
            if target[0] + (target[1] + i) > target[0]:
                q.append([target[0] + (target[1] + i), target[1] + i, target[2] + 1])

for i in result: print(i)