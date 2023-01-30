answer = []
n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

for i in range(n - 7):
    for j in range(m - 7):
        countB = 0 # B로 시작한 경우
        countW = 0 # W로 시작한 경우
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: # 합이 짝수면 시작점과 같음
                    if board[a][b] == 'B': # 현재가 B다
                        countW += 1 # 더 적은 횟수를 위해서는 시작이 B여야함
                    if board[a][b] == 'W':
                        countB += 1
                else:
                    if board[a][b] == 'B': # 현재가 B다
                        countB += 1 # 더 적은 횟수를 위해서는 시작이 W여야함
                    if board[a][b] == 'W':
                        countW += 1
        answer.append(min(countB, countW))
                
print(min(answer))