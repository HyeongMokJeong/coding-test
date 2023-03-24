import sys

n = int(sys.stdin.readline().rstrip())
ary = list(map(int, sys.stdin.readline().split()))
ary.sort()

for i in range(1, n): ary[i] += ary[i - 1]
print(sum(ary))