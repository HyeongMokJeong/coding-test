def solution(board):
    o, x, size = 'O', 'X', 3
    o_count, x_count = sum(row.count(o) for row in board), sum(row.count(x) for row in board)

    def check(target):
        for i in range(size):
            if all(cell == target for cell in board[i]): return True
        for j in range(size):
            if all(board[i][j] == target for i in range(size)): return True
        if all(board[i][i] == target for i in range(size)): return True
        if all(board[i][2 - i] == target for i in range(size)): return True
        return False

    # O가 X보다 적거나 2개 이상 많다면
    if o_count < x_count or abs(o_count - x_count) >= 2: return 0

    # O가 완성일 때 X 개수가 n-1개가 아니라면 / X가 완성일 때 O 개수가 n개가 아니라면
    if (check(o) and x_count != o_count - 1) or (check(x) and o_count != x_count): return 0

    return 1