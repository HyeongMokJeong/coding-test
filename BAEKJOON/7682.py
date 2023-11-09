import sys; input = sys.stdin.readline

def check(case, target):
    if case[0] == target and case[0] == case[1] == case[2]: return True
    elif case[0] == target and case[0] == case[3] == case[6]: return True
    elif case[4] == target and case[1] == case[4] == case[7]: return True
    elif case[4] == target and case[3] == case[4] == case[5]: return True
    elif case[8] == target and case[6] == case[7] == case[8]: return True
    elif case[8] == target and case[2] == case[5] == case[8]: return True
    elif case[4] == target and case[0] == case[4] == case[8]: return True
    elif case[4] == target and case[2] == case[4] == case[6]: return True
    else: return False

while True:
    case = input().rstrip()
    if case == 'end': break

    x_c = case.count('X')
    o_c = case.count('O')

    # x가 승리하려면 x개수 = o개수 + 1 / o가 승리하려면 o개수 = x개수
    if x_c == o_c + 1 or o_c == x_c:
        win, lose = ('X', 'O') if x_c == o_c + 1 else ('O', 'X')

        w_check, l_check = check(case, win), check(case, lose)

        # 둘다 동시에 성공하는 경우
        if l_check: print("invalid")
        # win도 성공하지 못한 경우
        elif not w_check:
            # 맵이 전부 차서 끝난 경우
            if case.count('.') == 0: print("valid")
            else: print("invalid")
        # lose가 성공하지 못했으면 가능
        else: print("valid")
    else: print("invalid")