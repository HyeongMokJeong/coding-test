def solution(picks, minerals):
    answer = 0
    count_ary = []
    MAX_COUNT = min(len(minerals), sum(picks) * 5)
    cost_dict = {0 : (1, 1, 1), 1 : (5, 1, 1), 2 : (25, 5, 1)}

    for i in range(0, MAX_COUNT, 5):
        temp = minerals[i : i + 5]
        dia, iron, stone = 0, 0, 0
        for i in temp:
            if i == "diamond": dia += 1
            elif i == "iron": iron += 1
            else: stone += 1
        count_ary.append((dia, iron, stone))
    count_ary.sort(reverse=True)
    
    picks_idx = 0
    for i in count_ary:
        while not picks[picks_idx]: picks_idx += 1
        answer += cost_dict[picks_idx][0] * i[0]
        answer += cost_dict[picks_idx][1] * i[1]
        answer += cost_dict[picks_idx][2] * i[2]
        picks[picks_idx] -= 1
    
    return answer