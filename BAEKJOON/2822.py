import sys

score = []
dic = dict()
result = []
count = 0

for i in range(8):
    n = int(sys.stdin.readline())
    score.append(n)
    dic[n] = i + 1

for i in range(5):
    big = score.index(max(score))
    count += score[big]
    result.append(dic[max(score)])
    score[big] = 0

print(count)
result.sort()
print(*result)