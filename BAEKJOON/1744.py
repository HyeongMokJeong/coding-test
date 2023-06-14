import sys; input = sys.stdin.readline
N = int(input().rstrip())
par, mar = [], []
result = 0
for _ in range(N):
    n = int(input().rstrip())
    if n == 1: result += 1
    elif n > 0: par.append(n)
    else: mar.append(n)
par.sort()
mar.sort(reverse=True)
while par:
    if len(par) == 1: result += par.pop()
    else: result += par.pop() * par.pop()
while mar:
    if len(mar) == 1: result += mar.pop()
    else: result += mar.pop() * mar.pop()
print(result)