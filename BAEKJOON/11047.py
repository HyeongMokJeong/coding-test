import sys

n, k = map(int, sys.stdin.readline().split())
ary = []
for _ in range(n):
    t = int(sys.stdin.readline().rstrip())
    if t <= k: ary.append(t)

count = 0
for i in ary[::-1]:
    count += k // i
    k -= k // i * i
    if k == 0: break
print(count)