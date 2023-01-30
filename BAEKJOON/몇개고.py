t, s = map(int, input().split())

if t <= 11 or t > 16: print(280)
else: print(320 if s == 0 else 280)