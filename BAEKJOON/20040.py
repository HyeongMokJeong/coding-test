import sys; input = sys.stdin.readline

n, m = map(int, input().split())
sycle = [i for i in range(n)]
result = 0

def find(idx):
    if sycle[idx] != idx:
        sycle[idx] = find(sycle[idx])
    return sycle[idx]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        sycle[b] = a
    else:
        sycle[a] = b

for i in range(m):
    a, b = map(int, input().split())
    fa, fb = find(a), find(b)
    if fa == fb:
        print(i + 1)
        exit(0)
    union(fa, fb)
else: print(0)