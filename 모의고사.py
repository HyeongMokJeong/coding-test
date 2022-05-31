def solution(answers):
    answer = []
    ct= [0, 0, 0]
    as1 = [1, 2, 3, 4, 5]
    as2 = [2, 1, 2, 3, 2, 4, 2, 5]
    as3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in answers:
        if answer[i] == as1[i % (len(as1)-1)]: 
            ct[0] += 1
        if answer[i] == as2[i % (len(as2)-1)]: 
            ct[1] += 1
        if answer[i] == as3[i % (len(as3)-1)]: 
            ct[2] += 1
    
    answer.append(ct.index(max(ct)) + 1)
    return answer
print(solution([1,3,2,4,2]))