s, n, k, r1, r2, c1, c2 = map(int, input().split())

def recur(size, x, y):
    b = size // n
    if size == 1:
        return 0
    if b * (n - k) // 2 <= x < b * (n + k )// 2 and b * (n - k) // 2 <= y < b * (n + k) // 2:
        return 1
    return recur(size // n, x % b, y % b)

start_size = n ** s
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(recur(start_size, i, j), end='')
    print()