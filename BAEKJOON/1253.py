import sys; input = sys.stdin.readline
N = int(input().rstrip())
ary = sorted(list(map(int, input().split())))

result = 0
for i in range(N):
    temp = ary[:i] + ary[i + 1:]
    lp, rp = 0, len(temp) - 1
    while lp < rp:
        t = temp[lp] + temp[rp]
        if t == ary[i]: 
            result += 1
            break
        elif t < ary[i]: lp += 1
        else: rp -= 1
print(result)