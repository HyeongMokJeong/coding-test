n = int(input())
result = [[' '] * 2 * n for _ in range(n)]

def star(x, y, size):
    if size == 3:
        result[x][y] = '*'
        result[x + 1][y - 1] = result[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            result[x + 2][y + i] = '*'
    else:
        next = size // 2
        star(x, y, next)
        star(x + next, y - next, next)
        star(x + next, y + next, next)

star(0, n - 1, n)
for i in result: print("".join(i))