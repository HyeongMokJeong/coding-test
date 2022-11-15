def solution(n, info):
    apeach_score = sum([10 - i for i in range(10) if info[i]])
    # 위에서 어피치의 점수를 비교없이 계산했으므로, 2배를 해줌
    score = [(10-i) * 2 if info[i] else 10-i for i in range(11)]
    answer = []

    q = [[0]]
    if n >= info[0] + 1: q.append([info[0] + 1])

    while q:
        t = q.pop(0)
        if sum(t) == n or len(t) == 11:
            while (len(t) != 11): t.append(0)
            if sum(t) < n: t[-1] = n - sum(t)
            new = sum([score[i] for i in range(len(t)) if t[i]])
            old = sum([score[i] for i in range(len(answer)) if answer[i]])
            if new > apeach_score and new >= old: answer = t
        elif sum(t) + info[len(t)] + 1 <= n:
            q.append(t + [info[len(t)] + 1])
            q.append(t + [0])
        else:
            q.append(t + [0])
    return answer if answer else [-1]

print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))