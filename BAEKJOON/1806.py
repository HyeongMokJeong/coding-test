import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, s = map(int, input().split())
ary = list(map(int, input().split()))

lp, rp = 0, 0
sums = 0
result = float('inf')

while True:
    if sums >= s:
        result = min(result, rp - lp)
        sums -= ary[lp]
        lp += 1
    elif rp == n: break
    else: 
        sums += ary[rp]
        rp += 1

if result == float('inf'): print(0)
else: print(result)