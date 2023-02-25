from collections import defaultdict

word = list(input())
word.sort()
dic = defaultdict(int)
for i in word: dic[i] += 1
side, mid = "", ""

while (len(side) * 2) + len(mid) < len(word):
    for i in dic.keys():
        if dic[i] == 1: 
            mid += i
            dic[i] = 0
        else:
            side += i * (dic[i] // 2)
            if dic[i] % 2 == 0:
                dic[i] = 0
            else:
                dic[i] = 1

if len(mid) > 1:
    print("I'm Sorry Hansoo")
else:
    print(side + mid + side[::-1])