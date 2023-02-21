n, m = map(int, input().split())

#최대공약수를 구하는 유클리드 호제법
def gcd(a, b):
    if (a % b == 0):
        return b
    return gcd(b, a % b)

print(m - gcd(n, m))