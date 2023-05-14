import sys; input = sys.stdin.readline

n, m = map(int, input().split())
ary = list(map(int, input().split()))
ma, left, right = 0, [], []
for i in ary:
    if i > 0: right.append(i)
    else: left.append(i)
    if abs(i) > abs(ma): ma = abs(i)
left.sort()
right.sort(reverse=True)

result = 0
for i in range(0, len(left), m): result += -left[i]
for i in range(0, len(right), m): result += right[i]
print((result - ma) * 2 + ma)