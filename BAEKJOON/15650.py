n, m = map(int,input().split())

ary = []
def run(target):
    if len(ary) == m: 
        print(' '.join(map(str, ary)))
        return

    for i in range(target, n + 1):
        if i not in ary:
            ary.append(i)
            run(i + 1)
            ary.pop()
run(1)