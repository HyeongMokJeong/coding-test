import sys

n = int(sys.stdin.readline().rstrip())
ary = []

for _ in range(n):
    ary.append(tuple(map(int, sys.stdin.readline().split())))

ary.sort(key=lambda x:(x[1], x[0]))

count = end = 0
for s, e in ary:
    if s >= end:
        count += 1
        end = e

print(count)