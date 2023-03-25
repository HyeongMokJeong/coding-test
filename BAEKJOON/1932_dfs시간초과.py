import sys

n = int(sys.stdin.readline().rstrip())
tree = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n_tree = [[0] * len(i) for i in tree]
n_tree[0][0] = tree[0][0]

def dfs(level, idx):
    if level >= n - 1: return
    n_tree[level + 1][idx] = max(n_tree[level][idx] + tree[level + 1][idx], n_tree[level + 1][idx])
    n_tree[level + 1][idx + 1] = max(n_tree[level][idx] + tree[level + 1][idx + 1], n_tree[level + 1][idx + 1])
    for i in range(len(tree[level + 1])):
        dfs(level + 1, i)

dfs(0, 0)
print(max(n_tree[n - 1]))