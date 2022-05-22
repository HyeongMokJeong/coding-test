def dfs(numbers, target, start, lists, result):
    if start == len(numbers):
        if sum(lists) == target: 
            result.append(0)
        return

    lists1, lists2 = lists.copy(), lists.copy()
    lists1.append(+numbers[start])
    lists2.append(-numbers[start])

    dfs(numbers, target, start + 1, lists1, result)
    dfs(numbers, target, start + 1, lists2, result)

    return len(result)


def solution(numbers, target):
    re = dfs(numbers, target, 0, list(), list())
    return re

print(solution([4, 1, 2, 1], 4))