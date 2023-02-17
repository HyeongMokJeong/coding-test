import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dic = defaultdict(int)

weight = 1
for case in range(len(str(n))):
    new_n = int(str(n)[:-1] + "9")
    gap = new_n - n
    # 1의 자리 계산
    for i in range(10): dic[i] += (n // 10 + 1) * weight
    for i in range(gap): dic[9 - i] -= weight
    
    # 10의 자리부터 계산
    for number in str(n)[:-1]:
        number = int(number)
        dic[number] -= gap * weight
    
    # 맨 앞에 0이 왔을 때의 경우 제외
    dic[0] -= weight

    n //= 10
    weight *= 10

for i in range(10): print(dic[i], end=' ')