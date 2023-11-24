from itertools import permutations

def solution(user_id, banned_id):
    def check(users):
        for i in range(len(banned_id)):
            if len(users[i]) != len(banned_id[i]): return False
            for j in range(len(users[i])):
                if banned_id[i][j] == "*": continue
                if banned_id[i][j] != users[i][j]: return False
        return True

    u_p = list(permutations(user_id, len(banned_id)))
    answer = []

    for i in u_p:
        if not check(i): continue
        else:
            u = set(i)
            if u not in answer: answer.append(u)
    
    return len(answer)