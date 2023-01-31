from collections import defaultdict

n, k = map(int, input().split())
bot = defaultdict(int)
bot[1] = n

t, answer = 1, 0
while 1:
    while t in bot:
        if bot[t] > 1:
            bot[t * 2] += bot[t] // 2
            bot[t] %= 2
        t *= 2

    if sum(list(bot.values())) <= k: break

    #합칠 수 있는 최소 물병의 수를 구입
    liters = [liter for liter in bot if bot[liter] > 0]
    answer += liters[1] - liters[0]
    bot[liters[0]] = 0
    bot[liters[1]] = 0
    bot[liters[1] * 2] += 1
    t = liters[1] * 2
        
print(answer)
