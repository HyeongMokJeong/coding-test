import sys

n, m = map(int, sys.stdin.readline().split())
num = []
q = []
dic = dict()

for _ in range(n): 
    num.append(int(sys.stdin.readline()))
num.sort()

for _ in range(m):
    q.append(int(sys.stdin.readline()))

for i in range(len(num)):
    if dic.get(num[i]) == None: dic[num[i]] = i

for i in q:
    print(-1 if dic.get(i) == None else dic[i])