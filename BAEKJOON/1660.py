N = int(input())
dp = []

num, idx = 0, 1
while N > num:
    num += (idx * (idx + 1)) // 2
    dp.append(num)
    idx += 1

result = [i for i in range(N + 1)]
for i in range(1, N + 1):
    for n in dp:
        if n == i:
            result[i] = 1
            break
        elif n > i: break
        result[i] = min(result[i], 1 + result[i - n])
print(result[-1])