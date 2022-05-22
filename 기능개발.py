def solution(progresses, speeds):
    answer = []

    while len(progresses) != 0:
        if (100 - progresses[0]) % speeds[0] == 0:
            need = 100 - progresses[0] / speeds[0]
        else:
            need = (100 - progresses[0]) / speeds[0] + 1
        for i in range(len(progresses)):
            progresses[i] += speeds[i] * need
        
        count = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                count += 1
            else: break
        if count != 0:
            del progresses[:count], speeds[:count]
            answer.append(count)

    return answer

print(solution([], []))