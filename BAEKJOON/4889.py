import sys; input = sys.stdin.readline

c = 1
while True:
    ary = list(input().rstrip())
    if '-' in ary: break

    count = 0
    stack = []
    for i in ary:
        if i == '{': stack.append(i)
        else:
            if stack: stack.pop()
            else:
                count += 1
                stack.append("{")

    print(f'{c}. {count + len(stack) // 2}')
    c += 1