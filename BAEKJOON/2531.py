import sys; input = sys.stdin.readline

N, d, k, c = map(int, input().split())
ary = [int(input().rstrip()) for _ in range(N)]
lp, rp = 0, 0
result = 0

while lp != N:
    rp = lp + k
    case = set()
    cou = True 
    for i in range(lp, rp):
        i %= N
        case.add(ary[i])
        if ary[i] == c: cou = False
    cnt = len(case)
    if cou: cnt += 1
    result = max(result, cnt)
    lp += 1
print(result)