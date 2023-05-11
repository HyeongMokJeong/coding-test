import sys; input = sys.stdin.readline
from collections import defaultdict

n = int(input().rstrip())
ary = [list(input().rstrip()) for _ in range(n)]
dic = defaultdict(int)
m = 0
for i in ary:
    if len(i) > m: m = len(i)
for i in range(len(ary)):
    if len(ary[i]) < m:
        ary[i] = ([0] * (m - len(ary[i]))) + ary[i]

for i in range(m):
    for j in range(n):
        if ary[j][i] == 0: continue
        dic[ary[j][i]] += 10 ** (m - i - 1)
v = [i for i in dic.values()]
v.sort(reverse=True)

target, result = 9, 0
for i in v:
    result += target * i
    target -= 1
print(result)