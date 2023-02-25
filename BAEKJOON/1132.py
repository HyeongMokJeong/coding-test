import sys

n = int(input())
num = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ary = [[0, False, chr(i + 65)] for i in range(10)]
result = 0

for i in num:
    ary[ord(i[0]) - 65][1] = True
    for idx, j in enumerate(i[::-1]):
        ary[ord(j) - 65][0] += 10 ** idx
ary.sort(reverse=True)

if ary[-1][1]:
    for idx, i in enumerate(ary[::-1]):
        if not i[1]:
            ary.append(ary.pop(len(ary) - 1 - idx))
            break

for i in range(len(ary)):
    result += ary[len(ary) - 1 - i][0] * i

print(result)
