import sys; input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ary = [input().rstrip() for _ in range(n)]
    ary.sort()

    for i in range(n - 1):
        if ary[i + 1].startswith(ary[i]):
            print("NO")
            break
    else: print("YES")