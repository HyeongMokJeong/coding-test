import sys
input = sys.stdin.readline

n = int(input())
ary = [list(map(int, input().split())) for _ in range(n)]
result = 0

def dfs(x, y, t):
    global result
    if x == n - 1 and y == n - 1: 
        result += 1
        return
    
    if x + 1 < n and y + 1 < n:
        if not ary[x + 1][y + 1] and not ary[x + 1][y] and not ary[x][y + 1]:
            dfs(x + 1, y + 1, 2)
    
    if t == 0 or t == 2:
        if y + 1 < n and not ary[x][y + 1]:
            dfs(x, y + 1, 0)
    
    if t == 1 or t == 2:
        if x + 1 < n and not ary[x + 1][y]:
            dfs(x + 1, y, 1)
    
dfs(0, 1, 0)
print(result)