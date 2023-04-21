import sys; input=sys.stdin.readline

a = [""] + list(input().rstrip())
b = [""] + list(input().rstrip())
temp = [[""] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            temp[i][j] = temp[i - 1][j - 1] + a[i]
        else:
            if len(temp[i - 1][j]) >= len(temp[i][j - 1]):
                temp[i][j] = temp[i - 1][j]
            else:
                temp[i][j] = temp[i][j - 1]
result = temp[-1][-1]
print(len(result))
print(result)