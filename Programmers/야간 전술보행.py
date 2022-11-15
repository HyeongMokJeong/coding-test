def solution(distance, scope, times):
    ary = []

    for idx, i in enumerate(scope):
        i.sort()
        for j in range(i[0], i[1] + 1):
            if 0 < (j % sum(times[idx])) <= times[idx][0]: 
                ary.append(j)
                break
    return distance if not ary else sorted(ary)[0]


print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]]	))
# print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]]))