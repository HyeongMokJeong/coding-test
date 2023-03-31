import sys

n = int(sys.stdin.readline().rstrip())
ary = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
result = ""

def recur(s_x, s_y, size):
    global result
    t = ary[s_x][s_y]

    for i in range(s_x, s_x + size):
        for j in range(s_y, s_y + size):
            if ary[i][j] != t:
                result += "("
                for a in range(2):
                    for b in range(2):
                        recur(s_x + a * size // 2, s_y + b * size // 2, size // 2)
                result += ")"
                return
    result += str(t)

recur(0, 0, n)
print(result)