n, m = map(int, input().split())
lamp = [list(map(int,list(input()))) for _ in range(n)]
k = int(input())
answer = 0

posible = []
for idx, i in enumerate(lamp):
    c = i.count(0)
    if c > k or (c % 2 == 0 and k % 2 != 0) or (c % 2 != 0 and k % 2 == 0): continue
    posible.append(idx)

for idx in posible:
    c = 0
    for j in lamp:
        if lamp[idx] == j: c += 1
    answer = max(answer, c)
print(answer)