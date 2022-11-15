import sys

n, l = map(int, sys.stdin.readline().split())
water = list(map(int, sys.stdin.readline().split()))
water.sort()
count = 1
pivot = water[0]

for i in range(1, len(water)):
    if ((water[i] + 0.5) - (pivot - 0.5) > l):
        count += 1
        pivot = water[i]

print(count)