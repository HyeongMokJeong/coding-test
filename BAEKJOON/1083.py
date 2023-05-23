import sys; input = sys.stdin.readline

N = int(input().rstrip())
ary = list(map(int, input().split()))
S = int(input().rstrip())

for i in range(N):
    big = max(ary[i:min(N, i + S + 1)])
    idx = ary.index(big)

    for j in range(idx, i, -1):
        ary[j], ary[j - 1] = ary[j - 1], ary[j]
    S -= idx - i
    if S <= 0: break
print(*ary)