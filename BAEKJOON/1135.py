from collections import defaultdict

n = int(input())
tree = list(map(int, input().split()))
dic = defaultdict(list)

for idx, i in enumerate(tree[1:]): dic[i].append(idx + 1)
count = [0 for _ in range(n)]

def dfs(target):
    global count
    temp = []
    if len(dic[target]) == 0: return
    else:
        for i in dic[target]:
            dfs(i)
            temp.append(count[i])
        
        temp.sort(reverse=True)
        temp = [temp[i] + i + 1 for i in range(len(temp))]
        count[target] = max(temp)
dfs(0)
print(count[0])