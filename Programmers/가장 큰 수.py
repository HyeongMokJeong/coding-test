num = list(map(str, input().split()))
dic = dict()

for idx, i in enumerate(num):
    if len(i) == 1:
        num[idx] = i * 4
        dic[i * 4] = 1
    else:
        num[idx] = i * 2
        dic[i * 2] = 2

num.sort(reverse=True)
for i in num:
    if dic[i] == 1:
        print(i[0], end='')
    else:
        print(i[:2], end='')