n, m = map(int, input().split())
old = [list(map(int, list(input()))) for _ in range(n)]
new = [list(map(int, list(input()))) for _ in range(n)]
answer = 0

def reverse(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            old[i][j] = 0 if old[i][j] != 0 else 1

if n < 3 or m < 3:
    if old == new: print(0)
    else: print(-1)
    exit(0)

for i in range(n - 2):
    for j in range(m - 2):
        if old[i][j] != new[i][j]:
            reverse(i, j)
            answer += 1
if old == new: print(answer)
else: print(-1)