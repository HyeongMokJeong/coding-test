package SOFTEER;

import java.io.*;
import java.util.*;

class 장애물인식프로그램 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] ip = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(ip[j]);
            }
        }

        // 전체 블록의 개수를 셀 count, 각각의 개수를 셀 List 선언
        int count = 0;
        List<Integer> countList = new ArrayList<>();

        // 맵을 순회하다가 1을 만나면 카운트를 세고 탐색한다.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) {
                    count += 1;
                    countList.add(bfs(i, j, map));
                }
            }
        }

        countList.sort((a, b) -> a - b);
        System.out.println(count);
        for (int cl : countList) System.out.println(cl);

        br.close();
    }

    private static int bfs(int x, int y, int[][] map) {
        int count = 1;
        Deque<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{x, y});
        // 방문 여부는 -1로 체크한다.
        map[x][y] = -1;

        int[][] directions = new int[][]{
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };
        
        while (!q.isEmpty()) {
            int[] target = q.poll();
            int dx = target[0], dy = target[1];

            for (int[] direction : directions) {
                int nx = dx + direction[0], ny = dy + direction[1];

                // 범위 밖이거나 1이 아니라면 패스
                if (0 > nx || nx >= map.length || 0 > ny || ny >= map[0].length) continue;
                if (map[nx][ny] != 1) continue;

                q.offer(new int[]{nx, ny});
                map[nx][ny] = -1;
                count += 1;
            }
        }
        return count;
    }
}
