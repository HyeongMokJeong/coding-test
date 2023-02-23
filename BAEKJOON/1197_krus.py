import sys

v, e = map(int, input().split())
edge = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(e)]
edge.sort(key=lambda x:x[2])
dic = [i for i in range(v + 1)]
result = 0

def find(node):
    if node != dic[node]:
        dic[node] = find(dic[node])
    return dic[node]

for a, b, w in edge:
    ar = find(a)
    br = find(b)
    if ar != br:
        dic[br] = ar
        result += w

print(result)