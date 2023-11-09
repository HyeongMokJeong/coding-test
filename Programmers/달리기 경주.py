def solution(players, callings):
    answer = []
    a, b = dict(), dict()
    # a는 순위 : 이름 (ex. 0 : mumu)
    # b는 이름 : 순위 (ex. mumu : 0)
    for idx, i in enumerate(players): 
        a[idx] = i
        b[i] = idx

    for i in callings:
        # 첫 시나리오 : poe 2등, kai 3등, kai가 추월했다.
        # i가 추월한 이름 : kai

        # old = 추월한 사람이 원래 있던 순위 : 3 
        old = b[i]
        # b[i] = 추월한 사람의 현재 순위 : 2
        b[i] -= 1
        # before = 추월 당한 사람 이름 : poe
        before = a[old - 1]
        # 추월해서 앞지른 순위 = old - 1, 그 이름이 a[old - 1] = kai = a[2]
        a[old - 1] = i
        # a[old] = 
        a[old] = before
        b[before] = old

    for i in range(len(players)): answer.append(a[i])
    return answer