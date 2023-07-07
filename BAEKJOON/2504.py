ary = list(input())

stack = []
result = 0 
temp = 1

for i in range(len(ary)):

    if ary[i] == "(":
        stack.append(ary[i])
        temp *= 2

    elif ary[i] == "[":
        stack.append(ary[i])
        temp *= 3

    elif ary[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        if ary[i -  1] == "(":
            result += temp
        stack.pop()
        temp //= 2
    else:
        if not stack or stack[-1] == "(":
            result = 0
            break
        if ary[i - 1] == "[":
            result += temp
        stack.pop()
        temp //= 3
if stack: 
    print(0)
else: 
    print(result)