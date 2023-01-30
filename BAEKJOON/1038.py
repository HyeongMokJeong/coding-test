n = int(input())

count = -1
def dfs(length, mj):
    global count
    if len(mj) == length:
        count += 1
        if count == n:
            print(mj)
            exit(0)
    
    else:
        if mj =='':
            for i in range(length - 1, 10): dfs(length, str(i))
        else:
            for i in range(length - len(mj) - 1, int(mj[-1])): # 남은 자리수 - 1 ~ 마지막 숫자보다 작은 범위
                dfs(length, mj + str(i))

for i in range(1, 11): # 9876543210 10자리까지 가능
    dfs(i, '')
print(-1)