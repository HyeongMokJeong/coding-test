import sys; input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    ary[a][b] = 1


for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if ary[i][k] and ary[k][j]: ary[i][j] = 1

result = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if ary[i][j]:
            result[i] += 1
            result[j] += 1
print(result.count(N - 1))