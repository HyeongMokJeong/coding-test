import sys; input = sys.stdin.readline

ary = [int(input()) for _ in range(int(input()))]

stack = []
result = 0
for i in ary:
    while stack and stack[-1] <= i: stack.pop()
    stack.append(i)
    result += len(stack) - 1
print(result) 