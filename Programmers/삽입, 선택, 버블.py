def i_sort(ary):
    for end in range(len(ary) - 1):
        for i in range(end, -1, -1):
            if (ary[i] > ary[i + 1]):
                ary[i], ary[i + 1] = ary[i + 1], ary[i]
    return ary

def s_sort(ary):
    for end in range(len(ary) - 1, 0, -1):
        big = end
        for i in range(end):
            if (ary[big] < ary[i]): big = i
        ary[big], ary[end] = ary[end], ary[big]
    return ary

def b_sort(ary):
    for end in range(len(ary) - 1, -1, -1):
        for i in range(end):
            if (ary[i] > ary[i + 1]):
                ary[i], ary[i + 1] = ary[i + 1], ary[i]
    return ary

ary = [1, -3, 4, 6, 2, -7, 4]
print(i_sort(ary))