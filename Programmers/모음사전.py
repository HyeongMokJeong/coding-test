def solution(word):
    global temp, result
    temp, result = -1, 0

    def run(target):
        global temp, result
        temp += 1
        if result: return
        if target == word:
            result = temp
            return
        if len(target) >= 5: return
        for i in ['A', 'E', 'I', 'O', 'U']: run(target + i)
    run("")
    return result