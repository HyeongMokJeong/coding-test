def solution(gems):
    answer = [0, 100001]
    n = len(gems)
    p1, p2 = 0, 0

    size = len(set(gems))
    dic = dict({gems[0] : 1})

    while p1 < n and p2 < n:
        if len(dic) == size:
            if answer[1] - answer[0] > p2 - p1:
                answer = [p1 + 1, p2 + 1]
            else:
                dic[gems[p1]] -= 1
                if not dic[gems[p1]]: dic.pop(gems[p1])
                p1 += 1
        else: 
            p2 += 1
            if p2 == n: break
            if dic.get(gems[p2]): dic[gems[p2]] += 1
            else: dic[gems[p2]] = 1
    return answer