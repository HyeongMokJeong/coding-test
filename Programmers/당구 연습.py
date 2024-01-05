def solution(m, n, startX, startY, balls):
    answer = []
    # 직선을 한번 만나는 두 점 사이의 최소거리 = 한 점을 해당 직선에 대칭한 대칭점과 다른 한 점사이의 거리
    # 대칭점 계산
    target = [(-startX, startY), (startX, -startY), (m * 2 - startX, startY), (startX, 2 * n - startY)]

    for x, y in balls:
        temp = []
        # 대칭점 순회
        for ex, ey in target:
            e_b = (x - ex) ** 2 + (y - ey) ** 2 # 대칭점에서 공까지의 거리
            e_s = (startX - ex) ** 2 + (startY - ey) ** 2 # 대칭점에서 시작점까지의 거리

            if not (startX == x == ex or startY == y == ey) or (e_b > e_s): temp.append(e_b)
        answer.append(min(temp))
    return answer