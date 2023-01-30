from math import sqrt, ceil

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k): 
        answer += ceil(sqrt(d**2 - i**2) // k + 1)
    return answer