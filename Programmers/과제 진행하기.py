from collections import deque
def solution(plans):
    answer = []

    target, now = "", float('inf')
    start_time_map, left_time_map = dict(), dict()
    for name, start, time in plans:
        h, m = map(int, start.split(':'))
        new_time = h * 60 + m
        start_time_map[new_time] = name
        left_time_map[name] = int(time)
        if new_time < now:
            now = new_time
            target = name

    stop_stack = deque()
    while len(answer) != len(plans):
        # 숙제 수행
        left_time_map[target] -= 1

        # 만약 다 했으면
        if not left_time_map[target]: 
            # answer에 추가
            answer.append(target)
            
            # 그 다음 시작해야할 숙제 확인
            # 만약 지금 시작해야할 숙제가 있다면 그 숙제를 target으로 지정
            check = start_time_map.get(now)
            if check != None: target = check
            elif stop_stack: target = stop_stack.pop()

        # 다 안했으면
        else:
            # 지금 시작해야할 숙제 확인
            check = start_time_map.get(now)
            # 만약 있다면 현재 숙제를 stop_stack에 추가하고 target 교체
            if check != None and check != target: 
                stop_stack.append(target)
                target = check
        now += 1
    return answer
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))