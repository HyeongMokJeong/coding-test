class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        // dp[][][0] : 아래쪽으로 이동 가능한 경우
        // dp[][][1] : 오른쪽으로 이동 가능한 경우
        int[][][] dp = new int[m + 1][n + 1][2];
        dp[1][1][0] = dp[1][1][1] = 1;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (cityMap[i - 1][j - 1] == 0) {
                    dp[i][j][0] += (dp[i - 1][j][0] + dp[i][j - 1][1]) % MOD;
                    dp[i][j][1] += (dp[i - 1][j][0] + dp[i][j - 1][1]) % MOD;
                } else if (cityMap[i - 1][j - 1] == 2) {
                    dp[i][j][0] = dp[i - 1][j][0];
                    dp[i][j][1] = dp[i][j - 1][1];
                }
            }
        }
        // 도착점은 0이기 때문에 dp[][][0]과 dp[][][1]이 같다.
        return dp[m][n][0];
    }
}