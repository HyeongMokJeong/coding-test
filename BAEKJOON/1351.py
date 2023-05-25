from collections import defaultdict
N, P, Q = map(int, input().split())
dic = defaultdict(int)
dic[0] = 1

def dfs(target):
    if dic[target] != 0: return dic[target]

    dic[target] = dfs(target // P) + dfs(target // Q)
    return dic[target]
print(dfs(N))