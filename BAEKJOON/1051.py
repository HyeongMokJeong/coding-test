n, m = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(n)]

size = n
while (size > 0):
    for i in range(n):
        for j in range(m):
            one = i + size - 1
            two = j + size - 1
            if one < n and one >= 0 and two < m and two >= 0:
                if matrix[one][j] == matrix[i][two] == matrix[i][j] == matrix[one][two]:
                    print(size ** 2)
                    exit(0)
    size -= 1
print(size)