package SOFTEER;

import java.io.*;
import java.util.*;

class 이미지프로세싱 {
    private static int h, w;
    private static int[][] map;
    private static int[][] directions = new int[][]{
        {1, 0}, {0, 1}, {-1, 0}, {0, -1}
    };
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // hw 입력
        int[] hw = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        h = hw[0]; w = hw[1];

        // 비트맵 입력 및 초기화
        map = new int[h][w];
        for (int i = 0; i < h; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < w; j++) {
                map[i][j] = input[j];
            }
        }

        // 변경되는 픽셀 입력
        int q = Integer.parseInt(br.readLine());
        for (int time = 0; time < q; time++) {
            int[] ijc = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int i = ijc[0] - 1, j = ijc[1] - 1, c = ijc[2];

            // 각 경우에 대해 방문 배열 선언
            boolean[][] visited = new boolean[h][w];
            visited[i][j] = true;
            dfs(i, j, map[i][j], c, visited);
        }

        StringBuilder sb = new StringBuilder();
        for (int[] m : map) {
            for (int pixel : m) sb.append(pixel).append(" ");
            sb.append("\n");
        }
        System.out.println(sb.toString());
        br.close();
    }

    private static void dfs(int x, int y, int before, int after, boolean[][] visited) {
        map[x][y] = after;
        for (int[] d : directions) {
            int nx = x + d[0], ny = y + d[1];

            // 범위를 초과했거나 이미 방문한 좌표면 continue
            if (0 > nx || nx >= h || 0 > ny || ny >= w) continue;
            if (visited[nx][ny]) continue;
            if (map[nx][ny] == before) {
                visited[nx][ny] = true;
                dfs(nx, ny, before, after, visited);
            }
        }
    }
}
