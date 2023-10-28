import sys; input = sys.stdin.readline

n, m = map(int, input().split())
x, y = [], []
for _ in range(m):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort(); y.sort()
a, b = x[m // 2], y[m // 2]
result = 0
for i in range(m): result += abs(a - x[i]) + abs(b - y[i])
print(result)