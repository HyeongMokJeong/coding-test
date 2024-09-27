class Solution {
    public int solution(String dirs) {
        int answer = 0;
        int x = 5, y = 5, limit = 10;

        int[][][] matrix = new int[4][limit + 1][limit + 1];
        for (char next : dirs.toCharArray()) {
            int nx = x, ny = y;

            if (next == 'U') {
                if (++ny > limit) continue;
                if (matrix[0][nx][ny] == 0 && matrix[1][x][y] == 0) {
                    matrix[1][x][y] = 1;
                    matrix[0][nx][ny] = 1;
                    answer += 1;
                }
            } else if (next == 'D') {
                if (--ny < 0) continue;
                if (matrix[1][nx][ny] == 0 && matrix[0][x][y] == 0) {
                    matrix[0][x][y] = 1;
                    matrix[1][nx][ny] = 1;
                    answer += 1;
                }
            } else if (next == 'R') {
                if (++nx > limit) continue;
                if (matrix[2][nx][ny] == 0 && matrix[3][x][y] == 0) {
                    matrix[3][x][y] = 1;
                    matrix[2][nx][ny] = 1;
                    answer += 1;
                }
            } else  {
                if (--nx < 0) continue;
                if (matrix[3][nx][ny] == 0 && matrix[2][x][y] == 0) {
                    matrix[2][x][y] = 1;
                    matrix[3][nx][ny] = 1;
                    answer += 1;
                }
            }
            x = nx; y = ny;
        }
        return answer;
    }
}