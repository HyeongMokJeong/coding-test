import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

dic = {i : 1 for i in num}

for i in target:
    if dic.get(i) == None: print(0)
    else: print(dic[i])