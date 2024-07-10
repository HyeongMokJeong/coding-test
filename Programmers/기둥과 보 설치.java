class Solution {
    private boolean[][] cols, rows; // 기둥, 보
    // 같은 좌표에 기둥과 보가 동시에 존재할 수 있으므로 배열을 구분

    public int[][] solution(int n, int[][] build_frame) {
        int count = 0;
        // 1 ~ n까지 사용하기 위해 n + 1 / 보의 경우 좌우를 고려해야 하므로 + 1 + 1
        cols = new boolean[n + 3][n + 3];
        rows = new boolean[n + 3][n + 3];

        for (int[] frame : build_frame) {
            int x = frame[0] + 1;
            int y = frame[1] + 1;
            if (frame[2] == 0) { // 기둥
                if (frame[3] == 1 && isExistCol(x, y)) { // 해당 위치에 기둥을 세울 수 있으면
                    cols[x][y] = true;
                    count++;
                }
                if (frame[3] == 0 && canRemove(n, x, y, 0)) { // 삭제할 수 있으면
                    cols[x][y] = false;
                    count--;
                }
            } else { // 보
                if (frame[3] == 1 && isExistRow(x, y)) {
                    rows[x][y] = true;
                    count++;
                }
                if (frame[3] == 0 && canRemove(n, x, y, 1)) {
                    rows[x][y] = false;
                    count--;
                }
            }
        }

        int[][] answer = new int[count][3];
        int index = 0;
        for (int i = 1; i <= n + 1; i++) { // 남아 있는 기둥과 보 배열에 저장
            for (int j = 1; j <= n + 1; j++) {
                if (cols[i][j]) answer[index++] = new int[]{i - 1, j - 1, 0};
                if (rows[i][j]) answer[index++] = new int[]{i - 1, j - 1, 1};
            }
        }
        return answer;
    }

    // 기둥이 존재할 수 있는지
    private boolean isExistCol(int x, int y) {
        // y == 1이면 바닥 위에 설치
        // cols[x][y - 1]이면 기둥 위에 설치
        // rows[x][y]이면 보에 연결
        // rows[x - 1][y]이면 보 오른쪽에 설치
        return y == 1 || cols[x][y - 1] || rows[x][y] || rows[x - 1][y];
    }

    // 보가 존재할 수 있는지
    private boolean isExistRow(int x, int y) {
        // cols[x][y - 1]이면 기둥 위에 설치
        // cols[x + 1][y - 1]이면 오른쪽 아래 기둥 위에 설치
        // 양쪽에 보가 있는 경우에도 설치
        return cols[x][y - 1] || cols[x + 1][y - 1] || (rows[x - 1][y] && rows[x + 1][y]);
    }

    private boolean canRemove(int n, int x, int y, int type) {
        boolean result = true;

        if (type == 0) cols[x][y] = false; // 임시로 삭제
        else rows[x][y] = false;

        loop:
        for (int i = 1; i <= n + 1; i++) {
            for (int j = 1; j <= n + 1; j++) {
                if (cols[i][j] && !isExistCol(i, j)) {
                    result = false;
                    break loop;
                }
                if (rows[i][j] && !isExistRow(i, j)) {
                    result = false;
                    break loop;
                }
            }
        }

        if (type == 0) cols[x][y] = true; // 삭제했던 구조물 원상복구
        else rows[x][y] = true;

        return result;
    }
}