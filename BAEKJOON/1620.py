import sys

n, m = map(int, sys.stdin.readline().split())
dic1, dic2 = dict(), dict()

for i in range(1, n + 1):
    poke = sys.stdin.readline().rstrip()
    dic1[poke] = i
    dic2[i] = poke

for _ in range(m):
    target = sys.stdin.readline().rstrip()
    if str(target).isdigit():
        print(dic2[int(target)])
    else:
        print(dic1[target])