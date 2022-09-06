def solution(record):
    answer = []
    dict = {}
    
    for i in record:
        cut = i.split(' ')
        if i.startswith("E") or i.startswith("C"):
            dict[cut[1]] = cut[2]

    for i in record:
        cut = i.split(' ')
        if i.startswith("E"):
            answer.append(f"{dict[cut[1]]}님이 들어왔습니다.")
        elif i.startswith("L"):
            answer.append(f"{dict[cut[1]]}님이 나갔습니다.")
    
    return answer

if __name__ == "__main__":
    a = solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
    print(a)