from math import gcd

def check(ary):
    g = ary[0]
    for i in ary[1:]:
        g = gcd(g, i)
    return g

def solution(ary, ary2):
    answer = 0

    a, b = check(ary), check(ary2)

    for i in ary:
        if i % b == 0: break
    else: answer = max(answer, b)
    for i in ary2:
        if i % a == 0: break
    else: answer = max(answer, a)
    return answer

print(solution([14, 35, 119], [18, 30, 102]))