target = input()
stack = []
one, two = ('+', '-'), ('*', '/')
result = ""

for i in target:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i in one:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i in two:
            while stack and stack[-1] in two:
                result += stack.pop()
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack: result += stack.pop()
print(result)
