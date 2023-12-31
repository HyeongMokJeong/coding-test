def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2

    # 다음 시간 기준으로 계산하니 현재 시간이 정각이면 카운트 1
    if start == 0 or start == 12 * 3600: answer += 1

    while start < end:
        # 시침은 1시간에 30도 -> 1초에 30 / 3600(초) = 1/120도 이동
        # 분침은 1분에 6도 -> 1초에 6 / 60 = 1 / 10도 이동
        # 360도 내에서 표현하기 위해 % 360
        h_cur = start / 120 % 360
        m_cur = start / 10 % 360
        s_cur = start * 6 % 360

        # 0도가 아닌 360도로 계산
        h_next = 360 if (start + 1) / 120 % 360 == 0 else (start + 1) / 120 % 360
        m_next = 360 if (start + 1) / 10 % 360 == 0 else (start + 1) / 10 % 360
        s_next = 360 if (start + 1) * 6 % 360 == 0 else (start + 1) * 6 % 360

        # 현재 초침이 시,분침 이전이었는데
        # 1초 뒤에 같거나 이후라면 카운트 추가
        if s_cur < h_cur and s_next >= h_next: answer += 1
        if s_cur < m_cur and s_next >= m_next: answer += 1
        # 초침이 시침, 분침과 모두 같다면 1번으로 계산하기 위해 - 1
        if s_next == h_next and s_next == m_next: answer -= 1

        start += 1
    return answer 