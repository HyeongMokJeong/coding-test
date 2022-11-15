def solution(id_list, report, k):
    answer = [0] * len(id_list)
    count = {x : 0 for x in id_list}
    report = list(set(report))

    for i in report:
        count[i.split()[1]] += 1
    
    for i in report:
        if count[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo"], 2))