n, a, b = map(int, input().split())
answer = 0

while a != b:
    a -= a // 2
    b -= b // 2
    answer += 1
print(answer)