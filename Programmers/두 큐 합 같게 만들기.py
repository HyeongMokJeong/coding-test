def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    leng = len(queue1) * 2
    ans = (sum1 + sum2) // 2
    i, j = 0, 0

    while i < leng and j < leng and sum1 != sum2:
        if sum1 > sum2:
            sum1 -= queue1[i]
            sum2 += queue1[i]
            queue2.append(queue1[i])
            i += 1
        else:
            sum1 += queue2[j]
            sum2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1

    if sum1 == ans:
        return i + j    
    else: 
        return -1

if __name__ == '__main__':
    q = solution([3, 2, 7, 2], [4, 6, 5, 1])
    print(q)