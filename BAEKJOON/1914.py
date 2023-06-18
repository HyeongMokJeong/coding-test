N = int(input())

def hanoi(n, s, m, e):
    if n == 1: 
        print(s, e)
        return
    
    hanoi(n - 1, s, e, m)
    print(s, e)
    hanoi(n - 1, m, s, e)
print(2 ** N - 1)
if N < 20: hanoi(N, 1, 2, 3)