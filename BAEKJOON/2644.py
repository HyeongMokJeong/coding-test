import sys; input = sys.stdin.readline

n = int(input().rstrip())
a, b = map(int, input().split())
m = int(input().rstrip())

dic = dict()
for _ in range(m):
    x, y = map(int, input().split())
    dic[y] = x

p_a, p_b = [a], [b]
while dic.get(a):
    p_a.append(dic[a])
    a = dic[a]
while dic.get(b):
    p_b.append(dic[b])
    b = dic[b]

if p_a[-1] != p_b[-1]:
    print(-1)
    exit()
ta, tb = len(p_a) - 1, len(p_b) - 1
while p_a[ta] == p_b[tb]:
    ta -= 1
    tb -= 1
print(ta + tb + 2)