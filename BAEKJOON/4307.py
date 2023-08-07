import sys; input = sys.stdin.readline

for _ in range(int(input())):
    l, n = map(int, input().split())
    ary = []
    for _ in range(n): ary.append(int(input()))
    ary.sort()

    min_r, max_r = 0, 0
    for i in ary:
        min_r = max(min_r, min(i, l - i))
        max_r = max(max_r, i, l - i)
    print(min_r, max_r)