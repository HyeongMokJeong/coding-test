class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int mod = 1000000007;

        int[][] matrix = new int[n + 1][m + 1];
        for (int[] puddle : puddles) matrix[puddle[1]][puddle[0]] = -1;
        matrix[1][1] = 1;

        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (matrix[i][j] == -1) continue;
                if (matrix[i - 1][j] != -1) matrix[i][j] += matrix[i - 1][j] % mod;
                if (matrix[i][j - 1] != -1) matrix[i][j] += matrix[i][j - 1] % mod;
            }
        }

        return matrix[n][m] % mod;
    }
}