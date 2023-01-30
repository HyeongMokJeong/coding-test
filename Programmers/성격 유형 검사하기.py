def solution(survey, choices):
    answer = ''
    t = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    dic = dict()
    for a, b in survey:
        dic[a], dic[b] = 0, 0

    for idx, i in enumerate(survey):
        score = choices[idx]

        if 0 < score < 4:
            dic[i[0]] += 4 - score
        elif 4 < score < 8:
            dic[i[1]] += score - 4

    for i in t:
        if dic.get(i[0]) == None: 
            answer += i[0]
            continue
        if dic[i[0]] >= dic[i[1]]:
            answer += i[0]
        else:
            answer += i[1]

    return answer

print(solution(["TR", "RT", "TR"], [7, 1, 3]))