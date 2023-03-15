import sys
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def dfs(node):
    for t, w in tree[node]:
        if visited[t] == -1:
            visited[t] = visited[node] + w
            dfs(t)

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1)
temp = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[temp] = 0
dfs(temp)
print(max(visited))