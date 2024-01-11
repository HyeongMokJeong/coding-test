def solution(answers):
    answer = []
    c = [0, 0, 0 ,0]
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == p1[i % len(p1)]: c[1] += 1
        if answers[i] == p2[i % len(p2)]: c[2] += 1
        if answers[i] == p3[i % len(p3)]: c[3] += 1
    m = max(c)
    for i in range(1, len(c)):
        if c[i] == m: answer.append(i)
    return answer