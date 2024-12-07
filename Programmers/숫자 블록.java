import java.util.*;

class Solution {
    public int[] solution(long begin, long end) {
        int b = (int) begin;
        int e = (int) end;
        int[] answer = new int[e - b + 1];
        
        for (int i = b; i <= e; i++) {
            answer[i - b] = calculate(i);
        }
        if (b == 1) answer[0] = 0;
        
        return answer;
    }
    
    private int calculate(int target) {
        int result = 1;
        
        for (int i = 2; i * i <= target; i++) {
            if (target % i == 0) {
                if (target / i <= 10000000) return target / i;
                result = i;
            }
        }
        return result;
    }
}