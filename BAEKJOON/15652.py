n, m = map(int, input().split())

def dfs(start):
    global ary
    if len(ary) == m:
        print(" ".join(map(str, ary)))
        return
    for i in range(start, n + 1):
        ary.append(i)
        dfs(i)
        ary.pop()

ary = []
dfs(1)