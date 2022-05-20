def solution(s):
    answer = []
    mid = len(s) // 2 + 1
    if len(s) < 2: return 1
    for i in range(1, mid):
        word = s
        lists = []
        result = ""
        for j in range(0, len(word), i):
            lists.append(word[j:j+i])
        count = 1

        for b in range(0, len(lists)-1):
            if lists[b] == lists[b + 1]:
                count += 1
            else:
                if count != 1:
                    result += f"{count}{lists[b]}"
                    count = 1
                else:
                    result += f"{lists[b]}"
        if count != 1:
            result += f"{count}{lists[b]}"
        else:
            result += f"{lists[len(lists)-1]}"
        answer.append(len(result))
    return min(answer)

print(solution("aabbaccc"))