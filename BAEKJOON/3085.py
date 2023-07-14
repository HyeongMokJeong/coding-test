import sys; input = sys.stdin.readline

N = int(input().rstrip())
ary = [list(input().rstrip()) for _ in range(N)]

def check():
    result = 1
    for i in range(N):
        # row 
        temp = 1
        for j in range(1, N): 
            if ary[i][j] == ary[i][j - 1]: temp += 1
            else: temp = 1
            result = max(result, temp)

        # col
        temp = 1
        for j in range(1, N):
            if ary[j][i] == ary[j - 1][i]: temp += 1
            else: temp = 1
            result = max(result, temp)
    if result == N:
        print(N)
        exit()
    return result

result = check()
for i in range(N):
    for j in range(N):
        for nx, ny in [(i + 1, j), (i, j + 1)]:
            if nx < N and ny < N and ary[i][j] != ary[nx][ny]:
                ary[i][j], ary[nx][ny] = ary[nx][ny], ary[i][j]
                result = max(result, check())
                ary[nx][ny], ary[i][j] = ary[i][j], ary[nx][ny]
print(result)