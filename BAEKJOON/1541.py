ary = input().split('-')
result = sum(map(int, ary[0].split('+')))

if len(ary) > 1:
    for i in ary[1:]:
        if '+' in i:
            new = i.split('+')
            temp = sum(map(int, new))
            result -= temp
        else:
            result -= int(i)
print(result)