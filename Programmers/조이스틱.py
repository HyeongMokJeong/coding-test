import queue, copy

def solution(name):
    alpha = {chr(i + 65) : i for i in range(26)}

    q = queue.Queue()
    q.put([['A'] * len(name), 0, 0]) # [1]은 조작횟수, [2]는 현재 커서 idx

    while(True):
        t = q.get()

        t[1] += min(alpha[name[t[2]]], 26 - alpha[name[t[2]]])
        t[0][t[2]] = name[t[2]]
        if (''.join(t[0]) == name): 
            return t[1]
        a, b = copy.deepcopy(t), copy.deepcopy(t)
        q.put([a[0], a[1] + 1, (a[2] + 1) % len(name)])
        q.put([b[0], b[1] + 1, b[2] - 1 if b[2] != 0 else len(name) - 1])

print(solution("JEROEN"))