import sys

n = int(sys.stdin.readline().rstrip())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for idx, i in enumerate(tree[1:], start=1):
    for idy, j in enumerate(i):
        if idy == 0:
            tree[idx][idy] += tree[idx - 1][idy]
        elif idy == len(i) - 1:
            tree[idx][idy] += tree[idx - 1][idy - 1]
        else:
            tree[idx][idy] += max(tree[idx - 1][idy - 1], tree[idx - 1][idy])
print(max(tree[n - 1]))