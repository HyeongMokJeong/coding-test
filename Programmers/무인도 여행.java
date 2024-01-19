import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

class Solution {
    private static boolean[][] visited;
    private static char[][] newMap;
    private static int x, y;
    private static int temp;

    private void dfs(int a, int b) {
        int[][] d = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

        for (int[] dxy : d) {
            int nx = dxy[0] + a, ny = dxy[1] + b;
            if ((0 <= nx && nx < x) && (0 <= ny && ny < y) && newMap[nx][ny] != 'X' && !visited[nx][ny]) {
                visited[nx][ny] = true;
                temp += Character.getNumericValue(newMap[nx][ny]);
                dfs(nx, ny);
            }
        }
    }

    public int[] solution(String[] maps) {
        List<Integer> answer = new LinkedList<>();
        x = maps.length;
        y = maps[0].length();
        visited = new boolean[x][y];
        newMap = new char[x][y];
        for (int i = 0; i < x; i++) newMap[i] = maps[i].toCharArray();

        for (int i = 0; i < x; i++) {
            for (int j = 0; j < y; j++) {
                if (newMap[i][j] != 'X' && !visited[i][j]) {
                    temp = Character.getNumericValue(newMap[i][j]);
                    visited[i][j] = true;
                    dfs(i, j);
                    answer.add(temp);
                }
            }
        }
        if (answer.isEmpty()) answer.add(-1);
        Collections.sort(answer);
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}