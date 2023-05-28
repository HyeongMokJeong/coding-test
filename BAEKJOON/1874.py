import sys; input = sys.stdin.readline
n = int(input().rstrip())
stack, result = [], ""

count = 1
for _ in range(n):
    target = int(input().rstrip())
    while count <= target:
        stack.append(count)
        result += "+"
        count += 1
    if stack[-1] == target:
        stack.pop()
        result += "-"
    else: 
        print("NO")
        break
else: 
    for i in result: print(i)
