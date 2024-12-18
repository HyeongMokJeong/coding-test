class Solution {
    private int row = 4;
    
    int solution(int[][] land) {
        int answer = 0;
        int n = land.length;

        int[][] dp = new int[land.length][row];
        for (int i = 0; i < row; i++) dp[0][i] = land[0][i];
        
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < row; j++) {
                for (int k = 0; k < row; k++) {
                    if (j == k) continue;
                    
                    int next = dp[i][j] + land[i + 1][k];
                    dp[i + 1][k] = Math.max(dp[i + 1][k], next);
                }
            }
        }

        for (int i : dp[n - 1]) answer = Math.max(answer, i);
        return answer;
    }
}