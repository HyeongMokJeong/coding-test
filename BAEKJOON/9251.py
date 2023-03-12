import sys

a, b = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
temp = [0] * len(b)

for i in range(len(a)):
    count = 0
    for j in range(len(b)):
        if count < temp[j]:
            count = temp[j]
        elif a[i] == b[j]:
            temp[j] = count + 1
print(max(temp))