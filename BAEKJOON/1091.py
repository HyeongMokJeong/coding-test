n = int(input())
p = list(map(int, input().split())) # 카드가 누구에게 가는지?
s = list(map(int, input().split()))
count = 0
same = [i for i in range(n)]

target = [[] for _ in range(3)]
for idx, i in enumerate(p): target[i].append(idx)

deck = [i for i in range(n)]

while 1:
    now = [[] for _ in range(3)]
    for i in range(n): now[i % 3].append(deck[i])
    for i in range(3): now[i].sort()
    if target == now: break

    else:
        new = [i for i in range(n)]
        for i in range(n): new[s[i]] = deck[i]
        deck = new
        if same == deck:
            count = -1
            break
        count += 1
print(count)