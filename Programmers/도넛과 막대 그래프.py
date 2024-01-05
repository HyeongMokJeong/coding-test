from collections import defaultdict
def solution(edges):
    # 전체 노드 개수 확인
    node_count = 0
    for i in edges: node_count = max(node_count, max(i))

    # 그래프 생성
    graph = [[] for _ in range(node_count + 1)]
    in_dict = defaultdict(int)
    for s, e in edges: 
        graph[s].append(e)
        in_dict[e] += 1
    
    # 시작 노드, 총 그래프 개수 확인
    # 들어오는게 없고 나가는게 2개 이상이라면 시작 노드
    for i in range(1, len(graph)):
        if not in_dict[i] and len(graph[i]) >= 2:
            start_node, graph_count = i, len(graph[i])
            for j in graph[start_node]: in_dict[j] -= 1
            break

    # 막대 그래프, 8자 그래프 확인
    # 나가는게 없는 노드는 막대 그래프에만 1개(마지막)씩 존재
    # 나가는게 2개, 들어오는게 2개인 노드는 8자 그래프에만 1개(중심)씩 존재
    s_count, e_count = 0, 0
    for i in range(1, len(graph)):
        if i == start_node: continue
        out_count = len(graph[i])
        if not out_count: s_count += 1
        if out_count == 2 and in_dict[i] == 2: e_count += 1
    d_count = graph_count - s_count - e_count

    return [start_node, d_count, s_count, e_count]