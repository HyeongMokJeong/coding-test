import sys
n = int(sys.stdin.readline().rstrip())

count = 0
board = [0] * n

def check(t):
    for i in range(t):
         if board[t] == board[i] or t - i == abs(board[t] - board[i]):
            return False
    return True


def dfs(target):
    if target == n:
        global count
        count += 1
    else:
        for i in range(n):
            board[target] = i
            if check(target):
                dfs(target + 1)

dfs(0)
print(count)