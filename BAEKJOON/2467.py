import sys; input = sys.stdin.readline; 
n = int(input().rstrip())
ary = list(map(int, input().split()))

lp, rp = 0, n - 1
gap = abs(ary[lp] + ary[rp])
result_l, result_r = lp, rp

while lp < rp:
    target = ary[lp] + ary[rp]

    if abs(target) < gap:
        gap = abs(target)
        result_l, result_r = lp, rp
        if target == 0: break
    if target < 0: lp += 1
    else: rp -= 1

print(ary[result_l], ary[result_r])