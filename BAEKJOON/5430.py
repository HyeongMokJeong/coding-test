import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = list(sys.stdin.readline())
    n = int(sys.stdin.readline())
    ary = sys.stdin.readline().rstrip()
    if n != 0: ary = deque(ary[1:-1].split(","))
    else: ary = deque()

    reverse = False
    for i in p:
        if i == "R":
            reverse = True if not reverse else False
        if i == "D":
            if len(ary) == 0:
                print("error")
                break
            if not reverse:
                ary.popleft()
            else:
                ary.pop()
    else:
        if not reverse:
            print("[" + ",".join(ary) + "]")
        else:
            ary.reverse()
            print("[" + ",".join(ary) + "]")