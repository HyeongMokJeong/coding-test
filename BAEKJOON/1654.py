import sys; input = sys.stdin.readline

K, N = map(int,input().split())
ary = [int(input().rstrip()) for _ in range(K)]

def get(m):
    result = 0
    for i in ary: result += i // m
    return result

left, right = 1, max(ary)
while left <= right:
    m = (right + left) // 2
    g = get(m)
    if (g >= N): 
        left = m + 1
    else:
        right = m - 1
print(right)