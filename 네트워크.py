def solution(n, computers):
    answer = 0
    if n == 1: return 1
    
    matrix  =[[0 for i in range(n)] for i in range(n)]
    
    for i in computers:
        x, y = None, None
        for j in range(len(i)):
            if i[j] != 0:
                if x == None: x = j
                elif y == None: y = j
                else:
                    matrix[y][x] = 1
                    x = y
                    y = j
        if y != None:
            matrix[y][x] = 1
        elif x != None and y == None:
            answer += 1

    visitedAry = [0]
    current = 0
    while True:
        next = None
        for i in range(n):
            if matrix[i][current] != 0:
                    if i not in visitedAry:
                        next = i
                        matrix[i][current] = 0
                        break
        if next != None:
            current = next
            visitedAry.append(next)
        else:
            answer += 1
            break

    return answer
print(solution(3, 	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))