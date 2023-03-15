import sys

n, m = int(sys.stdin.readline().rstrip()), int(sys.stdin.readline().rstrip())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1): graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] > c: graph[a][b] = c

for a in range(1, n + 1): # a를 반드시 거쳐서
    for b in range(1, n + 1): # b에서
        for c in range(1, n + 1): # c까지
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

for i in graph[1:]:
    for idx, j in enumerate(i[1:], start=1):
        if j == float('inf'):
            i[idx] = 0
    print(*i[1:])