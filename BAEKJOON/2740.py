import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        temp = 0
        for idx, a1 in enumerate(a[i]):
            temp += a1 * b[idx][j]
        result[i][j] = temp

for i in result: print(*i)