n, m = map(int, input().split())
know = list(map(int, input().split()))
party = [list(map(int, input().split())) for _ in range(m)]
dic = {i : 0 for i in range(1, n + 1)} # 0이면 거짓말 가능, 1이면 불가능
answer = 0

def m(target):
    for i in party:
        if target in i[1:]:
            for j in i[1:]:
                if dic[j] != 1:
                    dic[j] = 1
                    m(j)

if know[0] != 0:
    for i in know[1:]: 
        dic[i] = 1
        m(i)

for i in party:
    flag = True
    for j in i[1:]:
        if dic[j] == 1: 
            flag = False
            break
    if flag: answer += 1
print(answer)