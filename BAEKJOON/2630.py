import sys

n = int(sys.stdin.readline().rstrip())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white, blue = 0, 0

def recursion(x, y, size):
    global white, blue

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[x][y] != paper[i][j]:
                recursion(x, y, size // 2)
                recursion(x, y + size // 2, size // 2)
                recursion(x + size // 2, y, size // 2)
                recursion(x + size // 2, y + size // 2, size // 2)
                return

    if paper[x][y] == 0: white += 1
    else: blue += 1

recursion(0, 0, n)
print(white)
print(blue)