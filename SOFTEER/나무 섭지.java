package SOFTEER;

import java.io.*;
import java.util.*;

class 나무섭지 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n, m 저장
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]); int m = Integer.parseInt(nm[1]); 

        // 맵 초기화 및 유령, 남우, 목적지 좌표 저장
        List<int[]> ghosts = new ArrayList<>();
        int[] namwoo = new int[2];
        int[] goal = new int[2];

        String[][] map = new String[n][m];
        for (int r = 0; r < n; r++) {
            String[] tempInput = br.readLine().split("");

            for (int c = 0; c < m; c++) {
                String target = tempInput[c];
                map[r][c] = target;
                if (target.equals("D")) goal = new int[]{r, c};
                if (target.equals("N")) namwoo = new int[]{r, c};
                if (target.equals("G")) ghosts.add(new int[]{r, c});
            }
        }

        // bfs로 남우가 탈출까지 걸리는 시간 계산
        int namwooTime = bfs(namwoo[0], namwoo[1], map, false);
        // 출구에 도달하지 못했다면 No
        if (namwooTime == -1) {
            System.out.println("No");
            return;
        }

        // 출구에 더 가까운 유령 확인
        int ghostLength = Integer.MAX_VALUE;
        int[] ghostLocate = new int[2];

        for (int[] g : ghosts) {
            int leng = Math.abs(g[0] - goal[0]) + Math.abs(g[1] - goal[1]);
            if (leng < ghostLength) {
                ghostLength = leng;
                ghostLocate = new int[]{g[0], g[1]};
            }
        }
        
        // 유령이 탈출까지 걸리는 시간 계산
        int ghostTime = bfs(ghostLocate[0], ghostLocate[1], map, true);

        // 유령이 먼저 도착했다면 진우는 탈출하지 못함
        System.out.println((ghostTime <= namwooTime) ? "No" : "Yes");
    }

    private static int bfs(int x, int y, String[][] map, boolean isGhost) {
        // 방향 정의
        int[][] directions = new int[][]{
                {-1, 0},
                {0, 1},
                {1, 0},
                {0, -1},
        };

        // 큐, 방문 여부 확인할 배열 생성
        Deque<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{x, y, 0});

        boolean[][] isVisited = new boolean[map.length][map[0].length];
        isVisited[x][y] = true;

        // 큐가 빌 때까지 순회
        while (!dq.isEmpty()) {
            int[] target = dq.poll();
            int cx = target[0]; int cy = target[1]; int count = target[2];
            if (map[cx][cy].equals("D")) return count;

            // 네 방향 탐색
            for (int[] d : directions) {
                int nx = cx + d[0]; int ny = cy + d[1];

                // 범위 밖인지 확인
                if (0 > nx || map.length <= nx || 0 > ny || map[0].length <= ny) continue;
                // 이미 방문했는지 확인
                if (isVisited[nx][ny]) continue;
                // 벽인지 확인
                if (!isGhost && map[nx][ny].equals("#")) continue;

                // 큐에 추가 및 방문처리
                dq.offer(new int[]{nx, ny, count + 1});
                isVisited[nx][ny] = true;
            }
        }

        // 도달하지 못했다면 -1 리턴
        return -1;
    }
}
