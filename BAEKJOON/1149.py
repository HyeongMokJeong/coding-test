import sys

n = int(input())
ary = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    ary[i][0] = min(ary[i - 1][1], ary[i - 1][2]) + ary[i][0]
    ary[i][1] = min(ary[i - 1][0], ary[i - 1][2]) + ary[i][1]
    ary[i][2] = min(ary[i - 1][0], ary[i - 1][1]) + ary[i][2]
print(min(ary[n - 1]))