from collections import deque
def solution(n, wires):
    answer = float('inf')

    def bfs(tree):
        visited = [0] * (n + 1)
        count = []

        for i in range(1, n + 1):
            temp = 0
            if not visited[i]:
                q = deque([i])
                while q:
                    t = q.popleft()
                    for j in tree[t]:
                        if not visited[j]:
                            visited[j] = 1
                            q.append(j)
                            temp += 1
                count.append(temp)
        return abs(count[0] - count[1])


    def run(idx):
        tree =[[] for _ in range(n + 1)]
        for i, v in enumerate(wires):
            if i == idx: continue
            tree[v[0]].append(v[1])
            tree[v[1]].append(v[0])
        return bfs(tree)
    
    for i in range(len(wires)): answer = min(answer, run(i))
    return answer