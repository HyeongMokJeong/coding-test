n, s = map(int, input().split())
num = list(map(int, input().split()))

result = 0
temp = []

def run(start):
    global result
    if sum(temp) == s and len(temp) != 0:
        result += 1

    for i in range(start, n):
        temp.append(num[i])
        run(i + 1)
        temp.pop()

run(0)
print(result)