c = int(input())
answer = []

for _ in range(c):
    n, m = map(int, input().split())
    matrix = [list(input()) for _ in range(n)]

    start = 0
    start2 = 0
    for i in range(0, m, 2):
        for j in range(n):
            if matrix[j][i] == '.': start += 1
    for i in range(1, m, 2):
        for j in range(n):
            if matrix[j][i] == '.': start2 += 1
    
    answer.append(max(start, start2))

for i in answer: print(i)