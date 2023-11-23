def solution(users, emoticons):
    answer = [0, 0]

    sales = [10, 20, 30, 40]
    sales_combi = []
    def dfs(idx, temp):
        if idx == len(emoticons):
            sales_combi.append(temp[:])
            return
        for i in sales:
            temp[idx] += i
            dfs(idx + 1, temp)
            temp[idx] -= i
    dfs(0, [0] * len(emoticons))
    
    for i in sales_combi:
        temp_plus, temp_money = 0, 0
        for per, limit in users:
            temp = 0
            for idx, sale in enumerate(i):
                if sale >= per: temp += emoticons[idx] * (100 - sale) // 100
            if temp >= limit: temp_plus += 1
            else: temp_money += temp
        if answer[0] == temp_plus and answer[1] < temp_money: answer[1] = temp_money
        elif answer[0] < temp_plus: answer = [temp_plus, temp_money]
    
    return answer