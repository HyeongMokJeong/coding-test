ary = input().split(":")

result = []

check = False
for i in ary:
    if i == "" and not check:
        check = True
        result += ['0000' for _ in range(8 - len(ary) + 1)]
    else: result.append(i.zfill(4))
print(":".join(result))