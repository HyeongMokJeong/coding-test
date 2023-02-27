import sys

t = int(sys.stdin.readline())
for _ in range(t):
    zero, one = 0, 0
    ary = [(1, 0), (0, 1)]
    n = int(sys.stdin.readline())
    if n >= len(ary): 
        for i in range(2, n + 1):
            a, b = ary[i - 2][0] + ary[i - 1][0], ary[i - 2][1] + ary[i - 1][1]
            ary.append((a, b))
    print(*ary[n])