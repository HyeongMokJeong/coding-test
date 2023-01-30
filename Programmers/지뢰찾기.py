가로, 세로 = map(int, input().split())
matrix = [list(input()) for _ in range(세로)]
answer = []

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

def find(x, y):
    count = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 세로 and ny >= 0 and ny < 가로:
            if matrix[nx][ny] == '*': count += 1
    return count

for idx, i in enumerate(matrix):
    save = []
    for idy, j in enumerate(i):
        if j == '*': 
            save.append(j)
            continue
        save.append(find(idx, idy))
    answer.append(save)

for i in answer: 
    for j in i: print(j, end="")
    print()