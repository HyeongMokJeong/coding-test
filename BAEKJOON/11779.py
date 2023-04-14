import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bus[a].append((c, b))
t_s, t_e = map(int, input().split())

ary = [float('inf')] * (n + 1)
node_list = [0] * (n + 1)
def run():
    q = [(0, t_s)]
    while q:
        weight, target = heapq.heappop(q)
        if ary[target] < weight: continue
        for wei, tar in bus[target]:
            if weight + wei < ary[tar]:
                ary[tar] = weight + wei
                node_list[tar] = target
                heapq.heappush(q, (ary[tar], tar))
    return ary[t_e]

print(run())
result = [t_e]
temp = t_e
while temp != t_s:
    temp = node_list[temp]
    result.append(temp)
print(len(result))
print(*result[::-1])
