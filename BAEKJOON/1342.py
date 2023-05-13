from collections import defaultdict

word = list(input())
dic = defaultdict(int)
for i in word: dic[i] += 1

result = 0
def dfs(target, last):
    global result
    if len(target) == len(word):
        result += 1
        return
    
    for i in dic.keys():
        if dic[i] > 0 and i != last:
            dic[i] -= 1
            dfs(target + i, i)
            dic[i] += 1

for i in dic.keys():
    dic[i] -= 1
    dfs(i, i)
    dic[i] += 1
print(result)