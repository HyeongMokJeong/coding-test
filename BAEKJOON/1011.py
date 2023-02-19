import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x
    move = 1
    while 1:
        if move**2 - (move - 1) <= distance <= move**2 + move:
            if move**2 - (move - 1) <= distance <= move**2: print(2 * move - 1)
            else: print(2 * move)
            break
        move += 1