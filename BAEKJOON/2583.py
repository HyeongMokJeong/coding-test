import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**2)

M, N, K = map(int, input().split())
ary = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            ary[i][j] = 1

def dfs(x, y):
    global count
    count += 1
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < M and 0 <= ny < N and not ary[nx][ny]:
            ary[nx][ny] = 1
            dfs(nx, ny)

result, count = 0, 0
temp = []
for i in range(M):
    for j in range(N):
        if not ary[i][j]:
            result += 1
            ary[i][j] = 1
            dfs(i, j)
            temp.append(count)
            count = 0

print(result)
print(*sorted(temp))