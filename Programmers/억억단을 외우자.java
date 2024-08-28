class Solution {
    public int[] solution(int e, int[] starts) {
        // 약수의 개수가 가장 큰 숫자들 중 가장 작은 숫자

        // 약수 개수를 저장하는 배열 dp
        int[] dp = new int[e + 1];
        for (int i = 1; i <= e; i++) {
            for (int j = 1; j <= e / i; j++) dp[i * j] += 1;
        }

        // 구간 별 최대 약수 개수 + 최솟값 인덱스를 저장하는 배열 dp2
        int[] dp2 = new int[e + 1];

        dp2[e] = e;
        for (int i = e - 1; i >= 1; i--) {
            if (dp[i] >= dp[i + 1]) dp2[i] = i;
            else {
                dp2[i] = dp2[i + 1];
                dp[i] = dp[i + 1];
            }
        }
        int[] answer = new int[starts.length];
        for (int i = 0; i < starts.length; i++) answer[i] = dp2[starts[i]];
    
        return answer;
    }
}