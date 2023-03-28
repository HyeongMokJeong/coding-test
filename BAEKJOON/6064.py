import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    count = x

    while count <= m * n:
        if (count - x) % m == 0 and (count - y) % n == 0:
            print(count)
            break
        count += m
    else: print(-1)