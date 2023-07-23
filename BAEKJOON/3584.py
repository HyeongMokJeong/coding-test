import sys; input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    N = int(input().rstrip())
    parent = dict()
    for _ in range(N - 1):
        a, b = map(int, input().split())
        parent[b] = a
    a, b = map(int, input().split())
    
    a_p, b_p = [a], [b]
    while parent.get(a):
        a_p.append(parent[a])
        a = parent[a]
    while parent.get(b):
        b_p.append(parent[b])
        b = parent[b]
    
    a_l, b_l = len(a_p) - 1, len(b_p) - 1
    while a_p[a_l] == b_p[b_l]:
        a_l -= 1
        b_l -= 1
    print(a_p[a_l + 1])