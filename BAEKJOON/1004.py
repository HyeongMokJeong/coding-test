def solution():
    t = int(input())
    for _ in range(t):
        count = 0
        x1, y1, x2, y2 = map(int, input().split())
        n = int(input())
        for _ in range(n):
            c1, c2, r = map(int, input().split())
            new = (((x1 - c1) ** 2) + ((y1 - c2) ** 2)) ** 0.5
            new2 = (((x2 - c1) ** 2) + ((y2 - c2) ** 2)) ** 0.5
            if (new < r and new2 > r) or (new > r and new2 < r): count += 1
    print(count)
solution()