import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    answer = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
    print(answer)