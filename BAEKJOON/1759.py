import sys; input = sys.stdin.readline
L, C = map(int, input().split())
ary = sorted(input().rstrip().split())

temp = []
def bt(idx, size):
    global temp
    if size == L:
        mo, za = 0, 0
        for i in temp:
            if i in ['a', 'e', 'i', 'o', 'u']: mo += 1
            else: za += 1
        if mo >= 1 and za >= 2: print("".join(temp))
        return
    for i in range(idx, C):
        temp.append(ary[i])
        bt(i + 1, size + 1)
        temp.pop()
bt(0, 0)