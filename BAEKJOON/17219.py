import sys

n, m = map(int, sys.stdin.readline().split())
dic = dict()
for _ in range(n):
    site, password = sys.stdin.readline().split()
    dic[site] = password
for _ in range(m):
    target = sys.stdin.readline().rstrip()
    print(dic[target])