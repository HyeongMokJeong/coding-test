import sys; input = sys.stdin.readline

for _ in range(int(input())):
    password = input().rstrip()
    q1, q2 = [], []

    for i in password:
        if i == '<':
            if q1: q2.append(q1.pop())
        elif i == '>':
            if q2: q1.append(q2.pop())
        elif i == '-': 
            if q1: q1.pop()
        else: q1.append(i)
    print("".join(q1 + q2[::-1]))