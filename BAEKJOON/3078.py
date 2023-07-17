import sys; input = sys.stdin.readline
from collections import defaultdict

N, K = map(int, input().split())
dic = defaultdict(int)
ary = [len(input().rstrip()) for _ in range(N)]

result = 0
for i in range(N):
    if i > K: dic[ary[i - K - 1]] -= 1
    result += dic[ary[i]]
    dic[ary[i]] += 1

print(result)