from collections import defaultdict

n = int(input())
tree = list(map(int, input().split()))
d = int(input())
dic = defaultdict(list)
for idx, i in enumerate(tree): dic[i].append(idx)
answer = 0

def dfs(node):
    tree[node] = -2
    for i in range(n):
        if tree[i] == node: dfs(i)

dfs(d)
for idx, i in enumerate(tree):
    if i != -2 and idx not in tree: answer += 1

print(answer)