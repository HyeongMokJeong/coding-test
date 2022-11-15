import sys

N, L = map(int, sys.stdin.readline().split())
dep = list(map(int, sys.stdin.readline().split()))
dep.sort()

count = 1
line = dep[0] + L - 0.5
for i in range(1, len(dep)):
    if (dep[i] - dep[i - 1] > L) or (dep[i] > line): 
        count += 1
        line = dep[i] + L - 0.5

print(count)