import sys

n, k = map(int, sys.stdin.readline().split())
bag = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

weight = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n + 1): # weight 카운트 변수
    for j in range(1, k + 1): # 가방 무게
        w, cost = weight[i][0], weight[i][1]

        if j < w:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = max(cost + bag[i - 1][j - w], bag[i - 1][j])
print(bag[n][k])