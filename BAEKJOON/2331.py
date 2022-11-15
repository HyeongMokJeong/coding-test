def sum(n):
    n = str(n)
    result = 0
    for i in n:
        result += int(i)
    return result

def solution(n):
    n = str(n)
    result = 0
    for i in range(int(n)):
        if (int(i) + sum(i)) == int(n):
            result = i
            break
    return result

n = input()
print(solution(n))