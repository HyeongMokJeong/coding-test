import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
ary = [i for i in range(n + 1)]

def find(idx):
    if ary[idx] == idx: return idx
    ary[idx] = find(ary[idx])
    return ary[idx]

def union(a, b):
    a, b = find(a), find(b)
    if a < b: ary[b] = a
    elif a > b: ary[a] = b

for _ in range(m):
    t, a, b = map(int, input().split())
    if not t: union(a, b)
    else: print("NO" if find(a) != find(b) else "YES")