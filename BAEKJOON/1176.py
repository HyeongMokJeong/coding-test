from collections import defaultdict
import sys

v = int(input())
dic = defaultdict(list)
result = 0
node_num = 0
visited = [False for _ in range(v)]

def dfs(node, length):
    global result, node_num
    if (result < length):
        result = max(result, length)
        node_num = node
    
    for a, b in dic[node]:
        if not visited[a]:
            visited[a] = True
            dfs(a, length + b)
            visited[a] = False

for i in range(v):
    weight = list(map(int, sys.stdin.readline().split()))
    if len(weight) == 2: continue
    for j in range(1, len(weight) - 2, 2):
        dic[weight[0] - 1].append([weight[j] - 1, weight[j + 1]])

visited[0] = True
dfs(0, 0)
visited[0] = False

visited[node_num] = True
dfs(node_num, 0)

print(result)
