import sys

def hanoi(start, mid, end, n):
    if (n == 1):
        print(f"{start} {end}")
        return
    
    hanoi(start, end, mid, n - 1)
    print(f"{start} {end}")
    hanoi(mid, start, end, n - 1)


n = int(sys.stdin.readline())
print(2**n - 1)
hanoi(1, 2, 3, n)