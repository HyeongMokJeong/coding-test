king, stone, n = input().split()
n = int(n)
king, stone = list(king), list(stone)
king[1], stone[1] = int(king[1]), int(stone[1])
king[0], stone[0] = ord(king[0]) - 64, ord(stone[0]) - 64
move = [input() for _ in range(n)]

def check(move):
    global king, stone
    nx = king[0] + move[0]
    ny = king[1] + move[1]
    if nx > 0 and nx <= 8 and ny > 0 and ny <= 8:
        if nx == stone[0] and ny == stone[1]:
            nsx = stone[0] + move[0]
            nsy = stone[1] + move[1]
            if nsx > 0 and nsx <= 8 and nsy > 0 and nsy <= 8: king, stone = [nx, ny], [nsx, nsy]
        else: king = [nx, ny]

for i in move:
    if i == "R": check([1, 0])
    elif i == "L": check([-1, 0])
    elif i == "B": check([0, -1])
    elif i == "T": check([0, 1])
    elif i == "RT": check([1, 1])
    elif i == "LT": check([-1, 1])
    elif i == "RB": check([1, -1])
    elif i == "LB": check([-1, -1])
print(chr(king[0] + 64) + str(king[1]))
print(chr(stone[0] + 64) + str(stone[1]))