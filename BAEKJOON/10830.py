import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def mul(mat1, mat2):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for z in range(n):
                result[i][j] += mat1[i][z] * mat2[z][j] % 1000
    return result

def run(ary, size):
    if size == 1: return ary
    else:
        temp = run(ary, size // 2)
        if size % 2 == 0: return mul(temp, temp)
        else: return mul(mul(temp, temp), ary)
result = run(matrix, b)

for row in result:
    for col in row:
        print(col % 1000, end=" ")
    print()