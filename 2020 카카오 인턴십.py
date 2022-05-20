def solution(numbers, hand):
    answer = ''
    left, right, mid = [1, 4, 7], [3, 6, 9], [2, 5, 8, 0]
    left_last, right_last = [3, 0], [3, 2]

    for i in numbers:
        if i in left:
            left_last = [left.index(i), 0]
            answer += 'L'
        elif i in right:
            right_last = [right.index(i), 0]
            answer += 'R'
        else:
            left_length = abs(left_last[0] - mid.index(i)) + abs(left_last[1] - 1)
            right_length = abs(right_last[0] - mid.index(i)) + abs(right_last[1] - 1)
            if left_length == right_length:
                if hand == 'right':
                    answer += 'R'
                    right_last = [mid.index(i), 1]
                else:
                    answer += 'L'
                    left_last = [mid.index(i), 1]
            else:
                if min(left_length, right_length) == left_length:
                    answer += 'L'
                    left_last = [mid.index(i), 1]
                else:
                    answer += 'R'
                    right_last = [mid.index(i), 1]
    return answer
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))