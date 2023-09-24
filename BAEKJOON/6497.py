import sys; input = sys.stdin.readline

def find(x):
    if ary[x] != x: ary[x] = find(ary[x])
    return ary[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: ary[y] = x
    else: ary[x] = y

while True:
    m, n = map(int, input().split())
    if not m and not n: break
    ary = [i for i in range(m)]
    q = [list(map(int, input().split())) for _ in range(n)]
    q.sort(key=lambda x:x[2])

    result = 0
    for x, y, z in q:
        if find(x) != find(y): union(x, y)
        else: result += z
    print(result)