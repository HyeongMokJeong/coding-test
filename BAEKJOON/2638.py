import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
ary = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
def getAir(x, y):
    ary[x][y] = -1
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == 0 and not visited[nx][ny]:
            visited[nx][ny] = 1
            getAir(nx, ny)
            visited[nx][ny] = 0

def isEnd():
    for i in range(n):
        for j in range(m):
            if ary[i][j] == 1: return False
    return True

def check(x, y):
    count = 0
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < n and 0 <= ny < m and ary[nx][ny] == -1: count += 1
    if count >= 2: 
        ary[x][y] = 0
        return True
    return False
            
result = 0
while not isEnd():
    getAir(0, 0)
    melt = []
    for i in range(n):
        for j in range(m):
            if ary[i][j] == 1:
                if check(i, j): melt.append((i, j))
    for x, y in melt:
        getAir(x, y)
    result += 1
        
print(result)