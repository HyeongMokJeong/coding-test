import heapq
def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for start, end, weight in paths:
        graph[start].append((weight, end))
        graph[end].append((weight, start))
    summits.sort()
    ss = set(summits)

    def run():
        q = []
        intensity = [10000001] * (n + 1)

        for gate in gates:
            heapq.heappush(q, (0, gate))
            intensity[gate] = 0
        result = [0, 10000001]
        
        while q:
            weight, target = heapq.heappop(q)
            if target in ss or weight > intensity[target]: continue
            
            for wei, tar in graph[target]:
                new_intensity = max(wei, weight)
                if intensity[tar] > new_intensity:
                    intensity[tar] = new_intensity
                    heapq.heappush(q, (new_intensity, tar))
        for i in summits:
            if intensity[i] < result[1]:
                result = [i, intensity[i]]
        return result
    return run()