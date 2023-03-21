import sys
m = int(sys.stdin.readline().rstrip())
s = set()

for _ in range(m):
    inpu = sys.stdin.readline().split()
    if len(inpu) == 2: inpu[1] = int(inpu[1])
    if inpu[0] == "add":
        s.add(inpu[1])
    elif inpu[0] == "remove":
        s.discard(inpu[1])
    elif inpu[0] == "check":
        if inpu[1] in s: print(1)
        else: print(0)
    elif inpu[0] == "toggle":
        if inpu[1] in s: s.remove(inpu[1])
        else: s.add(inpu[1])
    elif inpu[0] == "all":
        s = set([i for i in range(1, 21)])
    elif inpu[0] == "empty":
        s = set()