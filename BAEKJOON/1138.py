n = int(input())
line = list(map(int, input().split()))
result = [0] * n
for idx, i in enumerate(line, start=1):
    count = 0
    for j in range(n):
        if count == i and result[j] == 0:
            result[j] = idx
            break
        if (result[j] == 0): count += 1
print(* result)