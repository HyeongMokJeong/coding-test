import sys

N, M = map(int, sys.stdin.readline().split())
nums = []
target = []
dic = {}

for _ in range(N): 
    n = nums.append(int(sys.stdin.readline()))
nums.sort()

for _ in range(M): 
    n = target.append(int(sys.stdin.readline()))

for idx, i in enumerate(nums):
    if dic.get(i) == None: dic[i] = idx

for i in target:
    if dic.get(i) == None: print(-1)
    else: print(dic.get(i))