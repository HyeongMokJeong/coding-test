package SOFTEER;

import java.io.*;
import java.util.*;

class 로봇이지나간경로 {
    private static int h, w;
    private static char[][] map;
    // 상하좌우 확인을 위한 2차원 배열
    private static int[][] directions = new int[][]{
            {1, 0}, {0, 1}, {-1, 0}, {0, -1}
    };
    // directions 배열의 각 인덱스와 매칭되는 방향을 저장한 Map
    private static Map<Integer, String> directionMap = Map.of(
        0, "v",
        1, ">",
        2, "^",
        3, "<"
    );
    private static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // hw 입력
        int[] hw = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        h = hw[0]; w = hw[1];

        // map 정보 입력 및 초기화
        map = new char[h][w];
        for (int i = 0; i < h; i++) {
            String input = br.readLine();
            for (int j = 0; j < w; j++) map[i][j] = input.charAt(j); 
        }

        // 조건에 따르면 상하좌우 4 방향에 #이 정확이 하나 있는 곳이 시작 가능한 점이 된다.
        // 시작 가능한 좌표를 찾으면 StringBuilder에 좌표와 시작 방향을 저장하고 dfs를 수행한다.
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (map[i][j] == '#') {
                    String checkResult = check(i, j); 
                    if (checkResult != null) {
                        // 문제의 출력 조건이 1부터 시작이기 때문에 각각 +1
                        sb.append(i + 1).append(" ").append(j + 1).append("\n");
                        sb.append(checkResult).append("\n");
                        dfs(i, j, checkResult);
                    }
                }
            }
        }
        System.out.println(sb.toString());
        
        br.close();
    }

    // 시작 가능한 좌표인지 체크하는 메서드
    private static String check(int x, int y) {
        // 인접한 #의 방향을 저장할 temp 변수
        String temp = null;
        for (int i = 0; i < 4; i++) {
            int[] d = directions[i];
            int nx = x + d[0], ny = y + d[1];
            // 범위를 벗어나면 넘어간다.
            if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
            // 인접한 #를 발견했다면
            if (map[nx][ny] == '#') {
                // 이미 발견한 적이 있다면 시작 가능한 좌표가 아니므로 즉시 null return
                if (temp != null) return null;
                temp = directionMap.get(i);
            }
        }
    
        return temp;
    }

    private static void dfs(int x, int y, String direct) {
        map[x][y] = '.';
        for (int i = 0; i < 4; i++) {
            int[] d = directions[i];
            // 인접한 상하좌우, 다음 좌표인 2칸 상하좌우
            int tx = x + d[0], ty = y + d[1];
            int nx = x + d[0] * 2, ny = y + d[1] * 2;

            if (nx < 0 || nx >= h || ny < 0 || ny >= w) continue;
            // 다음 이동 장소라면
            if (map[tx][ty] == '#' && map[nx][ny] == '#') {
                map[tx][ty] = '.';
                // 현재 로봇의 방향에 따라 분기한다.
                if (direct.equals("<")) {
                    if (i == 0) {
                        sb.append("L").append("A");
                        dfs(nx, ny, "v");
                    } else if (i == 2) {
                        sb.append("R").append("A");
                        dfs(nx, ny, "^");
                    } else {
                        sb.append("A");
                        dfs(nx, ny, direct); 
                    }
                } else if (direct.equals(">")) {
                    if (i == 0) {
                        sb.append("R").append("A");
                        dfs(nx, ny, "v");
                    } else if (i == 1) {
                        sb.append("A");
                        dfs(nx, ny, direct);
                    } else {
                        sb.append("L").append("A");
                        dfs(nx, ny, "^"); 
                    }
                } else if (direct.equals("^")) {
                    if (i == 1) {
                        sb.append("R").append("A");
                        dfs(nx, ny, ">");
                    } else if (i == 2) {
                        sb.append("A");
                        dfs(nx, ny, direct);
                    } else {
                        sb.append("L").append("A");
                        dfs(nx, ny, "<"); 
                    }
                } else if (direct.equals("v")) {
                    if (i == 0) {
                        sb.append("A");
                        dfs(nx, ny, direct);
                    } else if (i == 1) {
                        sb.append("L").append("A");
                        dfs(nx, ny, ">");
                    } else {
                        sb.append("R").append("A");
                        dfs(nx, ny, "<"); 
                    }
                }
            }
        }
    }
}
