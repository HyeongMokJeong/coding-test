import sys; input = sys.stdin.readline

N = int(input().rstrip())
ary = list(map(int, input().split()))
stack, result = [], [0] * N

for i in range(N):
    while stack:
        if stack[-1][0] < ary[i]: stack.pop()
        else:
            result[i] = stack[-1][1] + 1
            break
    stack.append((ary[i], i))
print(*result)