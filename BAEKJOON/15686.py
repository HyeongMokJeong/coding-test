import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
home, chicken = [], []

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2: chicken.append((i, j))
        elif matrix[i][j] == 1: home.append((i, j))

result = float('inf')
for i in combinations(chicken, m):
    chicken_len = 0
    for x, y in home:
        home_len = float('inf')
        for j in range(m):
            home_len = min(home_len, abs(x - i[j][0]) + abs(y - i[j][1]))
        chicken_len += home_len
    result = min(result, chicken_len)
print(result)