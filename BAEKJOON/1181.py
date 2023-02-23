import sys
from collections import defaultdict

n = int(input())
dic = defaultdict(set)
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    dic[len(word)].add(word)
# words.sort(key=lambda x: (len(x), x))
for i in sorted(dic.keys()):
    for j in sorted(dic[i]):
        print(j)