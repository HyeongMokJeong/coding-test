import sys; input = sys.stdin.readline

N, M, L = map(int, input().split())
ary = [0] + list(map(int, input().split())) + [L]
ary.sort()

start, end = 1, L - 1
result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2

    for i in range(1, len(ary)):
        if ary[i] - ary[i - 1] > mid:
            count += (ary[i] - ary[i - 1] - 1) // mid
    if count > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
print(result)