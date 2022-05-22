def solution(brown, yellow):
     
    all = brown + yellow
    for i in range(all):
        for j in range(i + 1):
            if i * j == all:
                if (i-2)*(j-2) == yellow:
                    return [i, j]