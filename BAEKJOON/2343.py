import sys; input = sys.stdin.readline

N, M = map(int, input().split())
ary = list(map(int, input().split()))

ma = max(ary)
start, end = ma, sum(ary)

result = float('inf')
while start <= end:
    mid = (start + end) // 2
    count, temp = 1, 0

    for i in range(N):
        if (temp + ary[i] <= mid): temp += ary[i]
        else:
            count += 1
            temp = ary[i]
        if count > M: break
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= ma: result = min(result, mid)
print(result)