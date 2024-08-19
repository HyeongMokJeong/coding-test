import java.util.Arrays;

class Solution {
    public int[] solution(int n, int s) {
        int defaultValue = s / n;
        if (defaultValue == 0) return new int[]{ -1 };
        int remain = s - defaultValue * n;

        int[] answer = new int[n];
        Arrays.fill(answer, defaultValue);

        for (int i = n - remain; i < n; i++) answer[i] += 1;
        
        return answer;
    }
}