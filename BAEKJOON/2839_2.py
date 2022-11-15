import sys

n = int(sys.stdin.readline())
flag = False
for i in range(n // 5, -1, -1):
    if (n - (5 * i)) % 3 == 0: 
        print(i + (n - (5 * i)) // 3)
        flag = True
        break

if not flag: print(-1)