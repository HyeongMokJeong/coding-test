import sys; input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
ary = list(map(int, input().split()))

pic, score = [], []
for i in range(M):
    if ary[i] in pic:
        for j in range(len(pic)):
            if ary[i] == pic[j]: score[j] += 1
    else:
        if len(pic) >= N:
            for j in range(N):
                if score[j] == min(score):
                    pic.pop(j)
                    score.pop(j)
                    break
        pic.append(ary[i])
        score.append(1)
pic.sort()
print(*pic)