import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int solution(int n, int[][] edge) {
        List<Integer>[] graph = new List[n + 1];
        for (int i = 0; i < graph.length; i++) graph[i] = new ArrayList<>();
        
        for (int[] e : edge) {
            graph[e[0]].add(e[1]);
            graph[e[1]].add(e[0]);
        }

        int[] depth = new int[n + 1];
        depth[1] = 1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);

        while (!queue.isEmpty()) {
            int target = queue.poll();

            for (int node : graph[target]) {
                if (depth[node] == 0) {
                    queue.add(node);
                    depth[node] = depth[target] + 1;
                }
            }
        }

        int maxDepth = Arrays.stream(depth).max().getAsInt();
        return (int) Arrays.stream(depth).filter(d -> d == maxDepth).count();
    }
}