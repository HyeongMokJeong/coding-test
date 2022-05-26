def a(number):
    if number == "0" or number=="1": return False
    for i in range(2, int(number)):
        if int(number) % i == 0: return False
    return True

def b(numbers, num, answer):
    if a(num) and num not in answer: 
        answer.append(num)
    for j in numbers:
        newnum = num + j
        print(newnum)
        new = numbers.replace(j, '', 1)
        b(new, newnum, answer)

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        num = numbers[i]
        if num != "0":
            ary = numbers.replace(num, '', 1)
            b(ary, num, answer)
    return len(answer)

print(solution("1234"))