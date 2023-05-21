import sys; input = sys.stdin.readline

N, M = map(int, input().split())
ary = [list(input().rstrip()) for _ in range(N)]

result = -1
for i in range(N):
    for j in range(M):
        for k in range(-N, N):
            for m in range(-M, M):
                if k == 0 and m == 0: continue
                temp = ''
                x, y = i, j
                while 0 <= x < N and 0 <= y < M:
                    temp = temp + ary[x][y]
                    if int(temp) == int(int(temp) ** 0.5) ** 2: result = max(result, int(temp))
                    x += k
                    y += m
print(result)