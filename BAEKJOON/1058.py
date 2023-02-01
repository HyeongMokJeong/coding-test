from collections import defaultdict

n = int(input())
ary = [list(input()) for _ in range(n)]
answer = 0
dic = defaultdict(list)

for idx, i in enumerate(ary):
    for idy, j in enumerate(i):
        if j == 'Y': dic[idx].append(idy)

for i in dic:
    temp = set()
    for j in dic[i]:
        temp.add(j)
        temp = set(dic[j]) | temp
    answer = max(answer, len(temp) - 1)
print(answer)