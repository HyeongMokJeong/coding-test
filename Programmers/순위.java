class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        int[][] dp = new int[n + 1][n + 1];
        
        for (int[] result : results) {
            int w = result[0]; int l = result[1];
            dp[w][l] = 1; dp[l][w] = -1;
        }

        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= n; j++){
                for (int k = 1; k <= n; k++){
                    if (dp[i][k] == 1 && dp[k][j] == 1){
                        dp[i][j] = 1;
                        dp[j][i] = -1;
                    }
                    if (dp[i][k] == -1 && dp[k][j] == -1){
                        dp[i][j] = -1;
                        dp[j][i] = 1;
                    }
                }
            }
        }

        for (int[] d : dp) {
            int temp = 0;
            for (int t : d) if (t != 0) temp += 1;
            if (temp == n - 1) answer++;
        }

        return answer;
    }
}