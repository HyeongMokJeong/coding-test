G = int(input())

l, r = 1, 1
result = []

while True:
    gap = r ** 2 - l ** 2
    if r - l == 1 and gap > G: break

    if gap > G: l += 1
    elif gap < G: r += 1
    else:
        result.append(r)
        r += 1

if result:
    for i in result: print(i)
else: print(-1)