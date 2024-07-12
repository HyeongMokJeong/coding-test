import java.util.Arrays;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);

        long lp = 0; long rp = times[times.length - 1] * (long)n;

        while (lp <= rp) {
            long pivot = (rp + lp) / 2;
            long temp = 0;
            for (int i = 0; i < times.length; i++) temp += pivot / times[i];
            if (temp >= n) {
                answer = pivot;
                rp = pivot - 1;
            } else {
                lp = pivot + 1;
            }
        }

        return answer;
    }
}