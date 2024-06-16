class Solution {
    public long solution(int[] sequence) {
        long answer = 0;
        long purse = -1; long dp1 = 0; long dp2 = 0;

        for (int s : sequence) {
            dp1 += purse * s;
            dp2 += -purse * s;

            dp1 = Math.max(0, dp1);
            dp2 = Math.max(0, dp2);

            answer = Math.max(answer, Math.max(dp1, dp2));

            purse *= -1;
        }

        return answer;
    }
}