import sys; input = sys.stdin.readline

N, H = map(int, input().split())
# 종유석(->), 석순(<-)
top, bottom = [0] * (H + 1), [0] * (H + 1)

for i in range(N):
    l = int(input().rstrip())
    if i % 2 == 1: top[l] += 1
    else: bottom[H - l + 1] += 1

for i in range(H - 1, 0, - 1): top[i] += top[i + 1]
for i in range(1, H + 1): bottom[i] += bottom[i - 1]
result, count = float('inf'), 1
for i in range(1, H + 1):
    t = top[i] + bottom[i]
    if t < result:
        result = t
        count = 1
    elif t == result: count += 1
print(result, count)