from collections import deque
import sys; input = sys.stdin.readline

K = int(input().rstrip())

def bfs(start):
    q = deque([start])
    visited[start] = 1
    while q:
        t = q.popleft()
        for i in tree[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = -1 * visited[t]
            elif visited[i] == visited[t]: return False
    return True

for _ in range(K):
    V, E = map(int, input().split())
    tree = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    visited = [0] * (V + 1)
    for i in range(1, V + 1):
        if not visited[i]:
            if not bfs(i):
                print("NO")
                break
    else: print("YES")