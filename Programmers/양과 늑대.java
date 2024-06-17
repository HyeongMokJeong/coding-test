import java.util.ArrayList;
import java.util.List;

class Solution {
    private int answer = 0;
    private List<Integer>[] tree;
    private int[] nodes;

    public int solution(int[] info, int[][] edges) {
        tree = initTree(info.length, edges); nodes = info;
        dfs(0, 0, 0, List.of(0));
        return answer;
    }

    private List<Integer>[] initTree(int countNode, int[][] edges) {
        List<Integer>[] result = new ArrayList[countNode];

        for (int i = 0; i < countNode; i++) result[i] = new ArrayList<Integer>();
        for (int[] edge : edges) result[edge[0]].add(edge[1]);
        return result;
    }

    private void dfs(int idx, int sheep, int wolf, List<Integer> next) {
        if (nodes[idx] == 0) sheep++;
        else wolf++;

        if (sheep <= wolf) return;
        answer = Math.max(answer, sheep);

        List<Integer> nextList = new ArrayList<>();
        nextList.addAll(next);
        nextList.remove(Integer.valueOf(idx));
        for (int chlid : tree[idx]) nextList.add(chlid);

        for (int n : nextList) dfs(n, sheep, wolf, nextList);
    }
}