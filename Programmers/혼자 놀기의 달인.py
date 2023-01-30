def dfs(cards, idx, visited, ary):
    if not visited[idx]:
        visited[idx] = True
        ary.append(cards[idx])
        return dfs(cards, cards[idx], visited, ary)
    else: return len(ary)

def solution(cards : list):
    cards.insert(0, 0)
    ary = []
    visited = [False] * len(cards)
    for j in range(1, len(cards)):
        if not visited[j]: ary.append(dfs(cards, j, visited, []))
    ary.sort(reverse=True)
    return ary[0] * ary[1] if len(ary) != 1 else 0

# print(solution([8,6,3,7,2,5,1,4]))
print(solution([2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))