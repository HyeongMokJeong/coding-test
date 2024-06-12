import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
        int[] answer = new int[sources.length];

        List<Integer>[] graph = initGraph(n, roads);

        int[] dist = new int[n + 1];
        Arrays.fill(dist, -1);
        dist[destination] = 0;

        ArrayDeque<Integer> q = new ArrayDeque<>();
        q.add(destination);

        while (!q.isEmpty()) {
            int t = q.pollFirst();

            for (int next : graph[t]) {
                if (dist[next] == -1) {
                    dist[next] = dist[t] + 1;
                    q.addLast(next);
                }
            }
        }
        for (int i = 0; i < sources.length; i++) answer[i] = dist[sources[i]];
        
        return answer;
    }

    private List<Integer>[] initGraph(int n, int[][] roads) {
        List<Integer>[] graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();
        
        for (int[] road : roads) {
            int a = road[0]; int b = road[1];
            graph[a].add(b);
            graph[b].add(a);
        }

        return graph;
    }
}