n, m = map(int, input().split())
lamp = [list(map(int,list(input()))) for _ in range(n)]
k = int(input())
answer = 0

al = [i for i in range(m)]
def dfs(visited, count):
    global answer
    if count == 0 or visited == al:
        c = 0
        for i in lamp:
            if 0 in i: continue
            c += 1
        answer = max(answer, c)
    for i in range(m):
        if i in visited: continue
        for j in range(n): lamp[j][i] = 0 if lamp[j][i] != 0 else 1
        visited.append(i)
        dfs(visited, count - 1)
        for j in range(n): lamp[j][i] = 0 if lamp[j][i] != 0 else 1
        visited = visited[:-1]

for i in range(m):
    dfs([], k)
print(answer)