n = int(input())
p = list(map(int, input().split())) # 누가 가져갈 건가
ori = p
s = list(map(int, input().split()))
g = [0, 1, 2] * (n // 3) # 순차 배열 - 0, 1, 2순으로 가져가는 순서 p가 맞춰질때 까지
new = [0] * n
cnt = 0
 
while p != g:
    for i in range(n):
        new[s[i]] = p[i] # 누가 가져가는지 그 순서 자체를 섞어서

    p = new
    new = [0] * n
    cnt += 1
    if ori == p: # 나왔던 순서(누가 가져갈지에 대한 순서)
        cnt =- 1
        break
print(cnt)