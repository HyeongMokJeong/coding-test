package SOFTEER;

import java.io.*;
import java.util.*;

class 나무조경 {    
    private static int maxCount;
    private static int result = 0;
    private static boolean[][] visited;
    private static int n;
    private static int[][] map;
    private static int[][] directions = new int[][]{
        {0, 1}, {1, 0}
    };
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력값 받기
        n = Integer.parseInt(br.readLine());
        map = new int[n][n];
        visited = new boolean[n][n];
        maxCount = (n == 2) ? 2 : 4;

        for (int i = 0; i < n; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

            for (int j = 0; j < n; j++) map[i][j] = input[j];
        }

        // dfs 수행
        dfs(0, 0);
        System.out.println(result);
        br.close();
    }

    private static void dfs(int count, int sum) {
        // 최대 그룹이라면 결과값 비교
        if (count == maxCount) {
            result = Math.max(sum, result);
            return;
        }

        // 모든 경우의 수 파악
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 이미 방문한 곳은 패스
                if (visited[i][j]) continue;

                // 각 좌표에 대해 우측, 하단 두 경우로 분기
                for (int[] d : directions) {
                    int nx = i + d[0], ny = j + d[1];
                    if (nx >= n || ny >= n || visited[nx][ny]) continue;

                    visited[i][j] = true;
                    visited[nx][ny] = true;
                    dfs(count + 1, sum + map[i][j] + map[nx][ny]);
                    visited[i][j] = false;
                    visited[nx][ny] = false;
                }
            }
        }
    }
}