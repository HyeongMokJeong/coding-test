n = int(input())
dic = dict()
answer = []

ary = list(map(int, input().split()))
new = sorted(ary)

for idx, i in enumerate(new):
    if dic.get(i): dic[i][1].append(idx)
    else: dic[i] = [0, [idx]]

for i in ary:
    idx = dic[i][0]
    num = dic[i][1]
    answer.append(num[idx])
    dic[i][0] += 1

print(*answer)