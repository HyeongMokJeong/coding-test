import java.util.Arrays;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        int[] count = new int[Arrays.stream(tangerine).max().getAsInt() + 1];
        for (int i : tangerine) count[i] += 1;
        
        Arrays.sort(count);
        for (int i = count.length - 1; i >= 0; i--) {
            answer += 1;
            k -= count[i];
            if (k <= 0) break;
        }
    
        return answer;
    }
}