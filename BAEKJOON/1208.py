import sys
from itertools import combinations
from collections import defaultdict

n, s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

l = n // 2
r = n - l
left, right = [], []
result = 0
dic = defaultdict(int)

for i in range(l + 1):
    for j in combinations(num[:l], i):
        left.append(j)
left = list(map(lambda x:sum(x), left))
for i in range(r + 1):
    for j in combinations(num[l:], i):
        right.append(j)
right = list(map(lambda x:sum(x), right))
for i in right: dic[i] += 1

for i in left:
    target = s - i
    if dic.get(target): result += dic[target]
    
print(result if s != 0 else result - 1)