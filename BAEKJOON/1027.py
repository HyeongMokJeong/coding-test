n = int(input())
build = list(map(int, input().split()))
answer = 0

for i in range(len(build)):
    count = 0
    left, right = i - 1, i + 1
    l_in, r_in = float("inf"), float("-inf")

    while (left >= 0):
        new_in = (build[i] - build[left]) / (i - left)
        if l_in > new_in: # 왼쪽으로 갈 때, 기존 기울기보다 새 기울기가 작으면 볼수 있음
            count += 1
            l_in = new_in
        left -= 1

    while (right < len(build)):
        new_in = (build[right] - build[i]) / (right - i)
        if r_in < new_in:
            count += 1
            r_in = new_in
        right += 1
    
    answer = max(answer, count)
print(answer)