target = input()
stack = []
result = 0
temp = ''

for i in target:
    if i == '(':
        stack.append((temp, result - 1))
        result = 0
    elif i == ')':
        n, l = stack.pop()
        result = (int(n) * result) + l
    else:
        result += 1
        temp = i
print(result)