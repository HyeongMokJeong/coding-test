n = int(input())
dic = dict()
nums = []

for _ in range(n):
    x, y = list(map(int, input().split()))
    nums.append([y, x])
nums.sort()
for i in nums: print(i[1], i[0])