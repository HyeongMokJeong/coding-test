def solution(n):
    answer = []
    
    def run(s, m, e, c):
        if not c: return
        run(s, e, m, c - 1)
        answer.append([s, e])
        run(m, s, e, c - 1)
    run(1, 2, 3, n)
    return answer