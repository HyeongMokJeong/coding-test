import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1), (x - 1, y - 1)]:
        if 0 <= nx < h and 0 <= ny < w and ary[nx][ny]:
            ary[nx][ny] = 0
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if not w and not h: break
    ary = [list(map(int, input().split())) for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if ary[i][j]:
                dfs(i, j)
                result += 1
    print(result)