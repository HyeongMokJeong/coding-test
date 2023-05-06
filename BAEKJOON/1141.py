import sys; input = sys.stdin.readline

n = int(input().rstrip())
words = [input().rstrip() for _ in range(n)]
words.sort(key=lambda x:len(x))

result = 0
for i in range(n):
    flag = True
    for j in range(i + 1, n):
        if words[j].startswith(words[i]):
            flag = False
            break
    if flag: result += 1
print(result)