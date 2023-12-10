def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    
    limit = 0
    for x, y in targets:
        if x >= limit:
            limit = y
            answer += 1
    return answer