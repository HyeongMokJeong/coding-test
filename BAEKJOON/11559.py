import sys

ary = [list(input()) for _ in range(12)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def down(ary):
    for i in range(len(ary) - 1, -1, 0):
        flag = False
        for j in range(len(i)):
            if ary[i][j] == '.':
                ary[i - 1][j], ary[i][j] = ary[i][j], ary[i - 1][j]
                flag = True
        if not flag: return False

count = 0
clear = []
result = 0

def dfs(x, y, target):
    if (x < 0 or x >= 12 or y < 0 or y >= 6): return
    global count

    if (ary[x][y] == target):
        for i in range(4):
            count += 1
            clear.append((x, y))
            dfs(x + dx[i], y + dy[i], target)
        return  

for i in range(11, -1, -1):
    for j in range(6):
        if (ary[i][j] != '.'):
            dfs(i, j, ary[i][j])
        if count >= 4:
            result += 1
            for i in clear:
                ary[i[0]][i[1]] = '.'
        count = 0
        clear = []
print(result)