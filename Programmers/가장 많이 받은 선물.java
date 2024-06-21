import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        Map<String, Integer> nameToIdxMap = new HashMap<>();
        for (int i = 0; i < friends.length; i++) nameToIdxMap.put(friends[i], i);

        int[] pidx = new int[friends.length];
        int[][] graph = new int[friends.length][friends.length];

        for (String gift : gifts) {
            String[] t = gift.split(" ");
            int a = nameToIdxMap.get(t[0]); int b = nameToIdxMap.get(t[1]);

            graph[a][b] += 1;
            pidx[a] += 1; pidx[b] -= 1;
        }

        int[] count = new int[friends.length];
        
        for (int i = 0; i < friends.length; i++) {
            for (int j = i; j < friends.length; j++) {
                if (i == j) continue;

                if (graph[i][j] > graph[j][i]) count[i] += 1;
                else if (graph[i][j] < graph[j][i]) count[j] += 1;
                else {
                    if (pidx[i] > pidx[j]) count[i] += 1;
                    else if (pidx[i] < pidx[j]) count[j] += 1;
                }
            }
        }

        return Arrays.stream(count).max().getAsInt();
    }
}