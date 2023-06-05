import sys; input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
ary = list(map(int, input().split()))
ary.sort()

temp = [ary[i] - ary[i - 1] for i in range(1, N)]
temp.sort()
print(sum(temp[:N - K]))