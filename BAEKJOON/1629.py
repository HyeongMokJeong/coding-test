a, b, c = map(int, input().split())

def run(x, y):
    if y == 1:
        return x % c
    else:
        temp = run(x, y // 2)
        if y % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * x % c

print(run(a, b))