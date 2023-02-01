n, r, c = map(int, input().split())
answer = 0

while n != 0:
    n -= 1
    if r < 2**(n):
        if c < 2**(n): 
            answer += (2**n) * (2**n) * 0
        else: 
            answer += (2**n) * (2**n) * 1
            c -= 2**n
    else:
        if c < 2**(n): 
            answer += (2**n) * (2**n) * 2
            r -= 2**n
        else: 
            answer += (2**n) * (2**n) * 3
            c -= 2**n
            r -= 2**n

print(answer)