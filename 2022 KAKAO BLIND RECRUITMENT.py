def solution(id_list, report, k):
    answer = [0] * len(id_list)
    count = {} # id별 신고당한 횟수
    m_count = {} # id별 메일 받은 횟수
    report = list(set(report))

    for i in report:
        a, b = i.split(' ')
        if count.get(b) == None:
            count[b] = 1
        else: count[b] += 1
    
    for j in report:
        a, b = j.split(' ')
        if count[b] >= k:
            if m_count.get(a) == None:
                m_count[a] = 1
            else: m_count[a] += 1
    
    for i in range(len(id_list)):
        if m_count.get(id_list[i]) == None:
            answer[i] = 0
        else: answer[i] = m_count[id_list[i]]
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"], 2))