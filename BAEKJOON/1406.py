import sys; input = sys.stdin.readline
from collections import deque

ary = list(input().rstrip())
stack, t_stack = [], deque()
for i in ary: stack.append(i)
for i in range(int(input().rstrip())):
    target = input().split()
    if len(target) == 2:
        stack.append(target[1])
    else:
        if target[0] == 'L':
            if stack: t_stack.appendleft(stack.pop())
        elif target[0] == 'D':
            if t_stack: stack.append(t_stack.popleft())
        else:
            if stack: stack.pop()
print("".join(stack), "".join(t_stack), sep="")
  