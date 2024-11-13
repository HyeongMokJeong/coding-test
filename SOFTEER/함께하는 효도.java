package SOFTEER;

import java.io.*;
import java.util.*;

class 함께하는효도 {
    private static int n, m;
    private static int[][] map;
    private static int[][] friends;
    private static boolean[][] visited;
    private static int result = 0;
    private static final int[][] directions = new int[][]{
      {1, 0}, {0, 1}, {-1, 0}, {0, -1}  
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // nm 입력
        int[] nm = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        n = nm[0]; m = nm[1];

        // map, visited 초기화
        map = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < n; j++) map[i][j] = input[j];
        }

        // friends 초기화
        friends = new int[m][2];
        for (int i = 0; i < m; i++) {
            int[] xy = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int x = xy[0] - 1, y = xy[1] - 1;
            visited[x][y] = true;
            result += map[x][y];
            friends[i] = new int[]{x, y};
        }

        dfs(friends[0][0], friends[0][1], 0, 0, result);
        
        System.out.println(result);
        br.close();
    }

    private static void dfs(int x, int y, int idx, int depth, int sum) {
        result = Math.max(result, sum);
        
        // idx번째 친구의 이동이 끝나면, 그대로 다음 친구에게로 이동
        if (depth == 3) {
            int nextIdx = idx + 1;
            if(nextIdx < m){
                dfs(friends[nextIdx][0], friends[nextIdx][1], nextIdx, 0, sum);
            }
            return;
        }

        for (int[] d : directions) {
            int nx = x + d[0], ny = y + d[1];
            if (0 > nx || nx >= n || 0 > ny || ny >= n) continue;
            if (visited[nx][ny]) continue;

            visited[nx][ny] = true;
            dfs(nx, ny, idx, depth + 1, sum + map[nx][ny]);
            visited[nx][ny] = false;
        }
    }
}