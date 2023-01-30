def solution(info, query):
    answer = []
    d = dict()

    for lang in ['cpp', 'java', 'python', "-"]:
        for job in ['backend', 'frontend', "-"]:
            for career in ['junior', 'senior', "-"]:
                for food in ['chicken', 'pizza', "-"]:
                    d[lang + job + career + food] = []

    for i in info:
        i = i.split()
        for lang in [i[0], "-"]:
            for job in [i[1], "-"]:
                for career in [i[2], "-"]:
                    for food in [i[3], "-"]:
                        d[lang + job + career + food].append(int(i[4]))
    
    for i in d.keys(): d[i].sort()

    for i in query:
        i = i.replace(" and ", "")
        i = i.split()

        t = d[i[0]]
        s = int(i[1])

        if (len(t) == 0):
            answer.append(0)
            continue
        else:
            start, end = 0, len(t)
            while (start < end):
                mid = (start + end) // 2
                if (t[mid] >= s):
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(t) - start)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))