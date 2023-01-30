n, m = map(int, input().split())
min_six, min_one = 1000, 1000

for i in range(m):
    a, b = map(int, input().split())
    if a < min_six: min_six = a
    if b < min_one: min_one = b

case1 = ((n // 6) + 1) * min_six
case2 = (n // 6) * min_six + (n - (n // 6) * 6) * min_one
case3 = min_one * n
print(min(case1, case2, case3))