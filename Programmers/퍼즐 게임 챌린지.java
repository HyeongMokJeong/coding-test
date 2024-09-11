import java.util.Arrays;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        long s = diffs[0], e = Arrays.stream(diffs).max().getAsInt();
        int answer = (int) e;

        while (s <= e) {
            long pivot = (s + e) / 2;
            boolean result = check(pivot, diffs, times, limit);

            if (result) {
                answer = (int) Math.min(answer, pivot);
                e = pivot - 1;
            } else s = pivot + 1;
        }

        return answer;
    }

    private boolean check(long pivot, int[] diffs, int[] times, long limit) {
        long temp = 0;
        
        for (int i = 0; i < diffs.length; i++) {
            if (diffs[i] <= pivot) temp += times[i];
            else temp += (times[i - 1] + times[i]) * (diffs[i] - pivot) + times[i];
            if (temp > limit) return false;
        }
        return true;
    }
}