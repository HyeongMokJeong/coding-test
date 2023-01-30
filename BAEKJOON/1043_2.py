n, m = map(int, input().split())
know = set(input().split()[1:])
party = [set(input().split()[1:]) for _ in range(m)]
answer = 0

for _ in range(m):
    for i in party:
        if i & know:
            know = know.union(i)

for i in party:
    if i & know: continue
    answer += 1
print(answer)