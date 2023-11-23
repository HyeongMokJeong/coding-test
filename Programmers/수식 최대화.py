from itertools import permutations
from collections import deque
def solution(expression):
    answer = 0
    types = ['*', '+', '-']
    def get_number():
        result = []
        temp = ""
        for i in expression:
            if i == '-' or i == '+' or i == '*':
                result.append(int(temp))
                result.append(i)
                temp = ""
            else: temp += i
        else: result.append(int(temp))
        return result

    
    def get_permutation():
        return list(permutations(types, len(types)))

    for case in get_permutation():
        s1, s2 = deque(get_number()), deque()

        for i in case:
            while s1:
                target = s1.popleft()
                if target == i:
                    t1 = s2.popleft()
                    t2 = s1.popleft()
                    if i == '*': s2.appendleft(t1 * t2)
                    elif i == '+': s2.appendleft(t1 + t2)
                    else: s2.appendleft(t1 - t2)
                else: s2.appendleft(target)
            s2.reverse()
            s1, s2 = s2, deque()
        res = abs(s1.pop())
        if res > answer: answer = res
    return answer