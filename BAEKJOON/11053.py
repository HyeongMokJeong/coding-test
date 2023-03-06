import sys

n = int(sys.stdin.readline().rstrip())
ary = list(map(int, sys.stdin.readline().split()))
visited = [1] * n

for i in range(n):
    for j in range(i):
        if ary[i] > ary[j]:
            visited[i] = max(visited[i], visited[j] + 1)
print(max(visited))