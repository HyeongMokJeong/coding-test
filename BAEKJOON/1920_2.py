import sys

dic = dict()
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
for i in num: dic[i] = 1

m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
for i in target: print(dic[i] if dic.get(i) != None else 0)