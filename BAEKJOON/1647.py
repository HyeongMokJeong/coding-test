import sys
input = sys.stdin.readline

def find_parent(target):
    if parent[target] != target:
        parent[target] = find_parent(parent[target])
    return parent[target]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
ary = []
for _ in range(m):
    a, b, c = map(int, input().split())
    ary.append((c, a, b))
parent = [i for i in range(n + 1)]

ary.sort()

selected = []
for c, a, b in ary:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        selected.append(c)

print(sum(selected[:-1]))