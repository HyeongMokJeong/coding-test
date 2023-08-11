import sys; input = sys.stdin.readline
from collections import defaultdict

dic = defaultdict(int)
count = 0
while True:
    tree = input().rstrip()
    if not tree: break
    count += 1
    dic[tree] += 1

keys = sorted(list(dic.keys()))
for i in keys: print(f'{i} {100 * dic[i] / count:.4f}')