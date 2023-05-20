n = 3

target = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[0] * n for _ in range(n)]

def run():
    n = 3
    for i in range(n):
        for j in range(n):
            result[i][j] = target[n - j - 1][i] # 핵심 i,j = n - j - 1, i
run()
for i in result:
    print(i)

target2 = ['1', '234', '56789']
result2 = ['' for _ in range(n)]

for idx, i in enumerate(target2):
    for idy, j in enumerate(i):
        t = n - 1 - idx + ((idy + 1) // 2) # 핵심 i =  n - 1 - idx + ((idy + 1) // 2)
        result2[t] = j + result2[t]
print(result2)