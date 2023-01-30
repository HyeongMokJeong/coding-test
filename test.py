import itertools

N = int(input())
nums = []

for i in range(1, 11):
    for j in itertools.combinations(range(10), i):
        print(j)
        j = sorted(list(j), reverse = True)
        print(j)
        nums.append(int(''.join(map(str, j))))
        print(nums)
        print()
nums.sort()
try :
    print(nums[N])
except:
    print(-1)