from itertools import combinations, product
def solution(dice):
    answer, result = [], 0

    # 주사위 번호 조합인 combi_a, combi_b
    # [[0, 1], [0, 2]...]
    combi_a, combi_b = [], []
    for combo in combinations([i for i in range(len(dice))], len(dice) // 2):
        combi_a.append(list(combo))
        combi_b.append([i for i in range(len(dice)) if i not in combo])

    # combi_a를 순회하면서 n//2개의 주사위끼리의 전체 합 경우의 수를 담는 result_a, result_b
    result_a, result_b = [], []
    for t in combi_a:
        temp = []
        for i in t: temp.append(dice[i])
        result_a.append(list(map(sum, list(product(*temp)))))

    for t in combi_b:
        temp = []
        for i in t: temp.append(dice[i])
        result_b.append(list(map(sum, list(product(*temp)))))

    # result_a와 result_b를 비교하며, result_a의 각 경우가 result_b의 각 경우에 대해 몇번 승리하는지 계산
    for i in range(len(result_a)):
        ta, tb = sorted(result_a[i]), sorted(result_b[i])
        dp = [0] * (max(max(ta), max(tb)) + 1)
        for b in tb: dp[b] += 1
        for dpi in range(1, len(dp)): dp[dpi] += dp[dpi - 1]
        
        temp = sum(dp[a - 1] for a in ta)
        if result < temp:
            result = temp
            answer = list(map(lambda x : x + 1, combi_a[i]))

    return answer