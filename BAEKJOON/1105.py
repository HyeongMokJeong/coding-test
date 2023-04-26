L, R = input().split()
if len(L) != len(R): print(0)
else:
    result = 0
    for i in range(len(R)):
        if L[i] == R[i] and L[i] == '8':
            result += 1
        elif L[i] != R[i]: break
    print(result)