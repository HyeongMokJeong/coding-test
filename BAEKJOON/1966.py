import sys

case = int(sys.stdin.readline())
result = []

for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    idx = [0] * n
    idx[m] = 1
    num = list(map(int, sys.stdin.readline().split()))
    count = 0

    while True:
        if num[0] == max(num):
            count += 1
            if (idx[0] == 1):
                result.append(count)
                break
            num[0] = 0
        num.append(num.pop(0))
        idx.append(idx.pop(0))

for i in result: print(i)