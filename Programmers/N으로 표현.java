import java.util.*;

class Solution {
    private int size = 8;
    public int solution(int N, int number) {
        if (N == number) return 1;
        
        // dp[i]는 N이 i개일 때 가능한 모든 경우를 포함한다.
        Set<Integer>[] dp = new HashSet[size + 1];
        for (int i = 0; i <= size; i++) dp[i] = new HashSet<>();
        
        // dp[i]를 초기화한다.
        for (int i = 1; i <= size; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < i; j++) sb.append(N);
            dp[i].add(Integer.parseInt(sb.toString()));
        }
        
        // dp[j]의 모든 경우와 dp[i - j]의 모든 경우를 사칙연산하여 dp에 추가한다.
        for (int i = 2; i <= size; i++) {
            for (int j = 1; j < i; j++) {
                int k = i - j;
                
                for (int n1 : dp[j]) {
                    for (int n2 : dp[k]) {
                        dp[i].add(n1 + n2);
                        dp[i].add(n1 - n2);
                        dp[i].add(n1 * n2);
                        if (n2 != 0) dp[i].add(n1 / n2);
                    }
                }
            }
            if (dp[i].contains(number)) return i;
        }
        
        return -1;
    }
}