class Solution {
    int[][] dp;
    public int[] solution(int target) {
        //dp[i][0] = c, 점수: i, 던진 횟수: c
        //dp[i][1] = s, 싱글/불 맞춘 횟수: s
        dp = new int[target + 1][2];
        for(int i = 0; i <= target; i++){
            dp[i][0] = Integer.MAX_VALUE;
            dp[i][1] = 0;
        }
        dp[0][0] = 0;

        int bull = 50;
        for (int i = 1; i <= target; i++) {
            for (int j = 1; j <= 20; j++) {
                // 싱글
                if (i - j >= 0) {
                    // 더 적은 경우라면 갱신
                    if (dp[i][0] > dp[i - j][0] + 1) {
                        dp[i][0] = dp[i - j][0] + 1;
                        dp[i][1] = dp[i - j][1] + 1;
                    }
                    // 만약 던진 횟수가 똑같다면, 싱글/불 맞춘 횟수가 더 높은 것으로 갱신
                    else if (dp[i][0] == dp[i - j][0] + 1) {
                        dp[i][1] = Math.max(dp[i][1], dp[i - j][1] + 1);
                    }
                }

                // 불
                if (i - bull >= 0) {
                    if (dp[i][0] > dp[i - bull][0] + 1) {
                        dp[i][0] = dp[i - bull][0] + 1;
                        dp[i][1] = dp[i - bull][1] + 1;
                    }
                    else if (dp[i][0] == dp[i - bull][0] + 1) {
                        dp[i][1] = Math.max(dp[i][1], dp[i - bull][1] + 1);
                    }
                }

                // 더블
                if (i - j * 2 >= 0) {
                    // 더 적은 경우라면 갱신하되, 싱글/불 맞춘 횟수는 유지한다.
                    if (dp[i][0] > dp[i - j * 2][0] + 1) {
                        dp[i][0] = dp[i - j * 2][0] + 1;
                        dp[i][1] = dp[i - j * 2][1];
                    }
                }

                // 트리플
                if (i - j * 3 >= 0) {
                    if (dp[i][0] > dp[i - j * 3][0] + 1) {
                        dp[i][0] = dp[i - j * 3][0] + 1;
                        dp[i][1] = dp[i - j * 3][1];
                    }
                }
            }
        }
        
        return new int[]{dp[target][0], dp[target][1]};
    }
}