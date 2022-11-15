import sys

n = int(sys.stdin.readline())
num = []
dic = {i : 0 for i in range(-4000, 4001)}
for _ in range(n): 
    dic[int(sys.stdin.readline())] += 1

result = []

for i in dic.keys():
    for j in range(dic[i]):
        result.append(i)

big = max(dic.values())
big_list = [key[0] for key in dic.items() if key[1] == big]

print(round(sum(result) / n))
print(result[len(result) // 2])
print(big_list[0] if len(big_list) == 1 else big_list[1])
print(result[-1] - result[0])