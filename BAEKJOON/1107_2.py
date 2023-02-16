import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
if m != 0: b = list(map(int, sys.stdin.readline().split()))
else: b = list()

result = abs(n - 100)

for nums in range(1000001):
    nums = str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in b: break

        elif j == len(nums) - 1:
            result = min(result, abs(int(nums) - n) + len(nums))
print(result)