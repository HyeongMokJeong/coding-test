target = input()
boom = input()
stack = []

idx = 0
for i in target:
    stack.append(i)
    if ''.join(stack[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()
print(''.join(stack) if len(stack) != 0 else "FRULA")