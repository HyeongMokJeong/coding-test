def solution(n, lost, reserve):
    n_lost = set(lost) - set(reserve)
    n_reserve = set(reserve) - set(lost)
    answer = len(n_lost)
    for i in n_lost:
        for j in [(i - 1), (i + 1)]:
            if j in n_reserve:
                answer -= 1
                n_reserve.remove(j)
                break
    return n - answer