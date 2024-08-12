import java.util.Arrays;

class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) parent[i] = i;

        Arrays.sort(costs, (a, b) -> a[2] - b[2]);

        for (int[] cost : costs) {
            if (find(parent, cost[0]) != find(parent, cost[1])) {
                union(parent, cost[0], cost[1]);
                answer += cost[2];
            }
        }

        return answer;
    }

    private int find(int[] parent, int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent, parent[x]);
    }

    private void union(int[] parent, int x, int y) {
        int rootX = find(parent, x);
        int rootY = find(parent, y);
        if (rootX != rootY) parent[rootY] = rootX;
    }
}