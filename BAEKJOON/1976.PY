import sys; input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
ary = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]
plan = list(map(int, input().split()))

def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a, b = find(x), find(y)
    if a > b: parent[a] = b
    else: parent[b] = a

for i in range(N):
    for j in range(N):
        if ary[i][j]: union(i, j)

target = parent[plan[0] - 1]
for i in plan[1:]:
    if target != parent[i - 1]:
        print("NO")
        break
else: print("YES")