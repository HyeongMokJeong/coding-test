import sys; input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int, input().split())
    
    time = [0] * n
    count = [0] * n
    score = [[0] * k for _ in range(n)]
    for sec in range(m):
        i, j, s = map(int, input().split())
        score[i - 1][j - 1] = max(score[i - 1][j - 1], s)
        time[i - 1] = sec
        count[i - 1] += 1
    result = []
    for i in range(len(score)):
        result.append([sum(score[i]), count[i], time[i], i])
    result.sort(key=lambda x:(-x[0], x[1], x[2]))
    for i in range(len(result)):
        if result[i][3] == t - 1:
            print(i + 1)
            break