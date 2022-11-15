from itertools import permutations as p

n = int(input())
k = int(input())
num = [str(input()) for _ in range(n)]

print(len(set(''.join(i) for i in p(num, k))))