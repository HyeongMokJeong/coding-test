n = int(input())
leng = len(str(n)) * 2
m = int(input())
if m != 0: b = list(map(int, input().split()))
else: b = list()
num = [i for i in range(10) if i not in b]

result = 0

gap = float("inf")

def dfs(number, i):
    global n, result, gap, leng
    if i > leng:
        if len(str(number)) == leng and abs(number - n) < gap:
            gap = abs(number - n)
            result = leng + gap
        return

    for a in num:
        n_number = number + a * (10 ** (leng - i))
        dfs(n_number, i + 1)

for i in num:
    dfs(i * (10 ** (leng - 1)), 2)

print(min(abs(100 - n), result))