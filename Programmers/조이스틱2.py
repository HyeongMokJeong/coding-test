def solution(name):
    answer = 0
    n = len(name) - 1

    for idx, i in enumerate(name):
        answer += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)

        if i == 'A':
            t = idx
            while (t < len(name) and name[t] == 'A'):
                t += 1
            if idx == 0:
                left = 0
            else:
                left = idx - 1
            right = len(name) - t
            n = min(n, left + right + min(left, right))
    return answer + n