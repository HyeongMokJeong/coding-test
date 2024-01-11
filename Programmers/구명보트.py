def solution(people, limit):
    answer = 0
    people.sort()

    lp, rp = 0, len(people) - 1
    while lp <= rp:
        temp = limit
        # 제일 무거운 사람 탑승
        temp -= people[rp]
        rp -= 1

        # 같이 탈 수 있는 가벼운 사람 탑승
        if people[lp] <= temp: lp += 1
        answer += 1
    return answer