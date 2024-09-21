class Solution {
    public int solution(int temperature, int t1, int t2, int a, int b, int[] onboard) {
        // 최댓값
        int k = 1000 * 100;
        // 온도 범위가 -10 부터기 때문에 0으로 맞춤
        t1 += 10; t2 += 10; temperature += 10;

        int[][] dp = new int[onboard.length][51];
        for (int i = 0; i < onboard.length; i++) {
            for (int j = 0; j < 51; j++) dp[i][j] = k;
        }
        dp[0][temperature] = 0;

        // 온도를 내릴지 올릴지
        int flag = (temperature > t2) ? -1 : 1;

        for (int i = 1; i < onboard.length; i++) {
            for (int j = 0; j < 51; j++) {
                int temp = k;
                // i분에 손님이 있고 적정온도이거나, 손님이 없는 경우에는 최소 전력량 갱신 필요
                if ((onboard[i] == 1 && t1 <= j && j <= t2) || onboard[i] == 0) {
                    // 에어컨을 켜지 않은 경우
                    // 1도 상승
                    if (0 <= j + flag && j + flag <= 50) temp = Math.min(temp, dp[i - 1][j + flag]);
                    // 유지
                    if (j == temperature) temp = Math.min(temp, dp[i - 1][j]);
                    // 에어컨을 켠 경우
                    // 1도 하강
                    if (0 <= j - flag && j - flag <= 50) temp = Math.min(temp, dp[i - 1][j - flag] + a);
                    // 유지
                    if (t1 <= j && j <= t2) temp = Math.min(temp, dp[i - 1][j] + b);

                    dp[i][j] = temp;
                }
            }
        }

        int answer = k;
        for (int j = 0; j < 51; j++) answer = Math.min(answer, dp[onboard.length - 1][j]);
        
        return answer;
    }
}