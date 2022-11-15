import sys

n = int(sys.stdin.readline())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num) / n))
print(num[n // 2])

save = []
max_count = 0
count = 0
for i in range(n - 1):
    if num[i] == num[i + 1]:
        count += 1
    else:
        if count > max_count: max_count = count
        save.append((num[i], count))
        count = 0
if count == 0:
    save.append((num[-1], 0))
else:
    if count > max_count: max_count = count
    save.append((num[-1], count))

answer = []
for i in save:
    if i[1] == max_count:
        answer.append(i[0])
if len(answer) == 1:
    print(answer[0])
else: 
    answer.sort()
    print(answer[1])

print(num[-1] - num[0])