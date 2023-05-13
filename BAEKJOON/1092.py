import sys; input = sys.stdin.readline

n = int(input().rstrip())
limit = list(map(int, input().split()))
m = int(input().rstrip())
weight = list(map(int, input().split()))
limit.sort(reverse=True)
weight.sort(reverse=True)

if limit[0] < weight[0]: 
    print(-1)
    exit(0)

result = 0
while weight:

    for i in limit:
        for j in weight:
            if j > i: continue
            weight.remove(j)
            break
    result += 1
print(result)