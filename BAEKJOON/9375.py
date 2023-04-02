import sys
from collections import defaultdict

case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    dic = defaultdict(int)
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        target, ty = sys.stdin.readline().split()
        dic[ty] += 1
    
    result = 1
    for i in dic.keys():
        result *= dic[i] + 1 
    print(result - 1)