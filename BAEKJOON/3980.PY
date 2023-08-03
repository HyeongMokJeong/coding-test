import sys; input = sys.stdin.readline

def bt(n): # n번째 선수
    global result
    if n == 11:
        result = max(result, sum(visited))
        return
    
    for i in range(11):
        if ary[n][i] and not visited[i]:
            visited[i] = ary[n][i]
            bt(n + 1)
            visited[i] = 0

for _ in range(int(input())):
    ary = [list(map(int, input().split())) for _ in range(11)]
    result = 0
    visited = [0] * 11

    bt(0)
    print(result)