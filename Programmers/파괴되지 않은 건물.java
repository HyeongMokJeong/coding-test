class Solution {
    int[][] matrix;

    public int solution(int[][] board, int[][] skill) {
        int answer = 0;
        matrix = new int[board.length + 1][board[0].length + 1];

        for (int[] s : skill) {
            int degree = (s[0] == 1) ? s[5] * -1 : s[5];

            matrix[s[1]][s[2]] += degree;
            matrix[s[3] + 1][s[2]] -= degree;
            matrix[s[1]][s[4] + 1] -= degree;
            matrix[s[3] + 1][s[4] + 1] += degree;
        }
        calculate();

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (matrix[i][j] + board[i][j] > 0) answer++;
            }
        }

        return answer;
    }

    private void calculate() {
        for (int i = 0; i < matrix.length - 1; i++) {
            for (int j = 0; j < matrix[0].length - 1; j++) {
                matrix[i][j + 1] += matrix[i][j];
            }
        }

        for (int i = 0; i < matrix[0].length - 1; i++) {
            for (int j = 0; j < matrix.length - 1; j++) {
                matrix[j + 1][i] += matrix[j ][i];
            }
        }
    }
}