import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    List<int[]>[] graph;
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = Integer.MAX_VALUE;

        graph = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();

        for (int[] f : fares) {
            int c = f[0]; int d = f[1]; int w = f[2];
            graph[c].add(new int[]{w, d});
            graph[d].add(new int[]{w, c});
        }

        int[] start = dijkstra(s, n);
        int[] startA = dijkstra(a, n);
        int[] startB = dijkstra(b, n);

        for(int i=1; i<=n; i++) answer = Math.min(answer, start[i] + startA[i] + startB[i]);
        
        return answer;
    }

    int[] dijkstra(int start, int n) {
        int[] result = new int[n + 1];
        Arrays.fill(result, 100001);
        result[start] = 0;

        PriorityQueue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        q.add(new int[]{0, start});

        while (!q.isEmpty()) {
            int[] t = q.poll();
            int w = t[0]; int node = t[1];

            for (int[] next : graph[node]) {
                int nw = next[0]; int nn = next[1];
                if (result[nn] > w + nw) {
                    result[nn] = w + nw;
                    q.add(new int[]{w + nw, nn});
                }
            }
        }
        return result;
    }
}