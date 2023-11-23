def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    t_del, t_pic = 0, 0
    for i in range(n):
        t_del += deliveries[i]
        t_pic += pickups[i]

        while t_del > 0 or t_pic > 0:
            t_del -= cap
            t_pic -= cap
            answer += (n - i) * 2
    return answer