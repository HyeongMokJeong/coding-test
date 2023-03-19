import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
dic = defaultdict(int)
result = []

for _ in range(n):
    dic[sys.stdin.readline().rstrip()] += 1
for _ in range(m):
    dic[sys.stdin.readline().rstrip()] += 1

for i in dic.keys():
    if dic[i] == 2: result.append(i)

result.sort()
print(len(result))
for i in result: print(i)