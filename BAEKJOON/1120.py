a, b = map(list, input().split())
gap = len(b) - len(a)
result = float('inf')

for i in range(gap + 1):
    count = 0
    for idx, j in enumerate(range(i, i + len(a))):
        if a[idx] != b[j]: count += 1
    result = min(result, count)
print(result)