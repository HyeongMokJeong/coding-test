def solution(k, dungeons):
    global answer
    answer = -1
    n = len(dungeons)

    visited = [0] * n
    def run(left, count):
        global answer
        answer = max(answer, count)

        for i in range(n):
            if visited[i]: continue
            need, use = dungeons[i]
            if left >= need:
                visited[i] = 1
                run(left - use, count + 1)
                visited[i] = 0
    run(k, 0)
    return answer