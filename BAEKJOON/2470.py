import sys; input = sys.stdin.readline
N = int(input().rstrip())
ary = list(map(int, input().split()))
ary.sort()

lp, rp = 0, N - 1
result = [lp, rp]
gap = float('inf')
while lp < rp:
    temp = ary[rp] + ary[lp]
    if abs(temp) < gap: 
        result = [lp, rp]
        gap = abs(temp)
        if temp == 0: break
    if temp < 0: lp += 1
    else: rp -= 1 
print(ary[result[0]], ary[result[1]])