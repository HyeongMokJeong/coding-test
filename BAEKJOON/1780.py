import sys

n = int(sys.stdin.readline().rstrip())
ary = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
minus, zero, one = 0, 0, 0

def recur(s_idx, s_idy, size):
    global minus, zero, one
    t = ary[s_idx][s_idy]
    
    for i in range(s_idx, s_idx + size):
        for j in range(s_idy, s_idy + size):
            if ary[i][j] != t:
                for a in range(3):
                    for b in range(3):
                        recur(s_idx + a * size // 3, s_idy + b * size // 3, size // 3)
                return
                
    if t == -1: minus += 1
    elif t == 0: zero += 1
    else: one += 1

recur(0, 0, n)
print(minus)
print(zero)
print(one)