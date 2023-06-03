import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input().rstrip())
ary = [list(map(int, input().split())) for _ in range(N)]

def run(idx, up):
    global result
    if idx == N: return
    up_idx = ary[idx].index(up)

    if up_idx == 0: down_idx = -1
    elif up_idx == 5: down_idx = 0
    elif 1 <= up_idx <= 2: down_idx = up_idx + 2
    else: down_idx = up_idx - 2
    down = ary[idx][down_idx]

    m = 0
    for i in ary[idx]:
        if i == up or i == down: continue
        m = max(m, i)
    result += m
    return run(idx + 1, down)

answer = 0
for i in range(1, 7):
    result = 0
    run(0, i)
    answer = max(answer, result)
print(answer)