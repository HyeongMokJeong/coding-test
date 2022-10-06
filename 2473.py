import sys

all = int(input())
inp = sorted(list(map(int, input().split())))
allsum = sys.maxsize

for i in range(all - 2):
    start = inp[i]
    left = i + 1
    right = all - 1
    while left < right:
        data = start + inp[left] + inp[right]
        if (allsum > abs(data)):
            allsum = abs(data)
            answer = [start, inp[left], inp[right]]
        
        if (data) < 0:
            left += 1
        elif (data) > 0:
            right -= 1
        else:
            break

print(*answer)