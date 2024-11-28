class Solution {
    public int solution(int sticker[]) {
        int answer = 0;
        int n = sticker.length;
        
        if (sticker.length == 1) return sticker[0];

        int[] dp = new int[n];
        // 첫 스티커를 뜯은 경우
        dp[0] = sticker[0];
        dp[1] = dp[0];
        // 첫 스티커 = 마지막 스티커이기 때문에 n - 2까지
        for (int i = 2; i < n - 1; i++) {
            // 2칸 전 스티커와 현재 스티커를 뗄지, 1칸 전 스티커를 떼고 현재 스티커를 포기할지
            dp[i] = Math.max(dp[i - 2] + sticker[i], dp[i - 1]);
        }
        answer = dp[n - 2];
        
        // 첫 스티커를 뜯지 않은 경우
        dp[0] = 0;
        dp[1] = sticker[1];
        for (int i = 2; i < n; i++) {
            dp[i] = Math.max(dp[i - 2] + sticker[i], dp[i - 1]);
        }
        answer = Math.max(answer, dp[n - 1]);
        
        return answer;
    }
}