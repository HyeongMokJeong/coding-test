# 1번 방법
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 2번 방법
from itertools import product
def solution2(numbers, target):
    l = [(i, -i) for i in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution2([4, 1, 2, 1], 4))