import java.util.*;

class Solution {
    public int solution(int N, int[][] road, int K) {
        int answer = 0;

        List<int[]>[] graph = new ArrayList[N];
        for (int i = 0; i < N; i++) graph[i] = new ArrayList<>();
        for (int[] r : road) {
            int a = r[0] - 1, b = r[1] - 1, c = r[2];

            graph[a].add(new int[]{c, b});
            graph[b].add(new int[]{c, a});
        }
        
        int[] weight = new int[N];
        Arrays.fill(weight, Integer.MAX_VALUE);
        boolean[] visited = new boolean[N];
        weight[0] = 0;
        
        Queue<int[]> q = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        q.offer(new int[]{0, 0});
        
        while (!q.isEmpty()) {
            int[] target = q.poll();
            int idx = target[1], w = target[0];
            
            if (visited[idx]) continue;
            visited[idx] = true;
            
            for (int[] next : graph[idx]) {
                int nextIdx = next[1], nw = next[0];
                int nextWeight = w + nw;

                if (weight[nextIdx] > nextWeight) {
                    weight[nextIdx] = nextWeight;
                    q.offer(new int[]{nextWeight, nextIdx});
                }
            }
        }
        Set<> s = new HashSet<>();
        Map<String, String> m = new HashMap<>();
        m.con

        for (int w : weight) {
            if (w <= K) answer += 1;
        }

        return answer;
    }
}