import sys; input = sys.stdin.readline
N = int(input().rstrip())
a = list(map(int, input().rstrip()))
b = list(map(int, input().rstrip()))

def run(a, b):
    a_copy = a[:]
    count = 0
    for i in range(1, N):
        if a_copy[i - 1] == b[i - 1]: continue

        count += 1
        for j in range(i - 1, i + 2):
            if j < N:
                a_copy[j] =  1 - a_copy[j]
    if a_copy == b: return count
    else: return float('inf')

result = run(a, b)
a[0] = 1 - a[0]
a[1] = 1 - a[1]
result = min(result, run(a, b) + 1)
if result != float('inf'): print(result)
else: print(-1)