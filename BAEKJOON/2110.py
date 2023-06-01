import sys; input = sys.stdin.readline;

N, C = map(int, input().split())
ary = [int(input().rstrip()) for _ in range(N)]
ary.sort()

start = 1
end = ary[-1] - ary[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    cur = ary[0]

    for i in range(1, N):
        if ary[i] >= cur + mid:
            count += 1
            cur = ary[i]
    if count >= C:
        start = mid + 1
        result = mid
    else: end = mid - 1
print(result)