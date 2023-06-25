import sys; input = sys.stdin.readline

N = int(input().rstrip())
ary = [list(map(int, input().split())) for _ in range(N)]
ary.sort(key=lambda x:x[0])
s, b = ary[0][0], ary[0][1]

result = 0
for x, y in ary[1:]:
    if x <= b:
        if y > b: b = y
    else: 
        result += b - s
        s, b = x, y
result += b - s
print(result)