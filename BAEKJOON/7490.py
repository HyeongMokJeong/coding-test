import sys; input = sys.stdin.readline

def bt(target, i):
    if i > N:
        if not eval(target.replace(" ", "")): print(target)
        return
    bt(target + " " + str(i), i + 1)
    bt(target + "+" + str(i), i + 1)
    bt(target + "-" + str(i), i + 1)

for _ in range(int(input())):
    N = int(input())
    bt("1", 2)
    print()