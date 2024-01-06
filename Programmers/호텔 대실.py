def solution(book_time):
    time, max_time = [], 0

    for s, e in book_time:
        st, sm = map(int, s.split(':'))
        et, em = map(int, e.split(':'))
        start, end = st * 60 + sm, et * 60 + em + 10
        if end > max_time: max_time = end
        time.append((start, end))
    dp = [0] * (max_time + 1)
    for s, e in time:
        dp[s] += 1
        dp[e] -= 1
    
    for i in range(1, max_time): dp[i] += dp[i - 1]
    return max(dp)