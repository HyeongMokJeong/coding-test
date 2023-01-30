n = int(input())
dic = dict()
answer = ""

for _ in range(n):
    target = list(input())
    for i in range(len(target)):
        if (dic.get(i)): dic[i].add(target[i])
        else: dic[i] = set(target[i])

for i in dic.keys():
    if len(dic.get(i)) == 1: answer += list(dic.get(i))[0]
    else: answer += "?"

print(answer)