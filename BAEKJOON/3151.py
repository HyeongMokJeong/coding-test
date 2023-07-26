import sys; input = sys.stdin.readline

n = int(input().rstrip())
ary = list(map(int, input().split()))
ary.sort()

result = 0
for i in range(n - 2):
    lp, rp = i + 1, n - 1
    g = -ary[i]
    mx_idx = n
    while lp < rp:
        t = ary[lp] + ary[rp]
        if t < g: lp += 1
        elif t > g: rp -= 1
        else:
            if ary[lp] == ary[rp]: result += rp - lp
            else:
                if mx_idx > rp:
                    mx_idx = rp
                    while mx_idx >= 0 and ary[mx_idx - 1] == ary[rp]: mx_idx -= 1
                result += rp - mx_idx + 1
            lp += 1
print(result)