import sys

n = int(sys.stdin.readline())
flag = False

five = n // 5 # 3
for i in range(five, -1, -1):
    if ((n - i * 5) % 3 == 0):
        print(i + ((n - i * 5) // 3))
        flag = True
        break

if not flag: print(-1)