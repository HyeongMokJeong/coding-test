n = int(input())
result = set()
temp = list()

def dfs():
    global result, temp
    if len(temp) > 0:
        result.add(int("".join(map(str, temp))))
    
    for i in range(0, 10):
        if len(temp) == 0 or i < temp[-1]:
            temp.append(i)
            dfs()
            temp.pop()

dfs()
result = sorted(list(result))
if n <= len(result): print(result[n - 1])
else: print(-1)