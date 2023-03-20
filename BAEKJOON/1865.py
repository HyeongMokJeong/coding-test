import sys
tc = int(sys.stdin.readline().rstrip())

def bf(start):
    ary = [10001 for _ in range(n + 1)]
    ary[start] = 0

    for i in range(n):
        for s, e, t in edge:
            if ary[e] > ary[s] + t:
                ary[e] = ary[s] + t
                if i == n - 1:
                    return True
    return False

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    edge = []
    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        edge.append((s, e, t))
        edge.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        edge.append((s, e, -1 * t))

    result = bf(1)
    if result: print("YES")
    else: print("NO")