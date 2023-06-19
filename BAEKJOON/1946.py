import sys; input = sys.stdin.readline
T = int(input().rstrip())

for _ in range(T):
    N = int(input().strip())
    ary = []
    for _ in range(N): ary.append(list(map(int, input().split()))) 
    ary.sort(key=lambda x:x[0])

    result, t = 1, ary[0][1]
    for i in range(1, N):
        if ary[i][1] < t:
            t = ary[i][1] 
            result += 1
    print(result)