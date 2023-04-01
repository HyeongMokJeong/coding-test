import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

count, i, result = 0, 1, 0
while i < m - 1:
    if s[i - 1] == 'I' and s[i] == 'O' and s[i + 1] == 'I':
        i += 2
        count += 1
        if count == n:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0
print(result)