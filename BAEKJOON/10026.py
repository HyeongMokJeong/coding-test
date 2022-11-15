import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(input().strip()) for i in range(n)]
visited = [[False] * n for i in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]

def rgb(x, y):
    visited[x][y] = True
    current_color = matrix[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < n) and (0<= ny < n):
            if visited[nx][ny] == False:
                if matrix[nx][ny] == current_color:
                    rgb(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rgb(i, j)
            three_cnt += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

visited = [[False] * n for i in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rgb(i, j)
            two_cnt += 1

print(three_cnt, two_cnt)