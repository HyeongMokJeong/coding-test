def solution(sequence, k):
    n = len(sequence)
    result_x, result_y = 0, n - 1

    temp, lp, rp = sequence[0], 0, 0
    while rp < n:
        if temp > k:
            temp -= sequence[lp]
            lp += 1
        else:
            if temp == k:
                if result_y - result_x > rp - lp: result_x, result_y = lp, rp
            rp += 1
            if rp < n: temp += sequence[rp]
        if lp > rp: lp, rp = rp, lp
    return [result_x, result_y]