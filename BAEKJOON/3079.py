import sys; input = sys.stdin.readline

N, M = map(int, input().split())
time = [int(input().rstrip()) for _ in range(N)]

start, end = min(time), max(time) * M

result = end
while start <= end:
    m = (start + end) // 2

    temp = 0
    for i in range(N): temp += m // time[i]

    if temp >= M:
        end = m - 1
        result = min(result, m)
    else: start = m + 1
print(result)